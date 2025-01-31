#include <stdio.h>

int main(){
    int H, W, N, M; // 세로, 가로, 세로, 가로
    scanf("%d %d %d %d", &H, &W, &N, &M);
    printf("%d", ((W - 1) / (M + 1) + 1) * ((H - 1) / (N + 1) + 1));
}