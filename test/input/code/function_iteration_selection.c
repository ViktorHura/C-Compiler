#include <stdio.h>

// extra construct test
// should print 2 4 6 8 10 72 98 128 162

int timesTwo(int x) {
    return x*2;
}

int main() {
    int x = 1;
    while (x < 10) {
        int result = timesTwo(x);
        if (x > 5) {
            result = result * x;
        }
        printf("%d\n", result); //show the result
        x = x + 1;
    }
    return 0;
}