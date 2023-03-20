#include <stdio.h>

// Should print the number 10
int main(){
    int x = 10;
    int* xp = &x;
    printf("%d", *xp);
}
