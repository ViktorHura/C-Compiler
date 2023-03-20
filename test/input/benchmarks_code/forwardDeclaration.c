#include <stdio.h>

void f();

void g();

void f(){
	printf("Hello ");
	return;
}

void g(){
	printf("World\n");
	f();
	printf("World\n");
}

int main(){
    // Should print "hello world" twice
	f();
	g();
	return 0;
}
