#include <stdio.h>


int main(){
	int x = 5;
	if (x < 5){
		printf("Something went wrong"); // Should not print
	}
	if (x >= 5){
		printf("Hello world!\n"); // Should print
	}
	if (x == 5 && 1){
		if (x != 4){
			printf("Hello world!\n"); // Should print
		}
	}
	return 0;
}
