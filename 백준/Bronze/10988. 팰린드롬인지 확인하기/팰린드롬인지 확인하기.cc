#include <stdio.h>

int main(){
     char word[101] = {0};
     scanf("%s", word);
     int count = 0;
     for(int i = 0; word[i] != '\0'; i++){
        count++;
     }
     // printf("%d\n", count);
     for (int i=0; i<count/2; i++){
        if (word[i] != word[count-1-i]){
            //printf("%c %c\n", word[i], word[count-1-i]);
            printf("0");
            return 0;
        }else{
            continue;
        }
     }
     printf("1");
}