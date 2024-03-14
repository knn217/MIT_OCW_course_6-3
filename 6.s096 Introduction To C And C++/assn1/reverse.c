#include <stdio.h>
#include "reverse.h"

void reverse(char *str, int len) {
	char reversed[len+1];  // C99 allows variable length arrays to be created on the stack so this is actually legal (for C99)
	int pos = 0;
	int caret = len;
	reversed[len] = '\0';
	for (int i = len - 1; i >= -1; --i){
		if (i == -1 || str[i] == ' '){
			for (int j = i + 1; j < caret; ++j){
				reversed[pos++] = str[j];
			}
			if (i != -1) {
				reversed[pos++] = ' ';
			}
			caret = i;
		}
	}
	printf("%s\n", reversed);
}
