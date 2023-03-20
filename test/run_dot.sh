#!/bin/bash 

# generate dot representation for input source file and create png

# $1 = file name (without extension)
# $2 = extra options for main.py

DIRNAME=`dirname "$0"`
EXE="$DIRNAME/../main.py"

if [ -r "$1.c" ]; then
    echo "Generating dot for $1.c"
    python3 "$EXE" $2 c2dot "$1.c" > "$1.dot"
    dot -Tpng "$1.dot" -o "$1.png"
    rm "$1.dot"
else
    echo "No file named $1.c"
fi