%{
#include "y.tab.h"
%}

%option yylineno

DIGIT   [0-9]
LETTER  [a-zA-Z_]

%%

"//".*                              ;
"/*"([^*]|\*+[^*/])*\*+"/"          ;

"int"|"float"|"char"|"double"       { return TYPE; }
"if"                                { return IF; }
"else"                              { return ELSE; }
"while"                             { return WHILE; }
"do"                                { return DO; }
"for"                               { return FOR; }

{LETTER}({LETTER}|{DIGIT})*         { return ID; }
{DIGIT}+(\.{DIGIT}+)?               { return NUM; }

"++"                                { return INC; }
"--"                                { return DEC; }
"&&"                                { return AND; }
"||"                                { return OR; }
"=="|"!="                           { return EQOP; }
"<="|">="|"<"|">"                   { return RELOP; }
"!"                                 { return NOT; }
"="                                 { return '='; }
[+\-*/%]                            { return yytext[0]; }
[(){};,]                            { return yytext[0]; }

[ \t\r\n]                           ;
.                                   { return yytext[0]; }

%%

int yywrap(void) {
    return 1;
}
