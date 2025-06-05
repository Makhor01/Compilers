grammar ExtendedLang;

program: statement+;

statement
    : assignment ';'
    | ifStatement
    | whileStatement
    | printStatement ';'
    ;

assignment: ID '=' expression;

ifStatement: 'if' '(' expression ')' block ('else' block)?;
whileStatement: 'while' '(' expression ')' block;
block: '{' statement* '}';

printStatement: 'print' expression (',' expression)*;

expression
    : '(' expression ')'                          # parenExpr
    | expression op=('*'|'/') expression          # mulDivExpr
    | expression op=('+'|'-') expression          # addSubExpr
    | expression op=('<'|'>'|'<='|'>=') expression # compExpr
    | expression op=('=='|'!=') expression        # eqNeqExpr
    | NUMBER                                      # number
    | STRING                                      # string
    | FLOAT                                       # float
    | ID                                          # id
    | BOOL                                        # bool
    ;

op: '+' | '-' | '*' | '/' | '<' | '>' | '<=' | '>=' | '==' | '!=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;