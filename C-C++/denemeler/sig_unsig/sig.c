#include <stdio.h>

int main(){
    unsigned int posu = 50;
    signed int negs = -50;
    unsigned int negu = -50;
    signed int poss = 50;
    printf("Positive Unsigned: %u\nNegative Signed: %d\nNegative Unsigned: %u\nPositive Signed: %d\n",posu,negs,negu,poss);
    printf("\n\n\n");
    int i=0;
    int cit=0;
    while(i<=100){
        i+=10;
        cit+=1; 
    }
    printf("%d\n\n\n",cit);
    char string[5] = "word";
    printf("%s\n",string);
}
