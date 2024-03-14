#include <stdio.h>

int main(int argc, char ** argv)
{
    int i = 1;
    loop:
        if(i < argc) 
        {
            printf("%s\n", argv[i]);
            i++;
            goto loop;
        }
    return 0;
}