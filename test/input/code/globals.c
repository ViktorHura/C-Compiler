#include <stdio.h>

// test globals
// should print 5 3.14 10 6.28

int a = 5;
float b = 3.14;

int main(){
	printf("%d\n", a);
	printf("%f\n", b);
	float a = 6.28;
	int b = 10;
	printf("%d\n", b);
	printf("%f\n", a);
	return 0;
}