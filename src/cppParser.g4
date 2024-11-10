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

statement
    : expressionStatement
    | compoundStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    | ioStatement
    ;

expressionStatement
    : expression? SEMICOLON
    | declarationStatement
    ;

declarationStatement
    : typeSpecifier ID (COMMA ID)* (ASSIGN expression)? SEMICOLON
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
    | arrayAccess
    ;

assignmentExpression
    : logicalOrExpression
    | logicalOrExpression ASSIGN assignmentExpression
    | logicalOrExpression INCREMENT
    | logicalOrExpression DECREMENT
    | logicalOrExpression PLUS_ASSIGN expression
    | logicalOrExpression MINUS_ASSIGN expression
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
    | INCREMENT unaryExpression
    | DECREMENT unaryExpression
    ;

primaryExpression
    : ID
    | NUMBER
    | CHAR_LITERAL
    | STRING_LITERAL
    | LPAREN expression RPAREN
    | arrayAccess
    | BOOL_LITERAL
    ;

declarator
    : ID
    | ID LBRACK expression? RBRACK
    ;

arrayAccess
: ID '[' expression ']'
;


// IO statements
ioStatement
    : outputStatement
    | inputStatement
    ;

outputStatement
    : COUT (LEFT_SHIFT expression)+ SEMICOLON
    ;

inputStatement
    : CIN (RIGHT_SHIFT expression)+ SEMICOLON
    ;
