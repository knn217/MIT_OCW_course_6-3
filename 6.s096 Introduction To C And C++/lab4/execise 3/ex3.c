#include <stdio.h>

struct X
{
    short s; 
    int i; 
    char c;
};

struct Y
{
    int i;
    char c;
    short s;
};

struct Z
{
    int   i;
    short s;
    char  c;
};

int main()
{
    printf("size of X: %zu \nsize of Y: %zu \nsize of Z: %zu", sizeof(struct X), sizeof(struct Y), sizeof(struct Z));
    return 0;
}