#include <stdio.h>

void amazeWOW() {  // iterative
	int i;
	printf("amazeWOW:\t");
	for (i = 0; i <= 10; i++) {
		if (i % 2 == 1) {
			printf("%d ", i);
		}
	}
	printf("\n");
}

void amaze1(int max) // recursive
{
    if(max >= 10) printf("\n");
    else
    {
        printf("%d ", (max + (max%2 + 1)));
        amaze1(max+2);
    }
}

void amaze2()  // cheat
{
    printf("1 3 5 7 9");
    printf("\n");
}

void amaze3()  // iterate array 
{
    int arr[5] = {1,3,5,7,9};
    for(int i = 0; i < 5; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void amaze4() // switch case
{
    for(int i = 0; i<10; i++)
    {
        switch(i%2)
        {
        case 0: break;
        case 1: printf("%d ", i); break;
        }
    }
    printf("\n");
}

int main()
{
    amazeWOW();
    amaze1(0);
    amaze2();
    amaze3();
    amaze4();
    return 0;
}