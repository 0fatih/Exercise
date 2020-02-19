#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int login(void);
int main(void){

    if(login() == 1){
        system("/bin/sh");
    }
}

int login(void){
    int authorized = 0;
    char userInput[51];
    puts("Please enter the pass:");
    scanf("%s", userInput);
    
    if(strcmp("ff", userInput) == 0){
        authorized = 1;
    } else{
        puts("Wrong Pass!\nAccess denied!");
    }
    return authorized;
}
