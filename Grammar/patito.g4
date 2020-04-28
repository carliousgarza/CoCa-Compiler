grammar patito;

@header {
from Compiler.compiler import *
from Compiler.function import *
from Compiler.variable import *
from Compiler.quadruple import *
compiler = Compiler()
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
  : PROGRAM ID SEMICOLON declarevars {compiler._add_function(compiler.currentFunction)} functions mainfunc
  ;

declarevars
  : VAR variables+
  ;

variables
  : vartypes COLON ID arrayconstant? {compiler.currentFunction._update_vars_table($ID.text, $vartypes.text)} (COMMA ID arrayconstant? {compiler.currentFunction._update_vars_table($ID.text, $vartypes.text)})* SEMICOLON
  ;

vartypes
  : (INT | BOOL | FLOAT | STRING | CHAR)
  ;

constant
  : (CTE_BOOL {compiler.addType("bool")} | CTE_FLOAT {compiler.addType("float")} | CTE_INT {compiler.addType("int")}| CTE_CHAR {compiler.addType("char")}| CTE_STRING {compiler.addType("string")})
  ;

arrayconstant
  : LEFT_BRACKET CTE_INT RIGHT_BRACKET | LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET
  ;

functions
  : function+
  ;

function
  : FUNCTION functiontype ID {compiler.currentFunction=Function($ID.text, $functiontype.text, {}, {})} LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS declarevars? {compiler._add_function(compiler.currentFunction)} LEFT_CURLY statute? RIGHT_CURLY
  ;

functiontype
  : (INT | BOOL | FLOAT | STRING | CHAR | VOID)
  ;

parameters
  : vartypes ID {compiler.currentFunction._update_parameters($ID.text, $vartypes.text)} (COMMA vartypes ID {compiler.currentFunction._update_parameters($ID.text, $vartypes.text)})*
  ;

hexp
  : mexp {compiler.topIsAssignment()} (ASSIGN {compiler.addOperator($ASSIGN.text)} mexp {compiler.topIsAssignment()} )*
  ;

mexp
  : sexp ((AND {compiler.addOperator($AND.text)} | OR {compiler.addOperator($OR.text)} ) mexp)*
  ;

sexp
  : exp ((GREATER {compiler.addOperator($GREATER.text)} |
      LESS {compiler.addOperator($LESS.text)} |
      GREATER_EQUAL {compiler.addOperator($GREATER_EQUAL.text)} |
      LESS_EQUAL {compiler.addOperator($LESS_EQUAL.text)} |
      NOT_EQUAL {compiler.addOperator($NOT_EQUAL.text)} |
      EQUAL {compiler.addOperator($EQUAL.text)} ) sexp)?
  ;

exp
  : term {compiler.topIsAddOrSub()} ((ADD {compiler.addOperator($ADD.text)} | SUB {compiler.addOperator($SUB.text)} ) exp {compiler.topIsAddOrSub()})*
  ;

term
  : factor {compiler.topIsMultOrDiv()}
    ((MULT {compiler.addOperator($MULT.text)} | DIV {compiler.addOperator($DIV.text)}) term {compiler.topIsMultOrDiv()})*
  ;

factor
  : (constant {compiler.addOperand($constant.text)} |
    LEFT_PARENTHESIS {compiler.addParenthesis()} mexp RIGHT_PARENTHESIS {compiler.popParenthesis()} |
    ID {compiler.addOperandAndType($ID.text)} ( |
      (DETERMINANT | TRANSPOSE | INVERSE) |
      LEFT_BRACKET mexp RIGHT_BRACKET |
      LEFT_BRACKET mexp RIGHT_BRACKET LEFT_BRACKET mexp RIGHT_BRACKET |
      LEFT_PARENTHESIS {compiler.addParenthesis()} ( | mexp (COMMA mexp)*) RIGHT_PARENTHESIS {compiler.popParenthesis()} ))
  ;

statute
  : (assignation | voidcall | returncall | read | write | conditional | whileloop | fromloop)*
  ;

assignation
  : ID {compiler.addOperandAndType($ID.text)} ( | LEFT_BRACKET mexp RIGHT_BRACKET | LEFT_BRACKET mexp RIGHT_BRACKET LEFT_BRACKET mexp RIGHT_BRACKET) ASSIGN {compiler.addOperator($ASSIGN.text)} hexp SEMICOLON
  ;

voidcall
  : ID LEFT_PARENTHESIS ( | mexp (COMMA mexp)* ) RIGHT_PARENTHESIS SEMICOLON
  ;

returncall
  : RETURN LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS SEMICOLON
  ;

indexvariable
  : (LEFT_BRACKET mexp RIGHT_BRACKET | LEFT_BRACKET mexp RIGHT_BRACKET LEFT_BRACKET mexp RIGHT_BRACKET)
  ;

read
  : INPUT LEFT_PARENTHESIS var_id=ID indexvariable? {compiler.generateReadQuad($var_id.text)} (COMMA var_id2=ID indexvariable? {compiler.generateReadQuad($var_id2.text)})* RIGHT_PARENTHESIS SEMICOLON
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
  : FROM ID indexvariable? ASSIGN mexp TO mexp DO LEFT_CURLY statute RIGHT_CURLY
  ;

mainfunc
  : MAIN {compiler.currentFunction=Function("main", "void", {}, {})} LEFT_PARENTHESIS RIGHT_PARENTHESIS {compiler._add_function(compiler.currentFunction)} LEFT_CURLY statute RIGHT_CURLY
  ;
