#include <stdio.h>

int main(){
    char s[3];
    scanf("%2s", s);
    double score = 0.0;
    if (s[0] == 'A'){
        score = score + 4.0;
    }else if (s[0] == 'B')
    {
        score = score + 3.0;
    }else if (s[0] == 'C')
    {
        score = score + 2.0;
    }else if (s[0] == 'D')
    {
        score = score + 1.0;
    }
    if (s[1] == '+'){
        score = score + 0.3;
    }else if (s[1] == '-')
    {
        score = score - 0.3;
    }
    
    printf("%.1f", score);
    
}