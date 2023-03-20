from src.AST import *


def run(file_name):
    # build AST from source file
    ast, errors = buildAST(file_name)

    # build symbol table
    errs = ast.buildSymbolTable()
    if errs:
        return errors + errs

    # semantic analysis
    errs, warnings = ast.semanticAnalysis()

    # optimisations
    ast.optimize()

    return errors + errs + warnings

def test_casts():
    err = run("test/input/warnings/casts.c")
    assert len(err) == 4
    assert err[0] == '[WARNING] on 10:8: Conversion from richer type: FLOAT, to poorer type: INT, could result in possible loss of information'
    assert err[1] == '[WARNING] on 11:8: Conversion from richer type: FLOAT, to poorer type: INT, could result in possible loss of information'
    assert err[2] == '[WARNING] on 17:9: Conversion from richer type: FLOAT, to poorer type: CHAR, could result in possible loss of information'
    assert err[3] == '[WARNING] on 18:9: Conversion from richer type: INT, to poorer type: CHAR, could result in possible loss of information'
