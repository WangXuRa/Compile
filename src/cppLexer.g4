lexer grammar cppLexer;

// IO Stream tokens
COUT: 'cout';
CIN: 'cin';
LEFT_SHIFT: '<<';
RIGHT_SHIFT: '>>';

// Keywords
CLASS:              'class';
PUBLIC:             'public';
PRIVATE:            'private';
PROTECTED:          'protected';
VIRTUAL:            'virtual';
OVERRIDE:           'override';
NEW:                'new';
DELETE:             'delete';
THIS:               'this';
NAMESPACE:          'namespace';
USING:              'using';
TEMPLATE:           'template';
TYPENAME:           'typename';
CONST:              'const';
STATIC:             'static';
RETURN:             'return';
IF:                 'if';
ELSE:               'else';
FOR:                'for';
WHILE:              'while';
DO:                 'do';
BREAK:              'break';
CONTINUE:           'continue';
SWITCH:             'switch';
CASE:               'case';
DEFAULT:            'default';
TRY:                'try';
CATCH:              'catch';
THROW:              'throw';
GETLINE:            'getline';

// Types
TYPE_VOID:          'void';
TYPE_BOOL:          'bool';
TYPE_CHAR:          'char';
TYPE_INT:           'int';
TYPE_FLOAT:         'float';
TYPE_DOUBLE:        'double';
TYPE_STRING:        'string';
TYPE_AUTO:          'auto';

// Operators
ASSIGN:             '=';
PLUS:               '+';
PLUS_PLUS:          '++';
PLUS_EQUAL:         '+=';
MINUS:              '-';
MINUS_MINUS:        '--';
MINUS_EQUAL:        '-=';
STAR:               '*';
STAR_EQUAL:         '*=';
DIV:                '/';
DIV_EQUAL:          '/=';
MOD:                '%';
MOD_EQUAL:          '%=';
AMPERSAND:          '&';
LOGICAL_AND:        '&&';
BITWISE_AND_EQUAL:  '&=';
OR:                 '|';
LOGICAL_OR:         '||';
BITWISE_OR_EQUAL:   '|=';
XOR:                '^';
XOR_EQUAL:          '^=';
NOT:                '!';
NOT_EQUAL:          '!=';
ARROW:              '->';
DOT:                '.';
COLON_COLON:        '::';

// Comparison
LESS:               '<';
LESS_EQUAL:         '<=';
GREATER:            '>';
GREATER_EQUAL:      '>=';
EQUAL:              '==';

// Delimiters
LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACK:             '[';
RBRACK:             ']';
SEMI:               ';';
COMMA:              ',';
COLON:              ':';
QUESTION:           '?';

// Literals
BOOL_LITERAL:       'true' | 'false';
INTEGER_LITERAL:    DECIMAL_LITERAL | HEX_LITERAL | OCT_LITERAL;
DECIMAL_LITERAL:    [0-9]+;
HEX_LITERAL:        '0' [xX] [0-9a-fA-F]+;
OCT_LITERAL:        '0' [0-7]+;
FLOAT_LITERAL:      [0-9]+ '.' [0-9]* | '.' [0-9]+;
CHAR_LITERAL:       '\'' ( ~['\\\r\n] | '\\' . ) '\'';
STRING_LITERAL:     '"' ( ~["\\\r\n] | '\\' . )* '"';
NULL_LITERAL:       'nullptr';

// Identifiers
IDENTIFIER:         [a-zA-Z_] [a-zA-Z0-9_]*;

// Comments and whitespace
BLOCK_COMMENT:      '/*' .*? '*/'     -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*     -> channel(HIDDEN);
WS:                 [ \t\r\n]+        -> skip;

// Preprocessor directives
INCLUDE:            '#include' [ \t]* ('<' ~[\r\n>]+ '>' | '"' ~[\r\n"]+ '"');
DEFINE:             '#define' [ \t]+ [a-zA-Z_] [a-zA-Z0-9_]* ~[\r\n]*;
IFDEF:              '#ifdef' [ \t]+ [a-zA-Z_] [a-zA-Z0-9_]* ~[\r\n]*;
IFNDEF:             '#ifndef' [ \t]+ [a-zA-Z_] [a-zA-Z0-9_]* ~[\r\n]*;
ENDIF:              '#endif' ~[\r\n]*;
PRAGMA:             '#pragma' ~[\r\n]*;

// extra
STRUCT:             'struct';
ENUM:               'enum';
INLINE:             'inline';
EXPLICIT:           'explicit';
NOEXCEPT:           'noexcept';
VOLATILE: 'volatile';

MUTABLE    : 'mutable';
OPERATOR   : 'operator';
FRIEND     : 'friend';
UNIQUE_PTR : 'unique_ptr';
SHARED_PTR : 'shared_ptr';
WEAK_PTR   : 'weak_ptr';
MAKE_UNIQUE: 'make_unique';
MAKE_SHARED: 'make_shared';
