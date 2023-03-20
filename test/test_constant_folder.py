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

def test_folding():
    err, ast = run("test/input/constant_folding.c")
    assert len(err) == 0

    test_str = '''{
    "_python_object": "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"
}'''

    json_str = json.dumps(ast, cls=PythonObjectEncoder, indent=4)
    assert (json_str == test_str)




