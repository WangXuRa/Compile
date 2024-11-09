// Simplified C++ Grammar with Class Declarations and Comparisons for ANTLR4
parser grammar CPPParser;

options {
    superClass = cppParserBase;
    tokenVocab = CPPLexer;
}

// Parser rules
program : (classDefinition | functionDefinition | declaration | expressionStatement)* ;

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
    : typeSpecifier declarator (COMMA declarator)* SEMICOLON
    | typeSpecifier declarator ASSIGN assignmentExpression
    ;

typeSpecifier
    : INT
    | DOUBLE
    | CHAR
    | VOID
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
    | FOR LPAREN expressionStatement expressionStatement expression? RPAREN statement
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
    : additiveExpression
    | relationalExpression (LT | GT | LE | GE) additiveExpression
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
    : primaryExpression
    | (PLUS | MINUS | NOT) unaryExpression
    ;

primaryExpression
    : ID
    | NUMBER
    | CHAR_LITERAL
    | STRING_LITERAL
    | LPAREN expression RPAREN
    ;

declarator
    : ID
    | ID LBRACK expression? RBRACK
    ;
