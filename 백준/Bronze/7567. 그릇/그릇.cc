#include <stdio.h>

int main() {
    char dish[51] = {0};
    int height = 0;
    scanf("%s", dish);
    for (int i=0; i<50; i++){
        if (dish[i] == 0){
            break;
        }
        if (dish[i] == dish[i+1]){
            height += 5;
        }else{
            height += 10;
        }
    }
    printf("%d", height);
}