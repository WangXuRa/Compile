lexer grammar CPPLexer;

PLUS        : '+' ;
MINUS       : '-' ;
DIV         : '/' ;
ASSIGN      : '=' ;
LT          : '<' ;
GT          : '>' ;
LE          : '<=' ;
GE          : '>=' ;
EQ          : '==' ;
NE          : '!=' ;

AMPERSAND   : '&';
ASTERISK    : '*';

AND         : '&&' ;
OR          : '||' ;
NOT         : '!' ;
SEMICOLON   : ';' ;
COMMA       : ',' ;
DOT         : '.' ;
COLON       : ':' ;
SCOPE       : '::' ;
LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACE      : '{' ;
RBRACE      : '}' ;
LBRACK      : '[' ;
RBRACK      : ']' ;
QUESTION    : '?' ;
INCREMENT       : '++' ;
DECREMENT       : '--' ;
PLUS_ASSIGN     : '+=' ;
MINUS_ASSIGN    : '-=' ;

CLASS       : 'class' ;
PUBLIC      : 'public' ;
PRIVATE     : 'private' ;
PROTECTED   : 'protected' ;
INT         : 'int' ;
DOUBLE      : 'double' ;
CHAR        : 'char' ;
VOID        : 'void' ;
IF          : 'if' ;
ELSE        : 'else' ;
FOR         : 'for' ;
WHILE       : 'while' ;
RETURN      : 'return' ;
BOOL        : 'bool';
CONTINUE    : 'continue';
ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;
CHAR_LITERAL: '\'' ( . ) '\'';
STRING_LITERAL : '"' .*? '"' ;
BOOL_LITERAL: 'true'| 'false';

INCLUDE      : '#include';

WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip ;
