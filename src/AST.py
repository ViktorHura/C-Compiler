from src.visitors import *
from src.nodes import *

from src.LLVMContext import LLVMContext
from src.MIPSContext import MIPSContext

def buildAST(file_name:str):
    from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
    from src.grammar.CLexer import CLexer
    from src.grammar.CParser import CParser
    from src.ASTBuilder import ASTBuilder

    # build CST
    input_stream = FileStream(file_name)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.start()  # start with start
    
    walker = ParseTreeWalker()
    astb = ASTBuilder()
    walker.walk(astb, tree)
    
    ast = AST(astb.getRoot())
    errors = astb.getErrors()

    # clean up AST
    pass1 = ASTPruneReferenceDereference()
    pass2 = ASTPrunePass3()

    ast.m_root.acceptVisitor(pass1)
    ast.m_root.acceptVisitor(pass2)

    # return ast and errors
    return ast, errors + pass2.getErrors()

class AST:
    def __init__(self, r=None):
        if r is None:
            self.m_root = Block()
        else:
            self.m_root = r

    def toDot(self, showSymbolTable=True, showReachability=False):
        dotList = ["digraph AST {", "rankdir = BT;"]  # list of lines in our dot string

        self.acceptVisitor(ASTDotVisitor(dotList, showSymbolTable, showReachability))  # fill list using the Dot visitor

        dotList.append("}")

        dotString = ""  # combine the list of lines in to one string
        for line in dotList:
            dotString += line + "\n"  # separated by line breaks ofc
        return dotString

    def toLLVM(self):
        context = LLVMContext()
        self.m_root.generateLLVM(context)

        res = ''
        for line in context.code:
            res += line + '\n'

        return res

    def toMIPS(self):
        context = MIPSContext()
        self.m_root.generateMIPS(context)

        return context.toString()


    def buildSymbolTable(self):
        stb = ASTSymbolTableBuilder()
        self.acceptVisitor(stb)
        if len(stb.getErrors()) > 0:
            return stb.getErrors()

        # decorate types
        self.acceptVisitor(ASTTypeDecorator())

    def semanticAnalysis(self):
        analyser = ASTSemanticPass1()
        self.acceptVisitor(analyser)
        return analyser.getErrors(), analyser.getWarnings()

    def optimize(self):
        self.acceptVisitor(ASTReachableDecorator())
        ASTUnreachablePruner.prune(self.m_root)
        # propagate constants
        self.acceptVisitor(ASTConstantPropagation())
        # fold constants
        self.acceptVisitor(ASTConstantFolder())
        # remove unused variables
        finder = ASTUnusedVariableFinder()
        self.acceptVisitor(finder)
        pruner = ASTUnusedVariablePruner(finder.seen_vars)
        pruner.prune(self.m_root)
        # remove unused conditionals
        self.acceptVisitor(ASTUnusedConditionals())
        ASTUnusedConditionals.prune(self.m_root)

    def acceptVisitor(self, visitor):
        self.m_root.acceptVisitor(visitor)
