#include <stdio.h>

// this function return the triangular number at "steps" 
// and print the numbers before it to the terminal
unsigned int triangular_iterative(unsigned int steps)
{
    unsigned int triangle = 0;

    for(int i = 0; i < steps + 1; i++)
    {
        triangle += i;
        printf("%d ", triangle);
    }
    return triangle;
}

int main()
{
    unsigned int steps = 100;
    triangular_iterative(steps);

    return 0;
}