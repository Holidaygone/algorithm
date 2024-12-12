#include <stdio.h>

int main(){
 
    int a[3] = {0};
    int answer ,temp;
    scanf("%d %d %d", a, a+1, a+2);

    for (int i=0; i<3; i++){
        for (int j=0; j<2-i; j++){
            if(a[j]>a[j + 1]){
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    printf("%d", a[1]);    
    
}