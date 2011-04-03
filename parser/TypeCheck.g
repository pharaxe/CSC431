tree grammar TypeCheck;

options
{
   tokenVocab=Evil;
   ASTLabelType=CommonTree;
   backtrack=true;
}

@header
{
   import java.util.Map;
   import java.util.HashMap;
   import java.util.Vector;
   import java.util.Iterator;
}

verify
@init {
}
   : ^(PROGRAM types declarations functions)
   ;

types
@init {
}
   : ^(TYPES (types_declaration)*)
   ;

types_declaration
@init {
}
   : ^(STRUCT ID (var_decl)+)
   ;

var_decl
@init {
}
   : ^(DECL ^(TYPE type) ID)
   ;

type
@init {
}
   : INT
   | BOOL
   | ^(STRUCT ID)
   ;

declarations
@init {
}
   : ^(DECLS declaration*)
   ;

declaration
@init {
}
   : ^(DECLLIST ^(TYPE type) id_list)
   ;

id_list
@init {
}
   : ID (ID)*
   ;

functions
@init {
}
   : ^(FUNCS function*)
   ;

function
@init {
}
   : ^(FUN ID parameters ^(RETTYPE return_type) declarations statement_list)
   ;

return_type
@init {
}
   : type
   | VOID
   ;

parameters
@init {
}
   : ^(PARAMS var_decl*)
   ;

statement_list
@init {
}
   : ^(STMTS statement*)
   ;

statement
@init {
}
   : block
   | assignment
   | print
   | read
   | conditional
   | loop
   | delete
   | ret
   | invocation
   ;

block
@init {
}
   : ^(BLOCK statement_list)
   ;

assignment
@init {
}
   : ^(ASSIGN expression lvalue)
   ;

lvalue
@init {
}
   :  ID (DOT ID)*
   ;

print
@init {
}
   :  PRINT expression
   ;

read
@init {
}
   :  READ lvalue
   ;

conditional
@init {
}
   :  IF expression block (ELSE block)?
   ;

loop
@init {
}
   : ^(WHILE expression block expression)
   ;

delete
@init {
}
   : DELETE expression
   ;

ret
@init {
}
   : RETURN (expression)?
   ;

invocation
@init {
}
   : ^(INVOKE ID arguments)
   ;

// From here on out, there be dragons.
expression
   : boolterm ((AND | OR) boolterm)*
   ;

boolterm
   : simple ((EQ | LT | GT | NE | LE | GE) simple)?
   ;

simple
   : term ((PLUS | MINUS) term)*
   ;

term
   : unary ((TIMES | DIVIDE) unary)*
   ;

unary
   : selector
   | ^(NOT selector)
   | ^(NEG selector)
   ;

selector
   : factor (DOT ID)*
   ;

factor
   :  expression
   |  invocation
   |  ID
   |  INTEGER
   |  TRUE
   |  FALSE
   |  NEW ID
   |  NULL
   ;

arguments
   : ^(ARGS (expression)*)
   ;

