#include <stdio.h>

int main(){
    int K, N, M, result = 0;
    scanf("%d %d %d", &K, &N, &M);
    result = K * N - M;

    if (result >= 0){
        printf("%d\n", result);
    }else{
        printf("0\n");
    }
}