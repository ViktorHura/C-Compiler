#!/bin/bash 

# generate llvm IR for input source file and execute it

# $1 = file name (without extension)
# $2 = extra options for main.py

DIRNAME=`dirname "$0"`
EXE="$DIRNAME/../main.py"

if [ -r "$1.c" ]; then
    echo "Generating llvm for $1.c"
    python3 "$EXE" $2 c2llvm "$1.c" > "$1.ll"
    lli "$1.ll" > "$1-.txt" || echo "-> error generating well formed LLVM IR"
    diff "$1_llvm.txt" "$1-.txt" && rm "$1-.txt" || echo "-> error generating correct LLVM IR"
else
    echo "No file named $1.c"
fi