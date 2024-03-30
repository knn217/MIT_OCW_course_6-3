#include <stdio.h>

union float_bits 
{
    float f;
    unsigned int bits;
};

// print_hex( 5.Of ) outputs "The float looks like Ox4OaOOOOO in hex."
void print_hex( float f) 
{
    union float_bits t;
    t.f = f;
    printf( "The float looks like Ox%x in hex.\n", t.bits );
}

int main()
{
    printf( "Hi!\n");
   return 0;
}
