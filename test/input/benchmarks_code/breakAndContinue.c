#include <stdio.h>

int main(){
    // this should print the numbers: 0, 1, 2, 3, 4, 5
	int i = 0;
	while(i < 10){
		printf("%d\n",i);
		if (i == 5){
			break;
		} else {
			i++;
			continue;
		}
		i = 10;
	}
	return 0;
}
