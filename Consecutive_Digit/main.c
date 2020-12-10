"""
Problem:
Write a function to check for 3 or more consecutive digits in an integer.
No loop, no array, recursion only

Solution:
Use the sliding window of the last 3 digits of a number
Return true if they are equal, otherwise perform recursion on N/10 where N is the number
"""


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int check_digit(int n)
{
    if(n < 100) return 0;

    if((n%1000)/100 ==  (n%100)/10 && (n%100)/10 == n%10)
    {
        return 1;
    } 

    return check_digit(n/10);
}

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
