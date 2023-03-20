#include <stdio.h>

// arithmetic on characters
// should print A B C D

int main() {
    char a = 'B' - 1;
    char b;
    b = 'A' + 1;
    char c = a + ' ' + 2;
    char d = 68.0;
    printf("%c\n", a);
    printf("%c\n", b);
    printf("%c\n", c);
    printf("%c\n", d);
    return 0;
}
