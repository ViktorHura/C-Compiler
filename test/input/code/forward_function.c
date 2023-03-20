#include <stdio.h>

// forward declaration to solve circular dependency
// should print 0 for i in [-9, -1] and i+1 for i in [0, 9]

int helper(int x); 

int incrementOrZero(int x) {
    if (x < 0) return 0;
    return helper(x+1) - 2;
}

int helper(int x) {
    if (x < 0) return 0;
    return incrementOrZero(x-2) + 3;
}

int main() {
    int x = -9;
    while (x<=9) {
        printf("%d: %d\n", x, incrementOrZero(x));
        x = x + 1;
    }
    return 0;
}


