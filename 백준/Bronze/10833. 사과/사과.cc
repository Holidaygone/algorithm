#include <stdio.h>

int main(){
    int N;
    int leftApple = 0;
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        int student, apple;
        scanf("%d %d", &student, &apple);
        int left = 0;
        left = apple % student;
        leftApple += left;
    }
    printf("%d", leftApple);
}