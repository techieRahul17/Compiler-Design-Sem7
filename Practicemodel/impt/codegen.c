#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main(){
    char line[250];
    char dest[50],left[50],right[50],op[10];
    int label;
    while(fgets(line,sizeof(line),stdin)){
        if(sscanf(line,"if %49s %9s %49s goto L%d",left,op,right,&label)==4){
            printf("CMP %s , %s\n",left,right);
            if(!strcmp(op,"<=")) printf("JLE L%d\n",label);
            else if(!strcmp(op,">=")) printf("JGE L%d\n",label);
            else if(!strcmp(op,"==")) printf("JE L%d\n",label);
            else if(!strcmp(op,"!=")) printf("JNE L%d\n",label);
            else if(!strcmp(op,"<")) printf("JLT L%d\n",label);
            else if(!strcmp(op,">")) printf("JGT L%d\n",label);
            else printf("Invalid condition");
            continue;
        }
        if(sscanf(line,"goto L%d",&label)==1){
            printf("JMP L%d\n",label);
            continue;
        }
        if(sscanf(line,"L%d:",&label)==1){
            printf("L%d\n",label);
            continue;
        }
        if(sscanf(line,"%49s = %49s %9s %49s",dest,left,op,right)==4){
            printf("MOV R0 , %s\n",left);
            if(!strcmp(op,"+")) printf("ADD R0 , %s\n",right);
            else if(!strcmp(op,"-")) printf("SUB R0 , %s\n",right);
            else if(!strcmp(op,"*")) printf("MUL R0 , %s\n",right);
            else if(!strcmp(op,"/")) printf("DIV R0 , %s\n",right);
            else if(!strcmp(op,"and")) printf("AND R0 , %s\n",right);
            else if(!strcmp(op,"or")) printf("OR R0 , %s\n",right);
            else if(!strcmp(op,"<<")) printf("SHL R0 , %s\n",right);
            else {
                printf("Invalid condition");
                continue;
            }
            printf("MOV %s , R0\n",dest);
            continue;
        }
        if(sscanf(line,"%49s = %49s",dest,left)==2){
            printf("MOV %s , %s\n",dest,left);
            continue;
        }
        if(line[0]!='\0' || line[0]!='\n'){
            printf("Invalid TAC");
        }

    }
    return 0;
}