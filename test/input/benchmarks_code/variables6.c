#include <stdio.h>

// Should print the number 10 three times

int main(){
	int x = 10;
	int* xp = &x;
	int** xpp = &xp;
	printf("%d; %d; %d", x, *xp, **xpp);
	return 0;
}
