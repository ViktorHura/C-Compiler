
#include <stdio.h>

// This should print 1 and 0 alternating 
int main(){
        printf("%d; ", 1 && 2);
        printf("%d; ", 0 && 2);
        printf("%d; ", 1 || 2);
        printf("%d; ", 0 || 0);
        printf("%d; ", (0.5 || 0.0) && (0.0 || 1.0));
        printf("%d; ", !(1 && 2));
        return 0;
}
