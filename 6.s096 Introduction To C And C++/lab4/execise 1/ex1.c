#include <stdlib.h>
#include <stdio.h>

void fn()
{
    int* x = malloc(sizeof(int)); // only printing the 1st element so why have 10?
    x[0] = 0;  // didn't initialize 
    printf("%d",*x);
    free(x);   // didn't free memory
}

int main()
{
    fn();
    return 0;
}