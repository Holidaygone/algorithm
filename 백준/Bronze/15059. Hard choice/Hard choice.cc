#include <stdio.h>

int main(){
    int Ca, Ba, Pa;
    scanf("%d %d %d", &Ca, &Ba, &Pa);
    int Cr, Br, Pr;
    scanf("%d %d %d", &Cr, &Br, &Pr);

    int result = 0;

    if (Ca < Cr){
        result += Cr - Ca;
    }
    if (Ba < Br){
        result += Br - Ba;
    }
    if (Pa < Pr){
        result += Pr - Pa;
    }
    printf("%d", result);
}