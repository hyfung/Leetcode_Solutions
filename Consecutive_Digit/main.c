/*
Problem:
Write a function to check for 3 or more consecutive digits in an integer.
No loop, no array, recursion only
Assume there is no leading 0

Solution:
Use the sliding window of the last 3 digits of a number
Return true if they are equal, otherwise perform recursion on N/10 where N is the number

Sample Test Cases:
12345 -> No
122223 -> Yes
12321 -> No
1222333 -> Yes
12223334 -> Yes
*/


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "check_digit.h"


int main(int argc, char const *argv[])
{
    int i = 0;
    while(1)
    {
        scanf("%d", &i);
        printf("%s\n", check_digit(i)? "YES":"NO");
    }
    return 0;
}
