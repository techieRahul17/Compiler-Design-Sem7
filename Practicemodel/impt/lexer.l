%option noyywrap
%{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "parser.tab.h"
%}

%%

"int" {return INT;}
"and" {return AND;}
"or" {return OR;}

"<="|">="|"=="|"!="|"<"|">" {yylval.str=strdup(yytext);return RELOP;}

[a-zA-Z_][a-zA-Z0-9_]* {yylval.str=strdup(yytext);return ID;}
[0-9]+ {yylval.str=strdup(yytext);return NUMBER;}

[=,;()+\-*/] {return yytext[0];}
[ \t\r\n]+ ;
. {printf("Invalid character");}
