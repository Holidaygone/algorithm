#include <stdio.h>

int main(){
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
    for (int k = 0; k<2; k++){
        if (a[k] == a[k+1]){
            count++;
            same = a[k];
        }
    }
    if (count == 0){
        printf("%d", a[2] * 100);
    }else if (count == 1)
    {
        printf("%d", 1000 + same * 100);
    }else if (count == 2)
    {
        printf("%d", 10000 + same * 1000);
    }
}