#include <stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    for (int i = 0; i<T; i++){
        int A, B, N = 0;
        scanf("%d %d", &A, &B);
        if (A==B){
            printf("%d\n", A);
        }else if (A>B)
        {   
            N = A;
            if (B==1){
                printf("%d\n", A);
            }else
            {
                while(N % B != 0){
                    N = N + A;
                }
                printf("%d\n", N);
            }
        }else if (A<B){
            N = B;
            if (A==1){
                printf("%d\n", B);
            }else{
                while(N % A != 0){
                N = N + B;
                }
                printf("%d\n", N);
            }
        }
    }
}