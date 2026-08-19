%{
#include <stdio.h>

int yylex(void);
void yyerror(const char *s);
%}

%token TYPE IF ELSE WHILE RELOP ID NUM

%%

program     : stmt_list
            ;

stmt_list   : stmt_list stmt
            | stmt
            ;

stmt        : decl_stmt
            | assign_stmt
            | if_stmt
            | while_stmt
            | block
            ;

block       : '{' stmt_list '}'
            ;

decl_stmt   : TYPE id_list ';'
            ;

id_list     : id_list ',' ID
            | ID
            ;

assign_stmt : ID '=' expr ';'
            ;

if_stmt     : IF '(' bool_expr ')' stmt
            | IF '(' bool_expr ')' stmt ELSE stmt
            ;

while_stmt  : WHILE '(' bool_expr ')' stmt
            ;

bool_expr   : expr RELOP expr
            ;

expr        : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | '(' expr ')'
            | ID
            | NUM
            ;

%%

void yyerror(const char *s) {
    printf("Syntax Error\n");
}

int main(void) {
    if (yyparse() == 0)
        printf("Syntactically correct\n");
    return 0;
}
