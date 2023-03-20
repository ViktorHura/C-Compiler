grammar C;

/* 
    Parser rules
*/

start: ( function_declaration (SEMICOLON | compound_statement ) | declaration SEMICOLON | macro )*; // function or global variable

function_declaration: return_type IDENTIFIER LPAREN ( function_parameter (COMMA function_parameter)*)? RPAREN;

function_parameter: type_specifier (STAR_OP CONST?)? IDENTIFIER;

return_type: ((FLOAT | INT | CHAR) STAR_OP?) | VOID;

macro: INCLUDE LT_OP PATH GT_OP;

statement: compound_statement
    | expression SEMICOLON 
    | selection_statement 
    | iteration_statement
    | jump_statement;

compound_statement: LBRACE (statement | declaration SEMICOLON)* RBRACE;

selection_statement: IF LPAREN expression RPAREN statement 
    | IF LPAREN expression RPAREN statement ELSE statement
    | SWITCH LPAREN expression RPAREN statement;

iteration_statement: WHILE LPAREN expression RPAREN statement
    | DO statement WHILE LPAREN expression RPAREN SEMICOLON
    | FOR LPAREN init=declaration? SEMICOLON cond=expression? SEMICOLON iteration=expression? RPAREN statement;

jump_statement: BREAK SEMICOLON
    | CONTINUE SEMICOLON 
    | RETURN expression? SEMICOLON;

// precedence based on https://en.cppreference.com/w/c/language/operator_precedence
expression: expression op=(INCREMENT_OP | DECREMENT_OP)
    | function_call
    | expression op=LBRACKET expression RBRACKET
    | op=(PLUS_OP | MINUS_OP | STAR_OP | AMPERSAND_OP | NOT_OP | INCREMENT_OP | DECREMENT_OP /*| TILDE_OP | SIZEOF*/) expression
    | LPAREN explicit_cast_type RPAREN expression
    | expression op=(STAR_OP | SLASH_OP | PERCENT_OP) expression
    | expression op=(PLUS_OP | MINUS_OP) expression
    //| expression op=(SHIFTL_OP | SHIFTR_OP) expression
    | expression op=(LT_OP | LE_OP | GT_OP | GE_OP) expression
    | expression op=(EQ_OP | NEQ_OP) expression
    //| expression op=AMPERSAND_OP expression
    //| expression op=CARET_OP expression
    //| expression op=BAR_OP expression
    | expression op=AND_OP expression
    | expression op=OR_OP expression
    | <assoc=right> expression op=(ASSIGN_OP | PLUS_ASSIGN_OP | MINUS_ASSIGN_OP | STAR_ASSIGN_OP | SLASH_ASSIGN_OP | PERCENT_ASSIGN_OP | SHIFTL_ASSIGN_OP | SHIFTR_ASSING_OP | AMPERSAND_ASSIGN_OP | CARET_ASSIGN_OP | BAR_ASSIGN_OP) expression
    | LPAREN expression RPAREN
    | variable
    | literal;

literal: CHAR_LITERAL # char 
    | STRING_LITERAL # string
    | INT_LITERAL  # int
    | REAL_LITERAL # real;

variable: IDENTIFIER;

type_specifier: CONST? (FLOAT | INT | CHAR) CONST?;

explicit_cast_type: FLOAT | INT | CHAR;

declaration: type_specifier declarator (COMMA declarator)*;
declarator: (STAR_OP CONST?)* IDENTIFIER (LBRACKET INT_LITERAL RBRACKET)? (ASSIGN_OP expression)?;

function_call: IDENTIFIER LPAREN (expression (COMMA expression)*)? RPAREN;


/* 
    Lexer rules
*/

// keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CHAR: 'char';
CONST: 'const';
CONTINUE: 'continue';
DEFAULT: 'default';
DO: 'do';
DOUBLE: 'double';
ELSE: 'else';
ENUM: 'enum';
EXTERN: 'extern';
FLOAT: 'float';
FOR: 'for';
GOTO: 'goto';
IF: 'if';
INT: 'int';
LONG: 'long';
REGISTER: 'register';
RETURN: 'return';
SHORT: 'short';
SIGNED: 'signed';
SIZEOF: 'sizeof';
STATIC: 'static';
STRUCT: 'struct';
SWITCH: 'switch';
TYPEDEF: 'typedef';
UNION: 'union';
UNSIGNED: 'unsigned';
VOID: 'void';
VOLATILE: 'volatile';
WHILE: 'while';

// operators
ASSIGN_OP: '=';
PLUS_ASSIGN_OP: '+=';
MINUS_ASSIGN_OP: '-=';
STAR_ASSIGN_OP: '*=';
SLASH_ASSIGN_OP: '/=';
PERCENT_ASSIGN_OP: '%=';
AMPERSAND_ASSIGN_OP: '&=';
BAR_ASSIGN_OP: '|=';
CARET_ASSIGN_OP: '^=';
SHIFTL_ASSIGN_OP: '<<=';
SHIFTR_ASSING_OP: '>>=';

INCREMENT_OP: '++';
DECREMENT_OP: '--';

PLUS_OP: '+';
MINUS_OP: '-';
STAR_OP: '*';
SLASH_OP: '/';
PERCENT_OP: '%';
TILDE_OP: '~';
AMPERSAND_OP: '&';
BAR_OP: '|';
CARET_OP: '^';
SHIFTL_OP: '<<';
SHIFTR_OP: '>>';

NOT_OP: '!';
AND_OP: '&&';
OR_OP: '||';

EQ_OP: '==';
NEQ_OP: '!=';
LT_OP: '<';
LE_OP: '<=';
GT_OP: '>';
GE_OP: '>=';

DOT_OP: '.';
ARROW_OP: '->';

QUESTION_OP: '?';

// punctuation
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';

COLON: ':';
SEMICOLON: ';';
COMMA: ',';

// other
fragment DEC_LIT: [0-9]+;
fragment INT_SUFFIX: [uUlL];
INT_LITERAL: DEC_LIT INT_SUFFIX?;

fragment REAL_SUFFIX: [fFlL];
REAL_LITERAL: [0-9]*'.'[0-9]+ REAL_SUFFIX?;

// https://en.wikipedia.org/wiki/Escape_sequences_in_C
fragment CCHAR: ~['"\\\n] | '\\'[abfnrtv\\'"?];
CHAR_LITERAL: '\''(CCHAR | '"')'\'';
STRING_LITERAL: '"'(CCHAR | '\'')*'"';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

INCLUDE: '#include';
PATH: [a-zA-Z_./]+;

COMMENT: '/*' .*? '*/' -> channel(2);
LINE_COMMENT: '//' (.)*? '\n' -> channel(2);

WS: [ \n\t\r]+ -> skip; // Define whitespace rule, toss it out





