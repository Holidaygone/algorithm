#include <stdio.h>

int main(){
    int a, b = 1;
    while (a != 0 && b != 0){
        scanf("%d %d", &a, &b);
        if (a == 0 && b == 0){
            break;
        }
        printf("%d\n", a+b);
    }
}