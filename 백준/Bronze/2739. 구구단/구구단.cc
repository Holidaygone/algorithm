#include <stdio.h>

int main(){
    int num1;
    scanf("%d", &num1);
    for(int i=1; i<10;i++){
        printf("%d * %d = %d", num1, i, num1 * i);
        printf("\n");
    }
}