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
CTE_FLOAT: [0-9]+ '.' [0-9]+;
CTE_INT: [0-9]+;
CTE_CHAR: [.];
CTE_STRING: '"' .*? '"';
VOID: 'void';
ID: [_A-Za-z]([_A-Za-z0-9])*;

program
  : PROGRAM ID SEMICOLON declarevars {compiler._add_function(compiler.currentFunction)} {compiler.goto_main_quad()} functions mainfunc
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
  : (CTE_BOOL {compiler.addType("bool")} | CTE_FLOAT {compiler.addType("float")} | CTE_INT {compiler.addType("int")} | CTE_CHAR {compiler.addType("char")}| CTE_STRING {compiler.addType("string")})
  ;

arrayconstant
  : LEFT_BRACKET CTE_INT RIGHT_BRACKET | LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET
  ;

functions
  : function+
  ;

function
  : FUNCTION functiontype ID {compiler.currentFunction=Function($ID.text, $functiontype.text, [], {})}  LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS declarevars? {compiler._add_function(compiler.currentFunction)} LEFT_CURLY statute? RIGHT_CURLY
  ;

functiontype
  : (INT | BOOL | FLOAT | STRING | CHAR | VOID)
  ;

parameters
  : vartypes ID {compiler.currentFunction._update_parameters($ID.text, $vartypes.text)} (COMMA vartypes ID {compiler.currentFunction._update_parameters($ID.text, $vartypes.text)})*
  ;

mexp
  : sexp {compiler.topIsLogicOperator()} ((AND {compiler.addOperator($AND.text)} | OR {compiler.addOperator($OR.text)} ) mexp {compiler.topIsLogicOperator()} )*
  ;

sexp
  : exp {compiler.topIsComparison()} ((GREATER {compiler.addOperator($GREATER.text)} |
      LESS {compiler.addOperator($LESS.text)} |
      GREATER_EQUAL {compiler.addOperator($GREATER_EQUAL.text)} |
      LESS_EQUAL {compiler.addOperator($LESS_EQUAL.text)} |
      NOT_EQUAL {compiler.addOperator($NOT_EQUAL.text)} |
      EQUAL {compiler.addOperator($EQUAL.text)} ) sexp {compiler.topIsComparison()})?
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
      LEFT_PARENTHESIS {currentCounter=0} ( | mexp {currentCounter += 1} (COMMA mexp {currentCounter += 1})*) {compiler.validate_parameters($ID.text, currentCounter)} RIGHT_PARENTHESIS))
  ;

statute
  : (assignation | voidcall | returncall | read | write | conditional | whileloop | fromloop)*
  ;

assignation
  : <assoc=right> ID {compiler.addOperandAndType($ID.text)} indexvariable? ASSIGN {compiler.addOperator($ASSIGN.text)}
    (ID {compiler.addOperandAndType($ID.text)} indexvariable? ASSIGN {compiler.addOperator($ASSIGN.text)})*
    (ID {compiler.addOperandAndType($ID.text)} | mexp) SEMICOLON {compiler.generateAssignQuads()}
  ;

voidcall
  : ID {compiler.validate_void_function($ID.text)} LEFT_PARENTHESIS ( | mexp (COMMA mexp)* ) RIGHT_PARENTHESIS SEMICOLON
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
  : PRINT LEFT_PARENTHESIS (mexp {compiler.generateWriteQuad()}) (COMMA (mexp {compiler.generateWriteQuad()}))* RIGHT_PARENTHESIS SEMICOLON
  ;

conditional
  : IF LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS {compiler.generateIfQuad()} THEN LEFT_CURLY statute RIGHT_CURLY (ELSE {compiler.generateGoToQuad()} LEFT_CURLY statute RIGHT_CURLY)? {compiler.generateEndIfQuad()}
  ;

whileloop
  : WHILE LEFT_PARENTHESIS {compiler.generateWhileBeforeCheck()} mexp RIGHT_PARENTHESIS {compiler.generateWhileAfterCheck()} DO LEFT_CURLY statute {compiler.generateWhileEnd()} RIGHT_CURLY
  ;

fromloop
  : FROM ID {compiler.addFromVarOperand($ID.text)} indexvariable? ASSIGN {compiler.addOperator($ASSIGN.text)} mexp {compiler.generateAssignQuads()} TO {compiler.generateFromBeforeCheck()} mexp {compiler.generateFromAfterCheck()} DO LEFT_CURLY statute RIGHT_CURLY {compiler.generateEndFromQuad()}
  ;

mainfunc
  : MAIN {compiler.currentFunction=Function("main", "void", [], {})} LEFT_PARENTHESIS RIGHT_PARENTHESIS {compiler._add_function(compiler.currentFunction)} LEFT_CURLY {compiler.fill_goto_main_quad()} statute RIGHT_CURLY
  ;
