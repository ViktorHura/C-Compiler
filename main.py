from src.AST import AST, buildAST
import sys
import getopt

if __name__ == '__main__':

    # parse arguments
    options, remaining = getopt.getopt(sys.argv[1:], 'so', ['silent', 'opt'])

    assert len(remaining) == 2
    operation = remaining[0]
    filename = remaining[1]

    options_list = [option[0] for option in options]
    opt = '--opt' in options_list or '-o' in options_list
    silent = '--silent' in options_list or '-s' in options_list

    sys.setrecursionlimit(1000000)

    # build AST from source file
    ast, errors = buildAST(filename)
    for err in errors:
        print(err, file=sys.stderr)
    if not ast:
        sys.exit("Encountered errors while parsing source file. ABorting...")

    # build symbol table
    errors = ast.buildSymbolTable()
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        sys.exit("Encountered errors while building symbol table. Aborting...")

    # semantic analysis
    errors, warnings = ast.semanticAnalysis()
    if not silent:
        for warn in warnings:
            print(warn, file=sys.stderr)
    for err in errors:
        print(err, file=sys.stderr)

    # optimisations
    if opt:
        ast.optimize()

    if operation == 'c2dot':
        print(ast.toDot())
    elif operation == 'c2llvm':
        print(ast.toLLVM())
    elif operation == 'c2mips':
        print(ast.toMIPS())