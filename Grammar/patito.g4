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
  : (CTE_BOOL {compiler.add_operand($CTE_BOOL.text)} {compiler.add_constant_to_type_stack_and_table("bool")} | SUB CTE_FLOAT {compiler.add_operand("-" + $CTE_FLOAT.text)} {compiler.add_constant_to_type_stack_and_table("float")} | CTE_FLOAT {compiler.add_operand($CTE_FLOAT.text)} {compiler.add_constant_to_type_stack_and_table("float")} | SUB CTE_INT {compiler.add_operand("-" + $CTE_INT.text)} {compiler.add_constant_to_type_stack_and_table("int")} | CTE_INT {compiler.add_operand($CTE_INT.text)} {compiler.add_constant_to_type_stack_and_table("int")} | CTE_CHAR {compiler.add_operand($CTE_CHAR.text)} {compiler.add_constant_to_type_stack_and_table("char")}| CTE_STRING {compiler.add_operand($CTE_STRING.text)} {compiler.add_constant_to_type_stack_and_table("string")})
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
  : sexp {compiler.top_is_logic_operator()} ((AND {compiler.add_operator($AND.text)} | OR {compiler.add_operator($OR.text)} ) mexp {compiler.top_is_logic_operator()} )*
  ;

sexp
  : exp {compiler.top_is_comparison()} ((GREATER {compiler.add_operator($GREATER.text)} |
      LESS {compiler.add_operator($LESS.text)} |
      GREATER_EQUAL {compiler.add_operator($GREATER_EQUAL.text)} |
      LESS_EQUAL {compiler.add_operator($LESS_EQUAL.text)} |
      NOT_EQUAL {compiler.add_operator($NOT_EQUAL.text)} |
      EQUAL {compiler.add_operator($EQUAL.text)} ) sexp {compiler.top_is_comparison()})?
  ;

exp
  : term {compiler.top_is_add_or_sub()} ((ADD {compiler.add_operator($ADD.text)} | SUB {compiler.add_operator($SUB.text)} ) exp {compiler.top_is_add_or_sub()})*
  ;

term
  : factor {compiler.top_is_mult_or_div()}
    ((MULT {compiler.add_operator($MULT.text)} | DIV {compiler.add_operator($DIV.text)}) term {compiler.top_is_mult_or_div()})*
  ;

factor
  : (constant |
    LEFT_PARENTHESIS {compiler.add_parenthesis()} mexp RIGHT_PARENTHESIS {compiler.pop_parenthesis()} |
    ID {compiler.add_operand_and_type($ID.text)} ( |
      (DETERMINANT {compiler.generate_matrix_operation_quad($DETERMINANT.text)} | TRANSPOSE  {compiler.generate_matrix_operation_quad($TRANSPOSE.text)} | INVERSE  {compiler.generate_matrix_operation_quad($INVERSE.text)}) |
      LEFT_BRACKET {compiler.add_parenthesis()} mexp {compiler.pop_parenthesis()} {compiler.verify_one_index()} RIGHT_BRACKET |
      LEFT_BRACKET {compiler.add_parenthesis()} mexp {compiler.pop_parenthesis()} RIGHT_BRACKET LEFT_BRACKET {compiler.add_parenthesis()} mexp {compiler.pop_parenthesis()} {compiler.verify_two_indexes()} RIGHT_BRACKET ) |
    ID {compiler.validate_function_expression($ID.text)} LEFT_PARENTHESIS {compiler.add_parenthesis()} {currentCounter=0} ( | mexp {currentCounter += 1} (COMMA mexp {currentCounter += 1})*) {compiler.validate_parameters($ID.text, currentCounter)} {compiler.add_func_operand_and_type($ID.text)} {compiler.goto_function_quad($ID.text)} RIGHT_PARENTHESIS {compiler.pop_parenthesis()})
  ;

statute
  : (assignation | funccall | returncall | read | write | conditional | whileloop | fromloop)*
  ;

assignation
  : <assoc=right> ID {compiler.add_operand_and_type($ID.text)} indexvariable? ASSIGN {compiler.add_operator($ASSIGN.text)}
    (ID {compiler.add_operand_and_type($ID.text)} indexvariable? ASSIGN {compiler.add_operator($ASSIGN.text)})*
    (mexp) SEMICOLON {compiler.generate_assign_quads()}
  ;

funccall
  : ID {compiler.validate_void_function($ID.text)} LEFT_PARENTHESIS {compiler.add_parenthesis()} {currentCounter=0} ( | mexp {currentCounter += 1} (COMMA mexp {currentCounter += 1})* ) {compiler.validate_parameters($ID.text, currentCounter)} {compiler.goto_void_function_quad($ID.text)} RIGHT_PARENTHESIS SEMICOLON
  ;

returncall
  : RETURN LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS SEMICOLON {compiler.create_return_endfunc_goto()}
  ;

indexvariable
  : (LEFT_BRACKET {compiler.add_parenthesis()} mexp {compiler.pop_parenthesis()} {compiler.verify_one_index()}  RIGHT_BRACKET | LEFT_BRACKET {compiler.add_parenthesis()} mexp {compiler.pop_parenthesis()} RIGHT_BRACKET LEFT_BRACKET {compiler.add_parenthesis()} mexp {compiler.pop_parenthesis()} {compiler.verify_two_indexes()} RIGHT_BRACKET)
  ;

read
  : INPUT LEFT_PARENTHESIS varId=ID {compiler.add_operand_and_type($varId.text)} indexvariable? {compiler.generate_read_quad()} (COMMA varId2=ID indexvariable? {compiler.add_operand_and_type($varId2.text)} {compiler.generate_read_quad()})* RIGHT_PARENTHESIS SEMICOLON
  ;

write
  : PRINT LEFT_PARENTHESIS (mexp {compiler.generate_write_quad()}) (COMMA (mexp {compiler.generate_write_quad()}))* RIGHT_PARENTHESIS SEMICOLON
  ;

conditional
  : IF LEFT_PARENTHESIS mexp RIGHT_PARENTHESIS {compiler.generate_if_quad()} THEN LEFT_CURLY statute RIGHT_CURLY (ELSE {compiler.generate_go_to_quad()} LEFT_CURLY statute RIGHT_CURLY)? {compiler.generate_end_if_quad()}
  ;

whileloop
  : WHILE LEFT_PARENTHESIS {compiler.generate_while_before_check()} mexp RIGHT_PARENTHESIS {compiler.generate_while_after_check()} DO LEFT_CURLY statute {compiler.generate_while_end()} RIGHT_CURLY
  ;

fromloop
  : FROM ID {compiler.add_from_var_operand($ID.text)} indexvariable? ASSIGN {compiler.add_operator($ASSIGN.text)} mexp {compiler.generate_assign_quads()} TO {compiler.generate_from_before_check()} mexp {compiler.generate_from_after_check()} DO LEFT_CURLY statute RIGHT_CURLY {compiler.generate_end_from_quad()}
  ;

mainfunc
  : MAIN {compiler.currentFunction=Function("main", "void", [], {})} {compiler.clear_local_memory()} LEFT_PARENTHESIS RIGHT_PARENTHESIS {compiler._add_function(compiler.currentFunction)} LEFT_CURLY {compiler.fill_goto_main_quad()} statute RIGHT_CURLY
  ;
