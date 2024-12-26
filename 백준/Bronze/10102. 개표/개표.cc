#include <stdio.h>

int main(){
    int V;
    scanf("%d", &V);
    char vote[V+1];
    scanf("%s", vote);
    int Acount = 0;
    int Bcount = 0;
    for (int i = 0; i < V; i++){
        if (vote[i] == 'A'){
            Acount++;
        }else{
            Bcount++;
        }
        // printf("%c %d %d ", vote[i], Acount, Bcount);
    }
    if (Acount > Bcount){
        printf("A");
    }else if (Acount == Bcount)
    {
        printf("Tie");
    }else{
        printf("B");
    }
    
}