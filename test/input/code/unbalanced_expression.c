#include <stdio.h>

// test heavily unbalanced expressions requiring recycling of registers (turn off optimisation so expression isn't folded)
// should print 55

int main(){
	int a = 1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + (1 + (2 + (3 + 4)))))))))));
	printf("%d\n", a);
	return 0;
}
