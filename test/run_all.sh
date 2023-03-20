#!/bin/bash 

# run all code generations tests

DIRNAME=`dirname "$0"`
INPUT="$DIRNAME/input"
RUN="$DIRNAME/run.sh"

"$RUN" dot "$INPUT/code"
"$RUN" dot "$INPUT/benchmarks_code"

"$RUN" llvm "$INPUT/code" -s
"$RUN" llvm "$INPUT/benchmarks_code" -s

"$RUN" mips "$INPUT/code" -s
"$RUN" mips "$INPUT/benchmarks_code" -s

# run with optimizations
# "$RUN" dot "$INPUT/code/unreachable_code.c" -so
# "$RUN" llvm "$INPUT/code/unreachable_code.c" -so
# "$RUN" mips "$INPUT/code/unreachable_code.c" -so
