#include <stdio.h>

int main(){

    int A, B;
    int C;

    int pA, pB;

    scanf("%d %d", &A, &B);
    scanf("%d", &C);

    pA = C / 60;
    pB = C % 60;

    if ((B + pB) >= 60){
        A++;
        B = B + pB - 60;
    }else{
        B = B + pB;
    }

    if ((A + pA) >= 24){
        A = A + pA - 24;
    }else{
        A = A + pA;
    }

    printf("%d %d", A, B);
    
}