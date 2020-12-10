#include "check_digit.h"

int check_digit(int n)
{
    if(n < 100) return 0;

    if((n%1000)/100 ==  (n%100)/10 && (n%100)/10 == n%10)
    {
        return 1;
    } 

    return check_digit(n/10);
}
