#!/bin/bash 

# wrapper around various run scripts to handle batch processing

# $1 = command (dot/mips/llvm)
# $2 = c source file or directory containing source files
# $3 = extra options

DIRNAME=`dirname "$0"`
OPT="-s"

if [ $1 = "dot" ]
then
    ACTION="$DIRNAME/run_dot.sh"
elif [ $1 = "llvm" ]
then
    ACTION="$DIRNAME/run_llvm.sh"
elif [ $1 = "mips" ]
then
    ACTION="$DIRNAME/run_mips.sh"
else
    echo "Unknown command: $1"
fi

if [ -d "$2" ]
then
    for file in `find "$2" -type f -name "*.c"`
    do
        "$ACTION" "${file%.*}" "$3"
    done
elif [ -f "$2" ]
then
    "$ACTION" "${2%.*}" "$3"
else
    echo "No such file or directory: $2"
fi