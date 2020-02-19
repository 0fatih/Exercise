#include <stdio.h>

int main(void){
    int num;
    char string[21];
    
    puts("Enter a number: ");
    scanf("%d", &num);

    puts("Enter a string "
            "no longer than 20 characters: ");
    scanf("%s", string);

    printf("num is: %d\n", num);
    printf("string is: %s\n", string);

}
