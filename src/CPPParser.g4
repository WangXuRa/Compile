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
    : (accessSpecifier? (declaration | functionDefinition | memberDeclaration))* 
    ;

accessSpecifier
    : PUBLIC COLON
    | PRIVATE COLON
    | PROTECTED COLON
    ;

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
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : typeSpecifier ID
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
    | multiplicativeExpression (MUL | DIV) unaryExpression
    ;

unaryExpression
    : postfixExpression
    | (INCREMENT | DECREMENT | NOT) unaryExpression
    ;

postfixExpression
    : primaryExpression
    | postfixExpression (INCREMENT | DECREMENT)
    ;

primaryExpression
    : (ID SCOPE)? ID (LBRACK expression RBRACK)*
    | number
    | functionCall
    | CHAR_LITERAL
    | STRING_LITERAL
    | BOOL_LITERAL
    | LPAREN expression RPAREN
    ;

functionCall
    : ID LPAREN expression RPAREN
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