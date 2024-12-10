#include <stdio.h>

int main(){

    int A, B, C, D;

    scanf("%d %d %d", &A, &B, &C);
    scanf("%d", &D);
    
    int pA, pB, pC;

    pA = D / 3600;
    if (pA > 0){
        D = D - 3600 * pA;
    }
    pB = D / 60;
    if (pB > 0){
        D = D - 60 * pB;
    }
    pC = D;

    if ((C + pC) >= 60){
        B++;
        C = C + pC - 60;
    }else{
        C = C + pC;
    }
    if ((B + pB) >= 60){
        A++;
        B = B + pB - 60;
    }else{
        B = B + pB;
    }
    if ((A + pA) >= 24){
        A = (A + pA) % 24;
    }else{
        A = A + pA;
    }

    printf("%d %d %d", A, B, C);

}