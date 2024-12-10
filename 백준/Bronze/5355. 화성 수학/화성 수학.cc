#include <stdio.h>

int main(){
    int T;
    float a;
    char s1[7];
    scanf("%d", &T);
    for(int i =0; i<T; i++){
    
        scanf("%f", &a);
        getchar();
        scanf("%6[^\n]", s1);

        for (int j = 0; j<6; j++){
            if (s1[j] == '\0') // 문자열 끝이면 중단
                break;
            if (s1[j] == '@'){
                a = a * 3;
            }else if (s1[j] == '%')
            {
                a = a + 5;
            }else if (s1[j] == '#')
            {
                a = a - 7;
            }
        }
        printf("%.2f\n", a);
        
    }
}