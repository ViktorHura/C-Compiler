#!/bin/bash 

# generate mips asm for input source file and execute it

# $1 = file name (without extension)
# $2 = extra options for main.py

DIRNAME=`dirname "$0"`
EXE="$DIRNAME/../main.py"
MARS="$DIRNAME/../bin/mars.jar"

if [ -r "$1.c" ]; then
    echo "Generating mips for $1.c"
    python3 "$EXE" $2 c2mips "$1.c" > "$1.asm"
    java -jar "$MARS" "$1.asm" | tail -n +3 > "$1-.txt" || echo "-> error generating well formed ASM"
    diff "$1_mips.txt" "$1-.txt" && rm "$1-.txt" || echo "-> error generating correct ASM"
else
    echo "No file named $1.c"
fi