#include <stdio.h>

// arirthmetic on integers
// should pinrt 3 2 18 0 1 0 23

int main() {
    int a = 3, b;
    b = a-1;
    int c = 2*a + (a+1)*(b+1);
    int d = a < b;
    int e = a > b;
    int f = a == b;
    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d\n", c);
    printf("%d\n", d);
    printf("%d\n", e);
    printf("%d\n", f);
    printf("%d\n", a+b+c);
    return 0;
}
