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
TRANSPOSE: '#';
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
CTE_BOOL: 'True' | 'False';
CTE_FLOAT: [0-9]+ '.' [0-9]+;
CTE_INT: [0-9]+;
CTE_CHAR: '\'' . '\'';
CTE_STRING: '"' .*? '"';
VOID: 'void';
ID: [_A-Za-z]([_A-Za-z0-9])*;

program
  : PROGRAM ID {compiler._add_function(compiler.currentFunction)} SEMICOLON declarevars {compiler.goto_main_quad()} functions? mainfunc
  ;

declarevars
  : VAR variables+
  ;

variables
  : vartypes COLON ID {compiler.update_vars_table($ID.text, $vartypes.text)} (LEFT_BRACKET CTE_INT RIGHT_BRACKET {compiler.update_array_variable($ID.text, $CTE_INT.text, $vartypes.text)}| LEFT_BRACKET first_index=CTE_INT RIGHT_BRACKET LEFT_BRACKET second_index=CTE_INT RIGHT_BRACKET {compiler.update_matrix_variable($ID.text, $first_index.text, $second_index.text, $vartypes.text)})? (COMMA ID {compiler.update_vars_table($ID.text, $vartypes.text)} (LEFT_BRACKET CTE_INT RIGHT_BRACKET {compiler.update_array_variable($ID.text, $CTE_INT.text, $vartypes.text)}| LEFT_BRACKET first_index=CTE_INT RIGHT_BRACKET LEFT_BRACKET second_index=CTE_INT RIGHT_BRACKET {compiler.update_matrix_variable($ID.text, $first_index.text, $second_index.text, $vartypes.text)})?)* SEMICOLON
  ;

vartypes
  : (INT | BOOL | FLOAT | STRING | CHAR)
  ;

constant
  : (CTE_BOOL {compiler.addOperand($CTE_BOOL.text)} {compiler.addConstantToTypeStackAndTable("bool")} | SUB CTE_FLOAT {compiler.addOperand("-" + $CTE_FLOAT.text)} {compiler.addConstantToTypeStackAndTable("float")} | CTE_FLOAT {compiler.addOperand($CTE_FLOAT.text)} {compiler.addConstantToTypeStackAndTable("float")} | SUB CTE_INT {compiler.addOperand("-" + $CTE_INT.text)} {compiler.addConstantToTypeStackAndTable("int")} | CTE_INT {compiler.addOperand($CTE_INT.text)} {compiler.addConstantToTypeStackAndTable("int")} | CTE_CHAR {compiler.addOperand($CTE_CHAR.text)} {compiler.addConstantToTypeStackAndTable("char")}| CTE_STRING {compiler.addOperand($CTE_STRING.text)} {compiler.addConstantToTypeStackAndTable("string")})
  ;

functions
  : function+
  ;

function
  : FUNCTION functiontype ID {compiler.currentFunction=Function($ID.text, $functiontype.text, [], {})} {compiler.clear_local_memory()}  LEFT_PARENTHESIS parameters? RIGHT_PARENTHESIS declarevars? {compiler._add_function(compiler.currentFunction)} LEFT_CURLY statute? RIGHT_CURLY {compiler.create_endfunc()}
  ;

functiontype
  : (INT | BOOL | FLOAT | STRING | CHAR | VOID)
  ;

parameters
  : vartypes ID {compiler.update_parameters($ID.text, $vartypes.text)} (COMMA vartypes ID {compiler.update_parameters($ID.text, $vartypes.text)})*
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
  : (constant |
    LEFT_PARENTHESIS {compiler.addParenthesis()} mexp RIGHT_PARENTHESIS {compiler.popParenthesis()} |
    ID {compiler.addOperandAndType($ID.text)} ( |
      (DETERMINANT {compiler.generate_matrix_operation_quad($DETERMINANT.text)} | TRANSPOSE  {compiler.generate_matrix_operation_quad($TRANSPOSE.text)} | INVERSE  {compiler.generate_matrix_operation_quad($INVERSE.text)}) |
      LEFT_BRACKET {compiler.addParenthesis()} mexp {compiler.popParenthesis()} {compiler.verify_one_index()} RIGHT_BRACKET |
      LEFT_BRACKET {compiler.addParenthesis()} mexp {compiler.popParenthesis()} RIGHT_BRACKET LEFT_BRACKET {compiler.addParenthesis()} mexp {compiler.popParenthesis()} {compiler.verify_two_indexes()} RIGHT_BRACKET ) |
    ID {compiler.validate_function_expression($ID.text)} LEFT_PARENTHESIS {compiler.addParenthesis()} {currentCounter=0} ( | mexp {currentCounter += 1} (COMMA mexp {currentCounter += 1})*) {compiler.validate_parameters($ID.text, currentCounter)} {compiler.add_func_operand_and_type($ID.text)} {compiler.goto_function_quad($ID.text)} RIGHT_PARENTHESIS {compiler.popParenthesis()})
  ;

statute
  : (assignation | funccall | returncall | read | write | conditional | whileloop | fromloop)*
  ;

assignation
  : <assoc=right> ID {compiler.addOperandAndType($ID.text)} indexvariable? ASSIGN {compiler.addOperator($ASSIGN.text)}  // a =
    (ID {compiler.addOperandAndType($ID.text)} indexvariable? ASSIGN {compiler.addOperator($ASSIGN.text)})*             // b = | b[1]= | b[1][2]=
    (mexp) SEMICOLON {compiler.generateAssignQuads()}                                                                   // b; | 2+1;
  ;

funccall
  : ID {compiler.validate_void_function($ID.text)} LEFT_PARENTHESIS ( | mexp (COMMA mexp)* ) RIGHT_PARENTHESIS SEMICOLON
  ;

returncall
  : RETURN LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS SEMICOLON {compiler.create_return_endfunc_goto()}
  ;

indexvariable
  : (LEFT_BRACKET {compiler.addParenthesis()} mexp {compiler.popParenthesis()} {compiler.verify_one_index()}  RIGHT_BRACKET | LEFT_BRACKET {compiler.addParenthesis()} mexp {compiler.popParenthesis()} RIGHT_BRACKET LEFT_BRACKET {compiler.addParenthesis()} mexp {compiler.popParenthesis()} {compiler.verify_two_indexes()} RIGHT_BRACKET)
  ;

read
  : INPUT LEFT_PARENTHESIS var_id=ID {compiler.addOperandAndType($var_id.text)} indexvariable? {compiler.generateReadQuad()} (COMMA var_id2=ID indexvariable? {compiler.addOperandAndType($var_id2.text)} {compiler.generateReadQuad()})* RIGHT_PARENTHESIS SEMICOLON
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
