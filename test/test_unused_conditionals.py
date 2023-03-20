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


def test_unused_conditionals():
    err, ast = run("test/input/unused_conditionals.c")
    assert len(err) == 0

    test_str = '''{
    "_python_object": "gASVqwYAAAAAAACMB3NyYy5BU1SUjANBU1SUk5QpgZR9lIwGbV9yb290lIwPc3JjLm5vZGVzLkJsb2NrlIwFQmxvY2uUk5QpgZR9lCiMCG1fcGFyZW50lE6MCm1fY2hpbGRyZW6UXZSMEnNyYy5ub2Rlcy5GdW5jdGlvbpSMCEZ1bmN0aW9ulJOUKYGUfZQoaAtoCWgMXZQojBtzcmMubm9kZXMuRnVuY3Rpb25QYXJhbWV0ZXKUjBFGdW5jdGlvblBhcmFtZXRlcpSTlCmBlH2UKGgLaBFoDF2UjAZsaW5lbnKUjAMxOjCUjAR0eXBllIwIc3JjLlR5cGWUjARUeXBllJOUKYGUfZQojAZpbnNpZGWUaB2MBUNUeXBllJOUSv////+FlFKUjAVjb25zdJSJjANwdHKUiYwKYXJyYXlfc2l6ZZSJdWKMEnRlcm1pbmF0aW5nX25vcm1hbJSIjAlyZWFjaGFibGWUiIwKaWRlbnRpZmllcpSMBG1haW6UdWJoCCmBlH2UKGgLaBFoDF2UKIwUc3JjLm5vZGVzLkRlY2xhcmF0b3KUjApEZWNsYXJhdG9ylJOUKYGUfZQoaAtoLmgMXZRoGowDMjo4lGgcaB8pgZR9lChoImgkSwSFlFKUaCeJaCiJaCmJdWJoKohoK4hoLIwBYZR1YmgIKYGUfZQoaAtoLmgMXZSMGHNyYy5ub2Rlcy5VbmFyeU9wZXJhdGlvbpSMDlVuYXJ5T3BlcmF0aW9ulJOUKYGUfZQoaAtoPWgMXZSMEnNyYy5ub2Rlcy5WYXJpYWJsZZSMCFZhcmlhYmxllJOUKYGUfZQoaAtoQ2gMXZRoGowDNTo5lGgcaDhoKohoK4iMBG5hbWWUaDyMC3Njb3BlX3RhYmxllIwPc3JjLlN5bWJvbFRhYmxllIwLU3ltYm9sVGFibGWUk5QpgZR9lCiMBGRhdGGUfZRoPGg0c4wFYmxvY2uUaC6MBnBhcmVudJRoUSmBlH2UKGhUfZRoLWgXc2hWaAloV051YnVidWJhaBqMAzU6OZRoHGg4aCqIaCuIjAhvcGVyYXRvcpSMBisrcG9zdJR1YmFoGowENDoxNpRoHE5oKohoK4hoTmhRKYGUfZQoaFR9lGhWaD1oV2hSdWJ1YmgIKYGUfZQoaAtoLmgMXZRoQimBlH2UKGgLaGJoDF2UaEgpgZR9lChoC2hlaAxdlGgajAQxNDo5lGgcaDhoKohoK4hoTWg8aE5oUnViYWgajAQxNDo3lGgcaDhoKohoK4hoXIwFKytwcmWUdWJhaBqMBTEzOjE2lGgcTmgqiGgriGhOaFEpgZR9lChoVH2UaFZoYmhXaFJ1YnViaAgpgZR9lChoC2guaAxdlGhCKYGUfZQoaAtocmgMXZRoSCmBlH2UKGgLaHVoDF2UaBqMBDIyOjmUaBxoOGgqiGgriGhNaDxoTmhSdWJhaBqMBDIyOjmUaBxoOGgqiGgriGhcjAYtLXBvc3SUdWJhaBqMBDIxOjmUaBxOaCqIaCuIaE5oUSmBlH2UKGhUfZRoVmhyaFdoUnVidWJoCCmBlH2UKGgLaC5oDF2UaEIpgZR9lChoC2iCaAxdlGhIKYGUfZQoaAtohWgMXZRoGowFMjY6MTGUaBxoOGgqiGgriGhNaDxoTmhSdWJhaBqMBDI2OjmUaBxoOGgqiGgriGhcjAUrK3ByZZR1YmFoGowFMjU6MTaUaBxOaCqIaCuIaE5oUSmBlH2UKGhUfZRoVmiCaFdoUnVidWJoCCmBlH2UKGgLaC5oDF2UaEIpgZR9lChoC2iSaAxdlGhIKYGUfZQoaAtolWgMXZRoGowFMzY6MTKUaBxoOGgqiGgriGhNaDxoTmhSdWJhaBqMBTM2OjEwlGgcaDhoKohoK4hoXIwFKytwcmWUdWJhaBqMBTM1OjE3lGgcTmgqiGgriGhOaFEpgZR9lChoVH2UaFZokmhXaFJ1YnViaAgpgZR9lChoC2guaAxdlGhCKYGUfZQoaAtoomgMXZRoSCmBlH2UKGgLaKVoDF2UaBqMBTQ2OjEylGgcaDhoKohoK4hoTWg8aE5oUnViYWgajAU0NjoxMJRoHGg4aCqIaCuIaFyMBS0tcHJllHViYWgajAQ0NTo5lGgcTmgqiGgriGhOaFEpgZR9lChoVH2UaFZoomhXaFJ1YnViZWgajAQxOjExlGgcTmgqiGgriGhOaFJ1YmVoGowDMTowlGgcaCBoKohoK4h1YmFoGowHdW5rbm93bpRoHE5oKohoK4hoTmhYdWJzYi4="
}'''

    json_str = json.dumps(ast, cls=PythonObjectEncoder, indent=4)
    assert (json_str == test_str)




