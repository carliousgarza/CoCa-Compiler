grammar patito;

@header {
  from Compiler.compiler import *
  from Compiler.function import *
  from Compiler.variable import *
  from Compiler.interpreter import *
  interpreter = Interpreter()
}

//Ignore whitespace
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS : [ \t\r\n]+ -> skip ;

//Symbols
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
EQUAL: '==';
NOT_EQUAL: '!=';
ASSIGN: '=';
AND: '&&';
OR: '||';
ADD: '+';
SUB: '-';
MULT: '*';
DIV: '/';
LEFT_PARENTHESIS: '(';
RIGHT_PARENTHESIS: ')';
LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';
LEFT_CURLY: '{';
RIGHT_CURLY: '}';
DETERMINANT: '$';
TRANSPOSE: '¡';
INVERSE: '?';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';

//Words
PROGRAM: 'program';
MAIN: 'main';
FUNCTION: 'function';
RETURN: 'return';
INPUT: 'input';
PRINT: 'print';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
FROM: 'from';
TO: 'to';
VAR: 'var';
BOOL: 'bool';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
CHAR: 'char';

//Constants
CTE_BOOL: 'true' | 'false';
CTE_FLOAT: [0-9]+.[0-9]+;
CTE_INT: [0-9]+;
CTE_CHAR: [.];
CTE_STRING: '"' .*? '"';
VOID: 'void';
ID: [_A-Za-z]([_A-Za-z0-9])*;

program
  : PROGRAM ID SEMICOLON declarevars functions mainfunc
  ;

declarevars
  : VAR variables+
  ;

variables
  : vartypes COLON varindividual (COMMA varindividual)* SEMICOLON
  ;

vartypes
  : (INT | BOOL | FLOAT | STRING | CHAR)
  ;

constant
  : (CTE_BOOL | CTE_FLOAT | CTE_INT | CTE_CHAR | CTE_STRING)
  ;

varindividual
  : ID (LEFT_BRACKET CTE_INT RIGHT_BRACKET | LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET)?
  ;

functions
  : function+
  ;

function
  : FUNCTION (vartypes | VOID) ID LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS declarevars? LEFT_CURLY statute? RIGHT_CURLY
  ;

parameters
  : vartypes ID (COMMA vartypes ID)*
  ;

hexp
  : mexp (ASSIGN mexp)*
  ;

mexp
  : sexp ((AND {interpreter.addOperator($AND.text)} | OR {interpreter.addOperator($OR.text)} ) sexp)*
  ;

sexp
  : exp ((GREATER {interpreter.addOperator($GREATER.text)} |
      LESS {interpreter.addOperator($LESS.text)} |
      GREATER_EQUAL {interpreter.addOperator($GREATER_EQUAL.text)} |
      LESS_EQUAL {interpreter.addOperator($LESS_EQUAL.text)} |
      NOT_EQUAL {interpreter.addOperator($NOT_EQUAL.text)} |
      EQUAL {interpreter.addOperator($EQUAL.text)} ) exp)?
  ;

exp
  : term ((ADD {interpreter.addOperator($ADD.text)} | SUB {interpreter.addOperator($SUB.text)} ) term)*
  ;

term
  : factor ((MULT {interpreter.addOperator($MULT.text)} | DIV {interpreter.addOperator($DIV.text)}) factor)*
  ;

factor
  : (constant |
    LEFT_PARENTHESIS {interpreter.addParenthesis()} hexp RIGHT_PARENTHESIS {interpreter.popParenthesis()} |
    ID ( |
      (DETERMINANT | TRANSPOSE | INVERSE) |
      LEFT_BRACKET mexp RIGHT_BRACKET |
      LEFT_BRACKET mexp RIGHT_BRACKET LEFT_BRACKET mexp RIGHT_BRACKET |
      LEFT_PARENTHESIS {interpreter.addParenthesis()} ( | hexp (COMMA hexp)*) RIGHT_PARENTHESIS {interpreter.popParenthesis()} ))
  ;

statute
  : (assignation | voidcall | returncall | read | write | conditional | whileloop | fromloop)*
  ;

assignation
  : ID ( | LEFT_BRACKET mexp RIGHT_BRACKET | LEFT_BRACKET mexp RIGHT_BRACKET LEFT_BRACKET mexp RIGHT_BRACKET) ASSIGN hexp SEMICOLON
  ;

voidcall
  : ID LEFT_PARENTHESIS ( | mexp (COMMA mexp)* ) RIGHT_PARENTHESIS SEMICOLON
  ;

returncall
  : RETURN LEFT_PARENTHESIS hexp RIGHT_PARENTHESIS SEMICOLON
  ;

indexvariable
  : ID ( | LEFT_BRACKET mexp RIGHT_BRACKET | LEFT_BRACKET mexp RIGHT_BRACKET LEFT_BRACKET mexp RIGHT_BRACKET)
  ;

read
  : INPUT LEFT_PARENTHESIS indexvariable (COMMA indexvariable)* RIGHT_PARENTHESIS SEMICOLON
  ;

write
  : PRINT LEFT_PARENTHESIS (hexp | CTE_STRING) (COMMA (hexp | CTE_STRING))* RIGHT_PARENTHESIS SEMICOLON
  ;

conditional
  : IF LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS THEN LEFT_CURLY statute RIGHT_CURLY (ELSE LEFT_CURLY statute RIGHT_CURLY)?
  ;

whileloop
  : WHILE LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS DO LEFT_CURLY statute RIGHT_CURLY
  ;

fromloop
  : FROM indexvariable ASSIGN mexp TO mexp DO LEFT_CURLY statute RIGHT_CURLY
  ;

mainfunc
  : MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS LEFT_CURLY statute RIGHT_CURLY
  ;
