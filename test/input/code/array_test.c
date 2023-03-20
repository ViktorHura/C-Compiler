#include <stdio.h>

// extra array test with floats
// should print 4.5

float multiply(float x, float factor) {
    return x*factor;
}

int main() {
    float a[5];
    int i = 0;
    while (i < 5) {
        a[i] = multiply(i, 1.5);
        i = i+1;
    }
    printf("%f\n", a[3]);
    return 0;
}