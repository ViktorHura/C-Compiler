#include <stdio.h>

// test passing arguments
// should print 1 5 2 3 6 4

void test(int a) {
	printf("hello: %d\n", a);
}

int main(){
	test(1);
	int a = 5;
	printf("%d\n", a);
	test(2);
	a = 6;
	test(3);
	printf("%d\n", a);
	test(4);
	return 0;
}

