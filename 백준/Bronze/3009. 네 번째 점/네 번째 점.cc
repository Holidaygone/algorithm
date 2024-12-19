#include <stdio.h>

int main(){
    int a, b;
    int c, d;
    int e, f;

    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);
    scanf("%d %d", &e, &f);

    int n, m;

    if (a == c){
        n = e;
    }else if (a == e)
    {
        n = c;
    }else if (c == e)
    {
        n = a;
    }
    
    if (b == d){
        m = f;
    }else if (b == f)
    {
        m = d;
    }else if(d == f){
        m = b;
    }
    
    printf("%d %d", n, m);
}