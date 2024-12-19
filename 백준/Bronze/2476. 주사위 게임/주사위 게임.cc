#include <stdio.h>

int main(){

    int N = 0;
    int max = 0;
    scanf("%d", &N);
    for (int z = 0; z<N; z++){
        int a[3] = {0};
        int temp;
        scanf("%d %d %d", a, a + 1, a + 2);

        for (int i=0; i<3; i++){
            for (int j=0; j<2-i; j++){
                if(a[j]>a[j + 1]){
                    temp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = temp;
                }
            }
        }
        int count = 0;
        int same = 0;
        int point = 0;
        for (int k = 0; k<2; k++){
            if (a[k] == a[k+1]){
                count++;
                same = a[k];
            }
        }
        if (count == 0){
            point = a[2] * 100;
        }else if (count == 1)
        {
            point = 1000 + same * 100;
        }else if (count == 2)
        {
            point = 10000 + same * 1000;
        }  
        if (max < point){
            max = point;
        }
    }
    printf("%d", max);
}