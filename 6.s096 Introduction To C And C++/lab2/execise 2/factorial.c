#include <stdio.h>

int factorial (int n) {
	int i = 1;
	while (n > 1) {
		i = i * n;
		// int n = n - 1;
        // redefinition of n in a scope
        // this new "n" will be deleted at the end of each loop when the program go out of scope 
        n = n - 1;
	}
	return i;
}

int main (int argc, char *argv[]) {
	int fac4 = factorial(4);
	int fac5 = factorial(5);
	printf("4! = %d, 5! = %d\n", fac4, fac5);
	return 0;
}