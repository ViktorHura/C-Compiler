#include <stdio.h>

// test on pointers: indirectly change variable
// should print 6

int main() {
    int a = 5;

    int* b = &a;
    *b = 6;

    int* c = b + 1;

    printf("%d\n", a);

    return 0;
}

