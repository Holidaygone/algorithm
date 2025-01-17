#include <stdio.h>
#include <stdlib.h> 

int main(){
    int n = 0;
    while (n != -1){
        scanf("%d", &n);
        if (n == -1) break;
        int ary[10000] = {0};
        int hap = 0;
        int ary_number = 0;
        for (int i = 1; i<n; i++){
            if (i == 1){
                ary[ary_number] = i;
                ary_number++;
                continue;
            }else{
                if (n % i == 0){
                    ary[ary_number] = i;
                    ary_number++;
                }
            }
        }
        int ary_count = 0;
        for (int j = 0; j < 10000; j++){
            if (ary[j] == 0){
                break;
            }else{
                ary_count++;
                hap = hap + ary[j];
            }
        }
        if (hap != n){
            printf("%d is NOT perfect.\n", n);
        }else if (hap == n)
        {
            int* ary2 = (int*)malloc(sizeof(int) * ary_count);
            for (int j = 0; j < ary_count; j++){
                ary2[j] = ary[j];
            }
            int temp; // 버블정렬
            for (int i = 1; i < ary_count; i++){
                for (int j = 0; j < ary_count - i - i; j++){
                    if (ary2[j] > ary2[j + 1]){
                        temp = ary2[j];
                        ary2[j] = ary2[j + 1];
                        ary2[j + 1] = temp;
                    }
                }
            }

            printf("%d = 1", n);
            for (int j = 1; j < ary_count; j++){
                printf(" + %d", ary2[j]);
            }
            printf("\n");

            free(ary2);
        }
    }
    return 0;
}