from src.SymbolTable import SymbolTable
from .ASTVisitor import *
import sys

from src.nodes import *


class ASTSymbolTableBuilder(ASTVisitor):
    def __init__(self):
        self.m_root = None
        self.m_current = self.m_root
        self.errors = []

    def getErrors(self) -> list:
        return self.errors

    def enterVariable(self, node: Variable):
        symbol = node.getValue()
        data, table = self.m_current.lookUpAndGet(symbol)
        if not data:
            err = '[E] on {}: Use of an undefined or uninitialized variable: {}' \
                .format(node.linenr, symbol)
            self.errors.append(err)
            return
        node.setSymbolTable(table)

    def enterDeclarator(self, node: Declarator):
        symbol = node.getIdentifier()
        added = self.m_current.declare(symbol, node)
        if not added:
            dec = self.m_current.lookUp(symbol)
            right = dec.getRightSiblingIfExists()
            # has it been initialised when first declared?
            initialised = right is not None and isinstance(right, Assignment) and right.isExplicit()
            # are we initialising during this declaration?
            nright = node.getRightSiblingIfExists()
            node_init = nright is not None and isinstance(nright, Assignment) and nright.isExplicit()

            globalvar = node.getParent().getParent() is None

            error = False
            if initialised:
                error = True
            else:  # hasn't been initialised so we are allowed to redeclare for some reason
                if dec.getType() == node.getType():  # check that types still match
                    if not globalvar and not node_init:  # must be initialising if not global var
                        error = True
                    else:
                        self.m_current.redeclare(symbol, node)
                else:
                    error = True

            if error:
                err = '[E] on {}: Redeclaration or redefinition of an existing variable: {} (first declared on {})'. \
                    format(node.linenr, symbol, self.m_current.lookUpDeclarator(symbol).linenr)
                self.errors.append(err)

    def enterBlock(self, node: Block):
        if self.m_root is None:
            self.m_root = SymbolTable(node)
            self.m_current = self.m_root
        elif node.getSymbolTable() is None:
            tbl = SymbolTable(node)
            tbl.parent = self.m_current
            self.m_current = tbl
        node.setSymbolTable(self.m_current)

    def exitBlock(self, node: Block):
        self.m_current = self.m_current.parent

    ### Function stuff ###

    def isFuncDefined(self, symbol):
        fparam = self.m_current.lookUp(symbol)
        funcConstruct = fparam.getParent()
        return isinstance(funcConstruct.getChild(-1), Block)

    def declareFuncVariables(self, func):
        block = func.getChild(-1)
        # create symbol table for the block
        tbl = SymbolTable(block)
        tbl.parent = self.m_current
        self.m_current = tbl
        block.scope_table = tbl
        # add all function arguments to the symbol table
        for i in range(1, len(func.m_children) - 1):
            par = func.getChild(i)
            symbol = par.getIdentifier()
            added = self.m_current.declare(symbol, func.getChild(i))
            if not added:
                raise Exception("somehow failed to declare the parameters of a function scope?? good luck!")

    def validfuncParams(self, func):
        seen = []
        urange = func.getChildrenCount() - 1
        if not isinstance(func.getChild(-1), Block):
            urange = urange + 1
        for i in range(1, urange):
            id = func.getChild(i).getIdentifier()
            if id not in seen:
                seen.append(id)
            else:
                return False
        return True

    def enterFunction(self, node: Function):
        symbol = node.getChild(0).getIdentifier()  # first child contains function name and return type
        definition = isinstance(node.getChild(-1), Block)  # are we defining the function already?
        declared = self.m_current.lookUp(symbol) is not None  # has the function been declared before
        if declared:
            declarator = self.m_current.lookUpDeclarator(symbol)
            dec_signature = declarator.getParent().getSignature()
        signature = node.getSignature()

        if not self.validfuncParams(node):
            err = '[E] on {}: Function parameters contain duplicate names' \
                .format(node.linenr)
            self.errors.append(err)
            return

        if definition:  # we are defining the function
            if not declared:  # it hasn't been declared before
                self.m_current.declare(symbol, node.getChild(0))  # declare the function in it's scope
                self.declareFuncVariables(node)  # declare the function parameters in the function scope
            else: # function is declared, but it mustn't be defined yet
                defined = self.isFuncDefined(symbol)

                if defined: # already defined previously
                    err = '[E] on {}: Redefinition of function : {} ,previously defined on {}' \
                        .format(node.linenr, symbol, declarator.linenr)
                    self.errors.append(err)
                else: # only forward declared previously
                    if dec_signature != signature:
                        err = '[E] on {}: Signature of function does not match the function : {} ,previously declared on {}' \
                            .format(node.linenr, symbol, declarator.linenr)
                        self.errors.append(err)
                        return

                    self.m_current.redeclare(symbol, node.getChild(0))  # redeclare the function in it's scope
                    self.declareFuncVariables(node)  # declare the function parameters in the function scope

        else:  # we are simply forward(or rearward?) declaring the function
            if not declared:  # it hasn't been declared before (forward declaration)
                self.m_current.declare(symbol, node.getChild(0))  # declare the function in it's scope
            else:  # redeclare or rearward declare I guess
                if dec_signature != signature:
                    err = '[E] on {}: Signature of function does not match the function : {} ,previously declared on {}' \
                        .format(node.linenr, symbol, declarator.linenr)
                    self.errors.append(err)

    def enterFunctionCall(self, node : FunctionCall):
        function_identifier = node.getIdentifier()
        
        function = self.m_current.lookUp(function_identifier)
        if function and isinstance(function.getParent(), Function):
            node.setValue(function.getParent())
        else:
            self.errors.append(f'[E] on {node.linenr}: Unknown function `{function_identifier}`.')
