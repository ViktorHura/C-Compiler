#include <stdio.h>


int main(){
	int x = 5;
	if (x < 5){
		printf("Something went wrong"); // Should not print
	} else {
		printf("Hello world!\n"); // Should print
	}
	if (x == 5 && 1){
		if (x == 5){
			printf("Hello world!\n"); // Should print
		} else {
			printf("Something went wrong"); // Should not print
		}
	}
	return 0;
}
