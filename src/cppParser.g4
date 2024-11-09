parser grammar cppParser;

options {
    tokenVocab=CppLexer;
}

// Top level compilation rules
compilationUnit
    : preprocessorDeclaration* translationUnit? EOF
    ;

preprocessorDeclaration
    : INCLUDE
    | DEFINE
    | IFDEF
    | IFNDEF
    | ENDIF
    | PRAGMA
    ;

translationUnit
    : declarationseq
    ;

declarationseq
    : (preprocessorDeclaration | declaration)+
    ;

declaration
    : blockDeclaration
    | functionDefinition
    | classDefinition
    | namespaceDefinition
    | templateDeclaration
    | operatorOverloadingDeclaration
    | friendDeclaration
    ;


// Block level declarations
blockDeclaration
    : simpleDeclaration
    | usingDeclaration
    ;

simpleDeclaration
    : declSpecifierSeq? initDeclaratorList? SEMI
    ;

declSpecifierSeq
    : declSpecifier+
    ;

declSpecifier
    : storageClassSpecifier
    | typeSpecifier
    | VIRTUAL
    | CONST
    | STATIC
    | INLINE
    | EXPLICIT
    ;

storageClassSpecifier
    : STATIC
    | TYPE_AUTO
    ;

typeSpecifier
    : simpleTypeSpecifier
    | elaboratedTypeSpecifier
    | classDefinition
    | enumDefinition
    ;

elaboratedTypeSpecifier
    : CLASS IDENTIFIER
    | STRUCT IDENTIFIER
    | ENUM IDENTIFIER
    ;

enumDefinition
    : ENUM IDENTIFIER? LBRACE enumeratorList? RBRACE
    ;

enumeratorList
    : enumerator (COMMA enumerator)*
    ;

enumerator
    : IDENTIFIER (ASSIGN constantExpression)?
    ;

simpleTypeSpecifier
    : TYPE_VOID
    | TYPE_BOOL
    | TYPE_CHAR
    | TYPE_INT
    | TYPE_FLOAT
    | TYPE_DOUBLE
    | TYPE_STRING
    | TYPE_AUTO
    | IDENTIFIER
    | smartPointerType
    ;

// Function definition
functionDefinition
    : declSpecifierSeq? declarator functionBody
    ;

functionBody
    : compoundStatement
    | SEMI  // For pure virtual functions
    ;

// Class definition
classDefinition
    : CLASS IDENTIFIER classBase? LBRACE memberSpecification* RBRACE SEMI?
    ;

classBase
    : COLON baseSpecifierList
    ;

baseSpecifierList
    : baseSpecifier (COMMA baseSpecifier)*
    ;

baseSpecifier
    : accessSpecifier? IDENTIFIER
    ;

accessSpecifier
    : PUBLIC
    | PRIVATE
    | PROTECTED
    ;

memberSpecification
    : accessSpecifier COLON
    | memberDeclaration
    | friendDeclaration
    ;

memberDeclaration
    : functionDefinition
    | simpleDeclaration
    ;

// Statements
statement
    : ioStatement
    |expressionStatement
    | compoundStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    | declarationStatement
    | tryBlock
    | labeledStatement
    ;

declarationStatement
    : blockDeclaration
    ;

labeledStatement
    : IDENTIFIER COLON statement
    | CASE constantExpression COLON statement
    | DEFAULT COLON statement
    ;

compoundStatement
    : LBRACE statementSeq? RBRACE
    ;

statementSeq
    : statement+
    ;

expressionStatement
    : expression? SEMI
    ;

selectionStatement
    : IF LPAREN condition RPAREN statement (ELSE statement)?
    | SWITCH LPAREN condition RPAREN statement
    ;

condition
    : expression
    ;

iterationStatement
    : WHILE LPAREN condition RPAREN statement
    | DO statement WHILE LPAREN expression RPAREN SEMI
    | FOR LPAREN forInitStatement condition? SEMI expression? RPAREN statement
    | FOR LPAREN forRangeDeclaration COLON forRangeInitializer RPAREN statement
    ;

forInitStatement
    : expressionStatement
    | simpleDeclaration
    ;

jumpStatement
    : BREAK SEMI
    | CONTINUE SEMI
    | RETURN expression? SEMI
    | THROW expression? SEMI
    ;

