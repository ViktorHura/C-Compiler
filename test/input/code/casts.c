#include <stdio.h>

// test explicit casts
// should print 2.0, 2.5

int main() {
	int a = 5;
	float res1 = a / 2;
	float res2 = (float) a / 2;
	printf("%f\n", res1);
	printf("%f\n", res2);
	return 0;
}
