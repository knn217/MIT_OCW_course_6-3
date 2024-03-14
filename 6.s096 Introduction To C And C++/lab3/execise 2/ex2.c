#include <stdio.h>
#include <string.h>

void main() {
	char str[15];
	strcpy(str, "hakuna matata!"); // this line should copy "hakuna matata!"
	                         // into our char array
	printf("%s\n", str);
	// Anything else?
    return; // array call destructor when out of scope so no need to free memory, just return
			// in short, no need to free anything since didn't alloc anything, it's a trick question
}