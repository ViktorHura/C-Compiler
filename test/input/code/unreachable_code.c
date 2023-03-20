#include <stdio.h>

// test removal of unreachable code (optimizations needs to be enabled)
// should print nothing, generated code should contain no printf calls

void f(){
    int a = 10;
    return;
    printf("%d", a); // unreachable
}

int main(){
    int a = 10;
    for(int i=0; i<5; i++){
    if (1){
        continue;
        printf("%d", a); // unreachable
    }
    f();
    break;
    printf("%d", a); // unreachable
    }
    return 0;
    printf("%d", a); // unreachable
}