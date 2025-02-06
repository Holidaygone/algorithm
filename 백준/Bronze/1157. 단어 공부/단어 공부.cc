#include <stdio.h>
#include <ctype.h> // toupper() 사용하기 위함

int main(){
    char word[1000000];
    scanf("%s", word);

    for(int i = 0; word[i] != '\0'; i++){
        word[i] = toupper(word[i]);
    }
    int count[26] = {0};

    for (int i = 0; word[i] != '\0'; i++){
        count[word[i] - 'A']++; // 'A'를 기준으로 인덱스 계산
    }
    
    int max_count = 0;
    char max_char = '?';

    for (int i = 0; i < 26; i++){
        if (count[i] > max_count){
            max_count = count[i];
            max_char = 'A' + i;
        } else if (count[i] == max_count)
        {
            max_char = '?';
        }
    }
    printf("%c\n", max_char);
    return 0;
}