// New and Delete expressions
newExpression
    : NEW (LPAREN expressionList? RPAREN)? type (LBRACK expression RBRACK)* (LPAREN expressionList? RPAREN)?
    | NEW (LPAREN expressionList? RPAREN)? LPAREN type RPAREN (LBRACK expression RBRACK)* (LPAREN expressionList? RPAREN)?
    ;

deleteExpression
    : DELETE expression
    | DELETE LBRACK RBRACK expression
    ;

// Expressions
expression
    : assignmentExpression
    | expression COMMA assignmentExpression
    ;

assignmentExpression
    : conditionalExpression
    | logicalOrExpression assignmentOperator assignmentExpression
    ;

assignmentOperator
    : ASSIGN
    | PLUS_EQUAL
    | MINUS_EQUAL
    | STAR_EQUAL
    | DIV_EQUAL
    | MOD_EQUAL
    | BITWISE_AND_EQUAL
    | BITWISE_OR_EQUAL
    | XOR_EQUAL
    ;

conditionalExpression
    : logicalOrExpression (QUESTION expression COLON conditionalExpression)?
    ;

logicalOrExpression
    : logicalAndExpression (LOGICAL_OR logicalAndExpression)*
    ;

logicalAndExpression
    : inclusiveOrExpression (LOGICAL_AND inclusiveOrExpression)*
    ;

inclusiveOrExpression
    : exclusiveOrExpression (OR exclusiveOrExpression)*
    ;

exclusiveOrExpression
    : andExpression (XOR andExpression)*
    ;

andExpression
    : equalityExpression (AMPERSAND equalityExpression)*
    ;

equalityExpression
    : relationalExpression ((EQUAL | NOT_EQUAL) relationalExpression)*
    ;

