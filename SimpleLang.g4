grammar SimpleLang;

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

printStatement: 'print' expression;

expression
    : '(' expression ')'                          # parenExpr
    | expression operator=('*'|'/') expression   # mulDivExpr
    | expression operator=('+'|'-') expression   # addSubExpr
    | expression operator=('<'|'>'|'<='|'>=') expression  # compExpr
    | expression operator=('=='|'!=') expression # eqNeqExpr
    | NUMBER                                     # number
    | ID                                         # id
    ;



op: '+' | '-' | '*' | '/' | '<' | '>' | '<=' | '>=' | '==' | '!=';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;