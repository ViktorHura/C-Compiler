from src.AST import *
import os

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
    for file in os.listdir("test/input/benchmarks_code/"):
        if file.endswith(".c"):
            path = os.path.join("test/input/benchmarks_code/", file)
            err = run(path)
            if err:
                print(file)
            assert not err

def test_mainNotFound():
    err = run("test/input/benchmark_errors/mainNotFound.c")
    assert len(err) == 1
    assert err[0] == "[E] on 0:0: No main function is defined in the global scope"

def test_invalidUnaryOperation():
    err = run("test/input/benchmark_errors/invalidUnaryOperation.c")
    assert len(err) == 2
    assert err[0] == "[E] on 4:23: lvalue required as unary ‘++post’ operand but got: INT Literal: 9"
    assert err[1] == "[E] on 5:23: lvalue required as unary ‘--pre’ operand but got: INT Literal: 11"

def test_invalidIncludeError():
    err = run("test/input/benchmark_errors/invalidIncludeError.c")
    assert len(err) == 1
    assert err[0] == "[E] on 1:0: Unknown import: nonExistantFile.h"

def test_variableRedefinition1():
    err = run("test/input/benchmark_errors/variableRedefinition1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:8: Redeclaration or redefinition of an existing variable: x (first declared on 2:8)"

def test_variableRedefinition2():
    err = run("test/input/benchmark_errors/variableRedefinition2.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:10: Redeclaration or redefinition of an existing variable: x (first declared on 2:8)"

def test_variableRedefinition3():
    err = run("test/input/benchmark_errors/variableRedefinition3.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:7: Redeclaration or redefinition of an existing variable: x (first declared on 2:8)"

def test_variableRedefinition4():
    err = run("test/input/benchmark_errors/variableRedefinition4.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:6: Redeclaration or redefinition of an existing variable: x (first declared on 1:4)"

def test_variableRedefinition5():
    err = run("test/input/benchmark_errors/variableRedefinition5.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:4: Redeclaration or redefinition of an existing variable: x (first declared on 2:4)"

def test_variableRedefinition6():
    err = run("test/input/benchmark_errors/variableRedefinition6.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:6: Redeclaration or redefinition of an existing variable: x (first declared on 1:4)"

def test_undeclaredVariable1():
    err = run("test/input/benchmark_errors/undeclaredVariable1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 2:4: Use of an undefined or uninitialized variable: x"

def test_undeclaredVariable2():
    err = run("test/input/benchmark_errors/undeclaredVariable2.c")
    assert len(err) == 1
    assert err[0] == "[E] on 2:3: Use of an undefined or uninitialized variable: x"

def test_undeclaredVariable3():
    err = run("test/input/benchmark_errors/undeclaredVariable3.c")
    assert len(err) == 3
    assert err[0] == "[E] on 3:4: Use of an undefined or uninitialized variable: z"
    assert err[1] == "[E] on 3:8: Use of an undefined or uninitialized variable: x"
    assert err[2] == "[E] on 3:12: Use of an undefined or uninitialized variable: y"

def test_undeclaredFunction():
    err = run("test/input/benchmark_errors/undeclaredFunction.c")
    assert len(err) == 1
    assert err[0] == "[E] on 2:4: Unknown function `f`."

def test_returnTypeMismatch():
    err = run("test/input/benchmark_errors/returnTypeMismatch.c")
    assert len(err) == 1
    assert err[0] == "[E] on 2:4: Return type does not match the function return type, declared on 1:0"

def test_returnOutsideFunction():
    err = run("test/input/benchmark_errors/returnOutsideFunction.c")
    assert len(err) == 1

def test_pointerOperationError():
    err = run("test/input/benchmark_errors/pointerOperationError.c")
    assert len(err) == 1
    assert err[0] == "[E] on 5:8: Addition of pointer not allowed"

def test_parameterRedefinition1():
    err = run("test/input/benchmark_errors/parameterRedefinition1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:0: Function parameters contain duplicate names"

def test_parameterRedefinition2():
    err = run("test/input/benchmark_errors/parameterRedefinition2.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:0: Function parameters contain duplicate names"

def test_parameterRedefinition3():
    err = run("test/input/benchmark_errors/parameterRedefinition3.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:0: Function parameters contain duplicate names"

def test_invalidLoopControlStatement():
    err = run("test/input/benchmark_errors/invalidLoopControlStatement.c")
    assert len(err) == 2
    assert err[0] == "[E] on 2:1: Loop control statement used outside of a loop"
    assert err[1] == "[E] on 3:1: Loop control statement used outside of a loop"

def test_incompatibleTypes1():
    err = run("test/input/benchmark_errors/incompatibleTypes1.c")
    assert len(err) == 0

def test_incompatibleTypes2():
    err = run("test/input/benchmark_errors/incompatibleTypes2.c")
    assert len(err) == 0

def test_incompatibleTypes3():
    err = run("test/input/benchmark_errors/incompatibleTypes3.c")
    assert len(err) == 1
    assert err[0] == "[E] on 5:4: Invalid conversion from VOID type"

def test_incompatibleTypes4():
    err = run("test/input/benchmark_errors/incompatibleTypes4.c")
    assert len(err) == 0

def test_incompatibleTypes5():
    err = run("test/input/benchmark_errors/incompatibleTypes5.c")
    assert len(err) == 0

def test_incompatibleTypes6():
    err = run("test/input/benchmark_errors/incompatibleTypes6.c")
    assert len(err) == 1

def test_incompatibleTypes7():
    err = run("test/input/benchmark_errors/incompatibleTypes7.c")
    assert len(err) == 0

def test_functionRedefinition1():
    err = run("test/input/benchmark_errors/functionRedefinition1.c")
    assert len(err) == 3
    assert err[0] == "[E] on 7:0: Redefinition of function : f ,previously defined on 2:0"

def test_functionRedefinition2():
    err = run("test/input/benchmark_errors/functionRedefinition2.c")
    assert len(err) == 3
    assert err[0] == "[E] on 7:0: Redefinition of function : f ,previously defined on 2:0"

def test_functionRedefinition3():
    err = run("test/input/benchmark_errors/functionRedefinition3.c")
    assert len(err) == 3
    assert err[0] == "[E] on 7:0: Redefinition of function : f ,previously defined on 2:0"

def test_functionCallargumentMismatch1():
    err = run("test/input/benchmark_errors/functionCallargumentMismatch1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:4: Function call does not match function prototype \n expected: INT,INT,, but got INT,"

def test_functionCallargumentMismatch2():
    err = run("test/input/benchmark_errors/functionCallargumentMismatch2.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:4: Function call does not match function prototype \n expected: INT,, but got INT,INT,"

def test_functionCallargumentMismatch3():
    err = run("test/input/benchmark_errors/functionCallargumentMismatch3.c")
    assert len(err) == 1

def test_functionCallargumentMismatch4():
    err = run("test/input/benchmark_errors/functionCallargumentMismatch4.c")
    assert len(err) == 1

def test_dereferenceTypeMismatch1():
    err = run("test/input/benchmark_errors/dereferenceTypeMismatch1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 2:4: Attempting to dereference a non-pointer: INT Literal: 5"

def test_dereferenceTypeMismatch2():
    err = run("test/input/benchmark_errors/dereferenceTypeMismatch2.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:5: lvalue required as unary ‘&’ operand but got: INT Literal: 5"

def test_definitionInLocalScope():
    err = run("test/input/benchmark_errors/definitionInLocalScope.c")
    assert len(err) > 0
    err[0] = "[E] on 5:9: Unknown function `f`."

def test_declarationDefinitionMismatch1():
    err = run("test/input/benchmark_errors/declarationDefinitionMismatch1.c")
    assert len(err) == 3
    assert err[0] == "[E] on 5:0: Signature of function does not match the function : f ,previously declared on 2:0"

def test_declarationDefinitionMismatch2():
    err = run("test/input/benchmark_errors/declarationDefinitionMismatch2.c")
    assert len(err) == 2
    assert err[0] == "[E] on 5:0: Signature of function does not match the function : f ,previously declared on 2:0"

def test_declarationDefinitionMismatch3():
    err = run("test/input/benchmark_errors/declarationDefinitionMismatch3.c")
    assert len(err) == 2
    assert err[0] == "[E] on 5:0: Signature of function does not match the function : f ,previously declared on 2:0"

def test_declarationDeclarationMismatch1():
    err = run("test/input/benchmark_errors/declarationDeclarationMismatch1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 5:0: Signature of function does not match the function : f ,previously declared on 2:0"

def test_declarationDeclarationMismatch2():
    err = run("test/input/benchmark_errors/declarationDeclarationMismatch1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 5:0: Signature of function does not match the function : f ,previously declared on 2:0"

def test_declarationDeclarationMismatch3():
    err = run("test/input/benchmark_errors/declarationDeclarationMismatch1.c")
    assert len(err) == 1
    assert err[0] == "[E] on 5:0: Signature of function does not match the function : f ,previously declared on 2:0"

def test_arraySizeTypeMismatch():
    err = run("test/input/benchmark_errors/arraySizeTypeMismatch.c")
    assert len(err) == 1
    assert err[0] == "[E] on 2:8: Non integer array size: x[0.5]"

def test_arrayCompareError():
    err = run("test/input/benchmark_errors/arrayCompareError.c")
    assert len(err) == 1
    assert err[0] == "[E] on 4:4: Comparison of arrays"

def test_arrayAccessTypeMismatch():
    err = run("test/input/benchmark_errors/arrayAccessTypeMismatch.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:4: Array index is not an integer"

def test_arrayAccessTypeMismatch2():
    err = run("test/input/benchmark_errors/arrayAccessTypeMismatch2.c")
    assert len(err) == 1
    assert err[0] == "[E] on 3:4: Array operator on non-array"
