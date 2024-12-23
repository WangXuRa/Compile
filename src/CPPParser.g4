// Simplified C++ Grammar with Class Declarations and Comparisons for ANTLR4
parser grammar CPPParser;

options {
    superClass = cppParserBase;
    tokenVocab = CPPLexer;
}

// Parser rules
program : (includeStatement)* (classDefinition | functionDefinition | declaration | statement)* ;

classDefinition
    : CLASS ID LBRACE classBody RBRACE SEMICOLON
    ;

classBody
    : (accessSpecifier? (constructor | declaration | functionDefinition | memberDeclaration))* 
    ;

accessSpecifier
    : PUBLIC COLON
    | PRIVATE COLON
    | PROTECTED COLON
    ;

constructor: ID LPAREN parameterList? RPAREN (COLON functionCall+)? compoundStatement;

memberDeclaration
    : typeSpecifier declarator SEMICOLON
    ;

functionDefinition
    : typeSpecifier ID LPAREN parameterList? RPAREN compoundStatement
    ;

declaration
    : decl_ SEMICOLON
    | decl_assign SEMICOLON
    ;

decl_
    : typeSpecifier declarator (COMMA declarator)*
    ;

decl_assign
    : typeSpecifier declarator ASSIGN assignmentExpression (COMMA declarator ASSIGN assignmentExpression)*
    ;

typeSpecifier
    : INT
    | DOUBLE
    | CHAR
    | VOID
    | BOOL
    | (ID SCOPE)? ID
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : typeSpecifier (AMPERSAND | ASTERISK)* ID
    ;

compoundStatement
    : LBRACE (declaration | statement)* RBRACE
    ;

includeStatement
    : INCLUDE LT includeID GT
    ;

statement
    : expressionStatement
    | compoundStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    ;

expressionStatement
    : expression? SEMICOLON
    ;

selectionStatement
    : IF LPAREN expression RPAREN statement (ELSE statement)?
    ;

iterationStatement
    : WHILE LPAREN expression RPAREN statement
    | FOR LPAREN (decl_assign | assignmentExpression) SEMICOLON expressionStatement expression? RPAREN statement
    ;

jumpStatement
    : RETURN expression? SEMICOLON
    | CONTINUE SEMICOLON
    ;

expression
    : assignmentExpression
    | expression COMMA assignmentExpression
    ;

assignmentExpression
    : logicalOrExpression
    | logicalOrExpression ASSIGN assignmentExpression
    ;

logicalOrExpression
    : logicalAndExpression
    | logicalOrExpression OR logicalAndExpression
    ;

logicalAndExpression
    : equalityExpression
    | logicalAndExpression AND equalityExpression
    ;

equalityExpression
    : relationalExpression
    | equalityExpression (EQ | NE) relationalExpression
    ;

relationalExpression
    : shiftExpression
    | shiftExpression (LT | GT | LE | GE) shiftExpression
    ;

shiftExpression
    : additiveExpression (shiftOperator additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression
    | additiveExpression (PLUS | MINUS) multiplicativeExpression
    ;

multiplicativeExpression
    : unaryExpression
    | multiplicativeExpression (ASTERISK | DIV) unaryExpression
    ;

unaryExpression
    : postfixExpression
    | (INCREMENT | DECREMENT | NOT) unaryExpression
    | referenceOp unaryExpression
    ;

postfixExpression
    : primaryExpression
    | postfixExpression (INCREMENT | DECREMENT)
    ;

primaryExpression
    : variable
    | number
    | functionCall
    | CHAR_LITERAL
    | STRING_LITERAL
    | BOOL_LITERAL
    | LPAREN expression RPAREN
    ;

variable
    : (ID SCOPE)? variable_
    ;

variable_
    : ID (LBRACK expression RBRACK)?
    | ID DOT variable_
    ;

function
    : (ID SCOPE)? function_
    ;

function_
    : ID
    | ID DOT function_
    ;

functionCall
    : function LPAREN expression? RPAREN
    ;

number
    : (MINUS | PLUS)? NUMBER
    ;

declarator
    : ID
    | ID LBRACK NUMBER RBRACK
    ;

shiftOperator
    : GT GT
    | LT LT
    ;

includeID
    : ID (DOT ID)?
    ;

referenceOp
    : ASTERISK
    | AMPERSAND
    ;