#include <stdio.h>
#include <string.h>

int main(){
    int T;
    scanf("%d", &T);
    for (int i = 0; i<T; i++){
        int R, n = 0;
        char S[21] = {0};
        scanf("%d %s", &R, S);
        char S2[200] = {0};
        int j = 0;
        while (S[j] != '\0')
        {
            for (int k=0; k<R; k++){
                S2[n] = S[j];
                n++;
            }
            j++;
        }
        for (int g = 0; S2[g] != '\0'; g++){
            putchar(S2[g]);
        }
        printf("\n");

    }
}