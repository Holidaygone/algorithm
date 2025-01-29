#include <stdio.h>

int main(){
    int a = 1, b = 1, c = 1;
    while (1){
        if (scanf("%d %d %d", &a, &b, &c) != 3) {
            break;  // 입력값이 3개가 아닐 경우 루프 종료
        }

        if (a == 0 && b == 0 && c == 0){
            break;
        }

        if (a + b <= c || a + c <= b || b + c <= a) {
            printf("Invalid\n");
        }else if (a == b && b == c)
        {
            printf("Equilateral\n");
        }else if (a == b || b == c || a == c)
        {
            printf("Isosceles\n");
        }else{
            printf("Scalene\n");
        }
    }       
    return 0;
}