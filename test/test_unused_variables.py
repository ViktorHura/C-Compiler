import json

from src.AST import *

import base64
from collections.abc import MutableMapping
import json
import pickle


# https://stackoverflow.com/questions/23595801/how-to-serialize-a-tree-class-object-structure-into-json-file-format
class PythonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        return {'_python_object':
                base64.b64encode(pickle.dumps(obj)).decode('utf-8') }


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(base64.b64decode(dct['_python_object']))
    return dct


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

    return errors + errs, ast


def test_unused_variables():
    err, ast = run("test/input/unused_variables.c")
    assert len(err) == 0

    test_str = '''{
    "_python_object": "gASVtAQAAAAAAACMB3NyYy5BU1SUjANBU1SUk5QpgZR9lIwGbV9yb290lIwPc3JjLm5vZGVzLkJsb2NrlIwFQmxvY2uUk5QpgZR9lCiMCG1fcGFyZW50lE6MCm1fY2hpbGRyZW6UXZQojBJzcmMubm9kZXMuRnVuY3Rpb26UjAhGdW5jdGlvbpSTlCmBlH2UKGgLaAloDF2UKIwbc3JjLm5vZGVzLkZ1bmN0aW9uUGFyYW1ldGVylIwRRnVuY3Rpb25QYXJhbWV0ZXKUk5QpgZR9lChoC2gRaAxdlIwGbGluZW5ylIwDMTowlIwEdHlwZZSMCHNyYy5UeXBllIwEVHlwZZSTlCmBlH2UKIwGaW5zaWRllGgdjAVDVHlwZZSTlEr/////hZRSlIwFY29uc3SUiYwDcHRylImMCmFycmF5X3NpemWUiXVijBJ0ZXJtaW5hdGluZ19ub3JtYWyUiIwJcmVhY2hhYmxllIiMCmlkZW50aWZpZXKUjARmdW5jlHViaBYpgZR9lChoC2gRaAxdlGgajAQxOjEwlGgcaB8pgZR9lChoImgkSwSFlFKUaCeJaCiJaCmJdWJoKohoK4hoLIwBYZR1YmgIKYGUfZQoaAtoEWgMXZRoGowEMToxNpRoHE5oKohoK4iMC3Njb3BlX3RhYmxllIwPc3JjLlN5bWJvbFRhYmxllIwLU3ltYm9sVGFibGWUk5QpgZR9lCiMBGRhdGGUfZRoNmguc4wFYmxvY2uUaDeMBnBhcmVudJRoPimBlH2UKGhBfZQoaC1oF4wEbWFpbpRoFimBlH2UKGgLaBApgZR9lChoC2gJaAxdlChoSWgIKYGUfZQoaAtoS2gMXZQojBRzcmMubm9kZXMuRGVjbGFyYXRvcpSMCkRlY2xhcmF0b3KUk5QpgZR9lChoC2hOaAxdlGgajAQxMDo4lGgcaB8pgZR9lChoImg1aCeJaCiJaCmJdWJoKohoK4hoLIwBZJR1YowUc3JjLm5vZGVzLkFzc2lnbm1lbnSUjApBc3NpZ25tZW50lJOUKYGUfZQoaAtoTmgMXZQojBJzcmMubm9kZXMuVmFyaWFibGWUjAhWYXJpYWJsZZSTlCmBlH2UKGgLaF5oDF2UaBqMBDExOjSUaBxoWGgqiGgriIwEbmFtZZRoWmg7aD4pgZR9lChoQX2UaFpoVHNoQ2hOaERoRXVidWKMEXNyYy5ub2Rlcy5MaXRlcmFslIwHTGl0ZXJhbJSTlCmBlH2UKGgLaF5oDF2UaBqMBDExOjaUaBxoHymBlH2UKGgiaDVoJ4loKIloKYl1YmgqiGgriIwHbV92YWx1ZZRLAowGc2lnbmVklIh1YmVoGowEMTE6NJRoHGhYaCqIaCuIjAhleHBsaWNpdJSJdWJlaBqMBDU6MTGUaBxOaCqIaCuIaDtoaXViZWgajAM1OjCUaBxoHymBlH2UKGgiaCZoJ4loKIloKYl1YmgqiGgriHViaAxdlGgajAM1OjCUaBxoe2gqiGgriGgsaEh1YnVoQ2gJaEROdWJ1YnViZWgajAMxOjCUaBxoIGgqiGgriHViaEtlaBqMB3Vua25vd26UaBxOaCqIaCuIaDtoRXVic2Iu"
}'''

    json_str = json.dumps(ast, cls=PythonObjectEncoder, indent=4)
    assert (json_str == test_str)




