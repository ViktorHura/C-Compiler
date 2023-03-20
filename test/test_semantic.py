from src.AST import *

def run(file_name):
    # build AST from source file
    ast, errors = buildAST(file_name)

    # build symbol table
    errs = ast.buildSymbolTable()
    if errs:
        return errors + errs

    # semantic analysis
    errs, warns = ast.semanticAnalysis()

    # optimisations
    ast.optimize()
    
    return errors + errs

def test_happyday():
    err0 = run("test/input/happyday/basic_expressions.c")
    err1 = run("test/input/happyday/declarations.c")
    err2 = run("test/input/happyday/types.c")
    assert not err0
    assert not err1
    assert not err2

def test_const_declarations():
    err = run("test/input/const_declarations.c")
    assert len(err) == 3
    assert err[0] == '[E] on 5:0: Const variable must be initialised during declaration: ca (const INT)'
    assert err[1] == '[E] on 14:0: Const variable must be initialised during declaration: nca (INT * const)'
    assert err[2] == '[E] on 17:0: Const variable must be initialised during declaration: cca (const INT * const)'

def test_const_assignments():
    err = run("test/input/const_assignments.c")
    assert len(err) == 5
    assert err[0] == '[E] on 11:4: Assignment to a constant'
    assert err[1] == '[E] on 14:4: Assignment to a constant'
    assert err[2] == '[E] on 15:4: Assignment to a constant'
    assert err[3] == '[E] on 18:4: Assignment to a constant'
    assert err[4] == '[E] on 20:4: Assignment to a constant'

def test_variable_declarations():
    err = run("test/input/variable_declarations.c")
    assert len(err) == 2
    assert err[0] == '[E] on 2:4: Use of an undefined or uninitialized variable: a'
    assert err[1] == '[E] on 4:8: Redeclaration or redefinition of an existing variable: b (first declared on 3:8)'

def test_rvalue_assignment():
    err = run("test/input/rvalue_assignment.c")
    assert len(err) == 2
    assert err[0] == '[E] on 2:4: Assignment to an rvalue'
    assert err[1] == '[E] on 5:4: Assignment to an rvalue'

def test_pointer_operations():
    err = run("test/input/pointer_operations.c")
    assert len(err) == 11
    assert err[0] == '[E] on 3:10: Operation not allowed on pointer types: *'
    assert err[1] == '[E] on 5:10: Unary - on pointers not allowed'
    assert err[2] == '[E] on 6:10: Operation not allowed on pointer types: /'
    assert err[3] == '[E] on 10:10: Invalid subtraction of pointer'
    assert err[4] == '[E] on 14:10: Addition of pointer not allowed'
    assert err[5] == '[E] on 15:10: Operation not allowed on pointer types: *'
    assert err[6] == '[E] on 16:10: Operation not allowed on pointer types: /'
    assert err[7] == '[E] on 21:4: Conversion between floating point types and pointer types not allowed'
    assert err[8] == '[E] on 22:6: Conversion between floating point types and pointer types not allowed'
    assert err[9] == '[E] on 24:9: lvalue required as unary ‘&’ operand but got: INT Literal: 1'
    assert err[10] == '[E] on 27:4: Attempting to dereference a non-pointer: +: INT, INT -> INT'