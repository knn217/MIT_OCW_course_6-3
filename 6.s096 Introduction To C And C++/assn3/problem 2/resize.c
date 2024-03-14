#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(){
	//Allows you to generate random number
	srand(time(NULL));

	// Allows user to specify the original array size, stored in variable n1.
	printf("Enter original array size:");
	int n1=0;
	scanf("%d",&n1);

	//Create a new array of n1 ints
	int* a1 = malloc(sizeof(int) * n1);/* Fill in*/
	int i;
	for(i=0; i<n1; i++){
		//Set each value in a1 to 100
		a1[i] = 100;
		
		//Print each element out (to make sure things look right)
		printf("%d ", a1[i]);
	}

	//User specifies the new array size, stored in variable n2.
	printf("\nEnter new array size: ");
	int n2=0;
	scanf("%d",&n2);

	//Dynamically change the array to size n2
	a1 = realloc(a1 , sizeof(int) * n2);/* Fill in*/
    // realloc auto free the memory at the old adress (old a1) if needed
	//If the new array is a larger size, set all new members to 0. Reason: dont want to use uninitialized variables.

	for (; n1 < n2; n1++)
    {
        a1[n1] = 0;
    }
	

	for(i=0; i<n2;i++){
		//Print each element out (to make sure things look right)
		printf("%d ", a1[i]);
	}
	printf("\n");
	
	//Done with array now, done with program :D
	free(a1); // nice try

	return 0;
}