#include <stdio.h>

// another array test
// should print 8

int main(){
	int a[4];
	a[0] = 1;
	a[1] = a[0] * 2;
	a[2] = a[1] * 2;
	a[3] = a[2] * 2;
	printf("%d\n", a[3]);
	return 0;
}
