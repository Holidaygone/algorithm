#include <stdio.h>

int main(){
    int hap = 0;

    for (int i = 0; i<5; i++){
        int n = 0;
        scanf("%d", &n);
        if (n < 40){
            n = 40;
        }
        hap = hap + n;
    }
    printf("%d", hap / 5);
}