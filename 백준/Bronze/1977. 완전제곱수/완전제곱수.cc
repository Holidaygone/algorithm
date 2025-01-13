#include <stdio.h>
#include <stdbool.h>

int main(){
    int M, N;
    scanf("%d", &M);
    scanf("%d", &N);
    int  i = 1;
    int min = 0;
    int hap = 0;
    bool minTrue = false;
    bool sqExist = false;
    while(i * i <= N){
        if (i * i < M){
            i++;
            continue;
        }else if (i * i <= N){
            sqExist = true;
            if (minTrue == false){
                min = i * i;
                minTrue = true;
            }
            hap = hap + i * i;
            i++;
        }
    }
    if (sqExist == false){
        printf("-1");
    }else{
        printf("%d\n", hap);
        printf("%d\n", min);
    }
}