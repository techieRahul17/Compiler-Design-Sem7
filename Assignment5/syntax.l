%{
#include "y.tab.h"
%}

DIGIT   [0-9]
LETTER  [a-zA-Z_]

%%

"int"|"float"|"char"|"double"      { return TYPE; }
"if"                                { return IF; }
"else"                              { return ELSE; }
"while"                             { return WHILE; }
"=="|"!="|"<="|">="|"<"|">"         { return RELOP; }
"="                                 { return '='; }
{LETTER}({LETTER}|{DIGIT})*         { return ID; }
{DIGIT}+(\.{DIGIT}+)?                { return NUM; }
[+\-*/]                             { return yytext[0]; }
[(){};,]                            { return yytext[0]; }
[ \t\n]                             ;
.                                   ;

%%

int yywrap(void) {
    return 1;
}
