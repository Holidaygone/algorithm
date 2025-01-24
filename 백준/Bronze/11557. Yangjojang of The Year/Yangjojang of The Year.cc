#include <stdio.h>
#include <string.h> // 문자열 복사를 위한 헤더 파일

int main(){
    int T, N;
    scanf("%d", &T);

    for (int i = 0; i<T; i++){
        scanf("%d", &N);
        char school_Name[20]; // 학교 이름을 저장할 배열
        int tempScore = 0;
        for (int j = 0; j<N; j++){
            char S[20];
            int score;
            scanf("%s %d", S, &score);
            if (score > tempScore){
                tempScore = score;
                strcpy(school_Name, S); // S를 school_Name에 복사
            }else{
                continue;
            }
        }
        printf("%s\n", school_Name);
    }

    return 0;
}