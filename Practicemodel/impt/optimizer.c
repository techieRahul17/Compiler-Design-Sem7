#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int isnum(char *s){
    if(*s=='-' && *(s+1))s++;
    if(!*s)return 0;
    while(*s){
        if(!isdigit((unsigned char)*s++))return 0;
    } 
    return 1;
}

void optimize(char *line){
    char dest[50],left[50],right[50],op[10];
    int result,a,b;
    if(strstr(line,"goto") || strstr(line,"if ") || line[0] == 'L'){
        puts(line);
        return;
    }
    if(sscanf(line,"%49s = %49s %9s %49s",dest,left,op,right)!=4){
        puts(line);
        return;
    }
    if(isnum(left) && isnum(right)){
        a=atoi(left);
        b=atoi(right);
        if(!strcmp(op,"+"))result=a+b;
        else if(!strcmp(op,"-"))result=a-b;
        else if(!strcmp(op,"*"))result=a*b;
        else if(!strcmp(op,"/") && b!=0 && a%b==0)result=a/b;
        else{
            puts(line);
            return;
        }
        printf("%s = %d\n",dest,result);
    }
    else if(!strcmp(op,"+") && !strcmp(right,"0")) printf("%s = %s\n",dest,left);
    else if(!strcmp(op,"+") && !strcmp(left,"0")) printf("%s = %s\n",dest,right);
    else if(!strcmp(op,"-") && !strcmp(right,"0")) printf("%s = %s\n",dest,left);
    else if(!strcmp(op,"*") && !strcmp(right,"1")) printf("%s = %s\n",dest,left);
    else if(!strcmp(op,"*") && !strcmp(left,"1")) printf("%s = %s\n",dest,right);
    else if(!strcmp(op,"*") && !strcmp(right,"0")) printf("%s = 0\n",dest);
    else if(!strcmp(op,"*") && !strcmp(left,"0")) printf("%s = 0\n",dest);
    else if(!strcmp(op,"/") && !strcmp(right,"1")) printf("%s = %s\n",dest,left);

    else if(!strcmp(op,"*") && !strcmp(right,"2")) printf("%s = %s + %s\n",dest,left,left);
    else if(!strcmp(op,"*") && !strcmp(right,"4")) printf("%s = %s << 2\n",dest,left);
    else if(!strcmp(op,"*") && !strcmp(right,"8")) printf("%s = %s << 3\n",dest,left);

    else puts(line);
}

int main(){
    char line[250];
    while(fgets(line,sizeof(line),stdin)){
        line[strcspn(line,"\n")]='\0';
        if(!strcmp(line,"END"))break;
        if(*line)optimize(line);
    }
    return 0;
}