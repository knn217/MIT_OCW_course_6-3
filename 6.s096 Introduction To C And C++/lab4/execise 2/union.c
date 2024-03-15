#include <stdio.h>

union integer
{
    int intgr;
    char bytes[4];
};

int main()
{
    union integer i1;
    i1.intgr = 255;
    printf("%d, %d, %d, %d", i1.bytes[3], i1.bytes[2], i1.bytes[1], i1.bytes[0]);
    return 0;
}