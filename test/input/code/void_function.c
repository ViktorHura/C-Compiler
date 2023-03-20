#include <stdio.h>

// void function test
// should print hello 5 hello hello 6 hello

void test() {
	printf("hello\n");
}

int main(){
	test();
	int a = 5;
	printf("%d\n", a);
	test();
	a = 6;
	test();
	printf("%d\n", a);
	test();
	return 0;
}
