#include <stdio.h>

// global float and rounding
// should print 8.0

float global = 3.14;

int test(int a) {
	return a + global;
}

int main() {
	printf("%f\n", test(5));
	return 0;
}
