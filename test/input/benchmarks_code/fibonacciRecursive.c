
#include <stdio.h>

int f(int a) {
	if (a<2) {
		return a;
	}
	else {
		return f(a-1) + f(a-2);
	}
}

// Recursive fibonnaci
int main(){
	int n;
    printf("Enter a number:");
	scanf("%d",&n);
	int i = 1;
	while(i++ <= n){
		printf("fib(%d)\t= %d;\n", i, f(i));
	}
	return 0;
}
