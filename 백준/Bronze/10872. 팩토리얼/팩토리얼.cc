#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    long long result = 1;
    for (int i = N; i > 0; i--){
        result = result * i;
    }
    printf("%lld", result);
}