relationalExpression
    : additiveExpression ((LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression ((STAR | DIV | MOD) unaryExpression)*
    ;

unaryExpression
    : postfixExpression
    | PLUS_PLUS unaryExpression
    | MINUS_MINUS unaryExpression
    | unaryOperator unaryExpression
    | NEW newExpression
    | DELETE deleteExpression
    ;

unaryOperator
    : PLUS
    | MINUS
    | NOT
    | AMPERSAND
    | STAR
    ;

postfixExpression
    : primaryExpression
    | postfixExpression LBRACK expression RBRACK
    | postfixExpression LPAREN expressionList? RPAREN
    | postfixExpression DOT IDENTIFIER
    | postfixExpression ARROW IDENTIFIER
    | postfixExpression PLUS_PLUS
    | postfixExpression MINUS_MINUS
    ;

primaryExpression
    : literal
    | THIS
    | LPAREN expression RPAREN
    | IDENTIFIER
    | lambdaExpression
    | smartPointerCreation
    ;

expressionList
    : assignmentExpression (COMMA assignmentExpression)*
    ;

literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | BOOL_LITERAL
    | CHAR_LITERAL
    | STRING_LITERAL
    | NULL_LITERAL
    ;

// Lambda expressions
lambdaExpression
    : LBRACK lambdaCapture? RBRACK 
      (MUTABLE | exceptionSpecification)* 
      LPAREN parameterDeclarationClause? RPAREN 
      lambdaBody
    ;

lambdaCapture
    : captureDefault
    | captureList
    | captureDefault COMMA captureList
    ;

captureDefault
    : AMPERSAND
    | ASSIGN
    ;

captureList
    : capture (COMMA capture)*
    ;

capture
    : simpleCapture
    | initCapture
    ;

simpleCapture
    : THIS
    | AMPERSAND? IDENTIFIER
    ;

initCapture
    : AMPERSAND? IDENTIFIER initializer
    ;

lambdaBody
    : compoundStatement
    | ARROW expression
    ;

// Template support
templateDeclaration
    : TEMPLATE LESS templateParameterList GREATER declaration
    ;

templateParameterList
    : templateParameter (COMMA templateParameter)*
    ;

templateParameter
    : typeParameter
    ;

typeParameter
    : TYPENAME IDENTIFIER
    ;

// Namespace support
namespaceDefinition
    : NAMESPACE IDENTIFIER LBRACE declarationseq? RBRACE
    ;

// Using declarations
usingDeclaration
    : USING IDENTIFIER SEMI
    | USING NAMESPACE IDENTIFIER SEMI
    ;

// Additional declarations
operatorOverloadingDeclaration
    : declSpecifierSeq? OPERATOR overloadableOperator parametersAndQualifiers functionBody
    | declSpecifierSeq? OPERATOR typeSpecifier parametersAndQualifiers functionBody
    ;

overloadableOperator
    : NEW | DELETE
    | PLUS | MINUS | STAR | DIV | MOD
    | AMPERSAND | OR | XOR | NOT
    | EQUAL | NOT_EQUAL
    | LESS | GREATER | LESS_EQUAL | GREATER_EQUAL
    | LBRACK RBRACK
    | LPAREN RPAREN
    | ARROW | ARROW STAR
    | PLUS_PLUS | MINUS_MINUS
    | assignmentOperator
    ;

friendDeclaration
    : FRIEND friendDeclaratorList SEMI
    ;

friendDeclaratorList
    : CLASS IDENTIFIER
    | functionDefinition
    | simpleDeclaration
    ;

// Smart pointer support
smartPointerType
    : UNIQUE_PTR LESS typeSpecifier GREATER
    | SHARED_PTR LESS typeSpecifier GREATER
    | WEAK_PTR LESS typeSpecifier GREATER
    ;

smartPointerCreation
    : MAKE_UNIQUE LESS typeSpecifier GREATER LPAREN expressionList? RPAREN
    | MAKE_SHARED LESS typeSpecifier GREATER LPAREN expressionList? RPAREN
    ;

// Range-based for loop
forRangeDeclaration
    : declSpecifierSeq declarator
    ;

forRangeInitializer
    : expression
    | bracedInitList
    ;

bracedInitList
    : LBRACE initializerList? RBRACE
    ;

// Helper rules
declarator
    : pointerDeclarator
    | noPointerDeclarator
    ;

pointerDeclarator
    : (STAR | AMPERSAND) typeQualifierSeq? pointerDeclarator
    | noPointerDeclarator
    ;

noPointerDeclarator
    : declaratorId
    | noPointerDeclarator parametersAndQualifiers
    | noPointerDeclarator LBRACK constantExpression? RBRACK
    ;

declaratorId
    : IDENTIFIER
    ;

parametersAndQualifiers
    : LPAREN parameterDeclarationClause? RPAREN cvQualifierSeq? typeQualifierSeq?
    ;

typeQualifierSeq
    : (CONST | VOLATILE)
    ;

parameterDeclarationClause
    : parameterDeclarationList
    ;

parameterDeclarationList
    : parameterDeclaration (COMMA parameterDeclaration)*
    ;

parameterDeclaration
    : declSpecifierSeq (pointerDeclarator | declarator)
    | declSpecifierSeq abstractDeclarator?
    ;

cvQualifierSeq
    : cvQualifier+
    ;

cvQualifier
    : CONST
    | VOLATILE
    ;

abstractDeclarator
    : pointerAbstractDeclarator
    ;

pointerAbstractDeclarator
    : STAR typeQualifierSeq? pointerAbstractDeclarator?
    ;

constantExpression
    : conditionalExpression
    ;

initDeclaratorList
    : initDeclarator (COMMA initDeclarator)*
    ;

initDeclarator
    : declarator initializer?
    ;

initializer
    : ASSIGN initializerClause
    ;

initializerClause
    : assignmentExpression
    | LBRACE initializerList RBRACE
    ;

initializerList
    : initializerClause (COMMA initializerClause)*
    ;

type
    : typeSpecifier pointerOperators?
    ;

pointerOperators
    : (STAR | AMPERSAND)+
    ;

// Exception handling
tryBlock
    : TRY compoundStatement handlerSeq
    ;

handlerSeq
    : handler+
    ;

handler
    : CATCH LPAREN exceptionDeclaration RPAREN compoundStatement
    ;

exceptionDeclaration
    : typeSpecifier typeSpecifier?
    | typeSpecifier IDENTIFIER
    ;

// Exception specification
exceptionSpecification
    : THROW LPAREN typeIdList? RPAREN
    | NOEXCEPT
    | NOEXCEPT LPAREN constantExpression RPAREN
    ;

typeIdList
    : typeSpecifier (COMMA typeSpecifier)*
    ;

// IO statements
ioStatement
    : outputStatement
    | inputStatement
    | getlineStatement
    ;

outputStatement
    : COUT (LEFT_SHIFT expression)+ SEMI
    ;

inputStatement
    : CIN (RIGHT_SHIFT expression)+ SEMI
    ;

getlineStatement
    : GETLINE LPAREN CIN COMMA expression RPAREN SEMI
    ;