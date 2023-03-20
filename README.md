# Compilers-Project
This was a  project for the Compilers course at UAntwerpen

An ANTLR based compiler for (subset of) C,
compiles to LLVM-IR and MIPS-32 assembly

With an output representation of the AST in dot format

__Students__: Noah Daniels & Viktor Hura

__Grade__: 20/20

This repository contains instructions on how to run our compiler and a report discussing our progress


## Status

All benchmarks work. All mandatory features and a selection of optional features work.

Below is a list of implemented features, available for both the LLVM-IR and MIPS-32 backend:

### Mandatory feautures:

+ Expressions
    + Binary operations +, -, *, and /
    + Binary operations >, <, and ==
    + Unary operators + and -
    + Brackets to overwrite the order of operations

+ Variables
  + Primitive data types _char_, _float_, _int_, and _pointer_
  + _const_ keyword
  + Variable declarations, definitions, assignment statements, and identifiers appearing in expressions
  + Unary pointer operators * and &

+ Comments

+ Basic printf and scanf support
  + by `#include <stdio.h>`
  + the format string allows interpretation of sequences of the form _%[width][code]_
  + support for type codes _d_, _i_, _s_ and _c_
  + no support for flags and modifiers

+ Loops and Conditionals
  + Support for _if_, _else_, _while_, _for_, _break_, and _continue_ keywords
  + Support for unnamed scopes as well as scopes from loops and
     conditionals

+ Functions
  + Definition and calling of functions and procedures, including support for passing parameters of basic types by value as well as by reference
    (pointers).
  + Local and global variables
  + Support for function scopes, next to the previously supported
    scopes from loops and conditionals.
  + _return_ and _void_ keywords

+ Arrays
  + Array variables supported, as well as operations on individual array elements
  

+ Error Analysis
  + Syntax error check
    + Compiler will stop when it encounters a syntax error 
    + An indication of the location of the syntax error will be displayed
    
  + Semantic error check
    + Use of an undefined or uninitialized variable
    + Redeclaration or redefinition of an existing variable (within the same scope)
    + Operations or assignments of incompatible types
    + Assignment to an rvalue
    + Assignment to a const variable
    + Consistency of a return statement with the type of the enclosing function
    + Consistency between forward declarations and function definition signatures

### Optional features:

+ Extra operators
    + Binary operator %
        + `test/input/code/modulo.c`
        + `test/input/constant_folding.c`
        + `test/input/benchmarks_code/modulo.c`
    + Comparison operators >=, <= and !=
        + `test/input/benchmarks_code/comparisons2.c`
        + `test/input/constant_folding.c`
    + Logical operators &&, || and !
        + `test/input/benchmarks_code/comparisons1.c`
        + `test/input/constant_folding.c`
+ Constant folding (optimization)
    + `test/input/constant_folding.c`
    
+ Implicit conversions of compatible types with conversion warnings and explicit casts
    + `test/input/warnings/casts.c`
    + `test/input/code/casts.c`
+ Identifier Operations ++ and -- (pre- and postfix)
    + `test/input/benchmarks_code/unaryOperations.c`
+ Constant propagation (optimization)
    + `test/input/constant_propagation.c`
    
+ Omit code generation for unused variables (optimization)
    + `test/input/unused_variables.c`
+ Omit code generation for conditionals that are never true (or ignore the else if always true) (optimization)
    + `test/input/unused_conditionals.c`
## Instructions

To install:

    virtualenv -p python3 env
    source env/bin/activate
    pip3 install -e .

The following command runs the compiler

    python3 main.py [options] command <input_file>

The compiler has three supported commands:

+ c2dot: output representation of the AST in dot format
+ c2llvm: output generated LLVM IR
+ c2mips: output generated MIPS assembly

The compiler also has two optional options:

+ -s (--silent): supress warnings
+ -o (--opt): enable optimizations (see optional features)

## Tests

The following command runs all semantic analysis tests

    pytest

_Note that pytest should be run from the root_

In the `test/` folder you will find some shell scripts to test code generation (make sure that all scripts are executable). To run all provided tests, execute:

    test/run_all.sh

This runs the provided benchmarks as well as our own. The source files can be found in `test/input/code` and `test/input/benchmarks_code`. All generated code and images will be placed in those folder also.

The script runs in three stages:

1. For all source files, a dot representation is generated and converted to an image (png).

2. For all source files, LLVM IR code is generated. The code is executed and the output gets saved to a temporary file. This file is checked against the expected output. If the outputs match, the temporary is deleted and the script continues with the next file. If there is an error, it is reported and the temporary file remains for closer inspection.

3. Same as in 2, except for MIPS instead of LLVM. Note that there are different expected outputs for llvm and mips. This is because there are slight differences such as extra line breaks or different precision.

Note that for the script to run LLVM IR, the `lli` command must be available. To run MIPS, the MARS MIPS simulator should be present in the root `bin` directory.

**Note that the script will pause several times and wait for an input**
These are the inputs it expects:

`Generating ... for test/input/benchmarks_code/prime.c`
+ `10`

`Generating ... for test/input/benchmarks_code/scanf1.c`
+ `10` [enter] `10`

`Generating ... for test/input/benchmarks_code/fibonacciRecursive.c`
+ `10`

`Generating ... for test/input/benchmarks_code/scanf2.c`
+ `hello`

More information about our own benchmars can be found in the source files.

#### File structure
```
Root
├── bin                         # required binaries
│   ├── antlr-4.9.1.jar
│   └── mars.jar
├── main.py
├── README.md
├── run_antlr.sh
├── setup.py
├── src
└── test                        # test scripts
    ├── input                   # our semantic test files (no output, checking errors or ast)
    │   ├── benchmark_errors    # benchmark semantic test files (no output, checking errors)
    │   ├── benchmarks_code     # benchmark code generation test files
    │   ├── code                # our code generation test files
    │   ├── happyday            # benchmark semantic test files (no output, checking errors)
    │   └── warnings            # our semantic test files (no output, checking warnings)
    ├── run_all.sh
    ├── run_dot.sh
    ├── run_llvm.sh
    ├── run_mips.sh
    └── run.sh
```