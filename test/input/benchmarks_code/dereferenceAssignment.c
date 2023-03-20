#include <stdio.h>

// This should print: 10, 10, 11, 11
int main(){
	int x = 0;
	int* xp = &x;
	*xp = 10;
	printf("%d; ", x);
	printf("%d\n", *xp);
	(*xp)++;
	printf("%d; ", x);
	printf("%d\n", *xp);
	return 0;
}
