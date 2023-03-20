cd $(dirname "$0")
java -jar bin/antlr-4.9.1.jar -Dlanguage=Python3 src/grammar/C.g4 -visitor