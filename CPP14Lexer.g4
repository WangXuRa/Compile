lexer grammar CPP14Lexer;

// Keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CLASS: 'class';
CONST: 'const';
CONTINUE: 'continue';
DEFAULT: 'default';
DELETE: 'delete';
DO: 'do';
ELSE: 'else';
ENUM: 'enum';
FOR: 'for';
IF: 'if';
NEW: 'new';
PRIVATE: 'private';
PROTECTED: 'protected';
PUBLIC: 'public';
RETURN: 'return';
STRUCT: 'struct';
SWITCH: 'switch';
THIS: 'this';
VOID: 'void';
WHILE: 'while';

// Operators
PLUS: '+';
MINUS: '-';
STAR: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';
PLUSPLUS: '++';
MINUSMINUS: '--';
PLUSEQ: '+=';
MINUSEQ: '-=';
STAREQ: '*=';
DIVEQ: '/=';
MODEQ: '%=';

// Comparison operators
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';

// Logical operators
AND: '&&';
OR: '||';
NOT: '!';

// Separators
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
SEMI: ';';
COMMA: ',';
DOT: '.';

// Literals
INTEGER_LITERAL
    : DECIMAL_LITERAL
    | HEX_LITERAL
    | OCT_LITERAL
    | BINARY_LITERAL
    ;

fragment DECIMAL_LITERAL: [0-9]+;
fragment HEX_LITERAL: '0' [xX] [0-9a-fA-F]+;
fragment OCT_LITERAL: '0' [0-7]+;
fragment BINARY_LITERAL: '0' [bB] [01]+;

FLOATING_LITERAL
    : FRACTIONAL_CONSTANT EXP_PART? FLOAT_SUFFIX?
    | DIGIT_SEQUENCE EXP_PART FLOAT_SUFFIX?
    ;

fragment FRACTIONAL_CONSTANT
    : DIGIT_SEQUENCE? '.' DIGIT_SEQUENCE
    | DIGIT_SEQUENCE '.'
    ;

fragment EXP_PART: [eE] [+-]? DIGIT_SEQUENCE;
fragment DIGIT_SEQUENCE: [0-9]+;
fragment FLOAT_SUFFIX: [flFL];

STRING_LITERAL: '"' (~["\\\r\n] | '\\' .)* '"';
CHAR_LITERAL: '\'' (~['\\\r\n] | '\\' .)* '\'';

// Identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Whitespace and comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip; 