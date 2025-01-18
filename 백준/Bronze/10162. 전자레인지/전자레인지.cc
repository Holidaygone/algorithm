#include <stdio.h>

int main(){
    int T = 0; // 초단위
    scanf("%d", &T);
    // A = 300 , B = 60 , C = 10
    int A = 300;
    int B = 60;
    int C = 10;
    int Acount = 0, Bcount = 0, Ccount = 0;
    if (T >= A){
        Acount = T / A;
        T = T - A * Acount;
    }
    if (T >= B)
    {
        Bcount = T / B;
        T = T - B * Bcount;
    }
    if (T >= C)
    {
        Ccount = T / C;
        T = T - C * Ccount;
    }
    if (T == 0){
        printf("%d %d %d", Acount, Bcount, Ccount);
    }else{
        printf("-1");
    }

    return 0;
}