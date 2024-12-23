#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        int r, e, c;
        scanf("%d %d %d", &r, &e, &c);
        if (e - c > r){
            printf("advertise\n");
        }else if (e - c == r)
        {
            printf("does not matter\n");
        }else{
            printf("do not advertise\n");
        }
    }
}