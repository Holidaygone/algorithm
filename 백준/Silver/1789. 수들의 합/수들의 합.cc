#include <stdio.h>

int main(){
    unsigned long long S;
    scanf("%llu", &S);

    unsigned long long N = 0;
    unsigned long long sum = 0;

    while (sum + (N + 1) <= S){
        N++;
        sum += N;
    }
    printf("%llu", N);
    return 0;
}