#include<stdio.h>
// single line comment
/* multi
   line comment */
int main()
{
    int x = 0x1F, count = 5;
    float pi = 3.14;
    char ch = 'A';
    x += 2;
    count++;
    if (x <= 10 && count != 0) {
        printf("ok\n");
    }
    while (x > 0) {
        x--;
    }
    return 0;
}