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


def test_propagation():
    err, ast = run("test/input/constant_propagation.c")
    assert len(err) == 0

    test_str = '''{
    "_python_object": "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"
}'''

    json_str = json.dumps(ast, cls=PythonObjectEncoder, indent=4)
    assert (json_str == test_str)




