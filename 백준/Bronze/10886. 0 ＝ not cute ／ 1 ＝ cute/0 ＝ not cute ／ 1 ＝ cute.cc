#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    int cute = 0;
    int notCute = 0;
    for (int i = 0; i < N; i++){
        int vote = 0;
        scanf("%d", &vote);
        if (vote == 1){
            cute++;
        }else{
            notCute++;
        }
    }
    if (cute > notCute){
        printf("Junhee is cute!");
    }else{
        printf("Junhee is not cute!");
    }
}