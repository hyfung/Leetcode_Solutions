# Consecutive Digit

## Question
Implement function `bool check_digit(int n)` to check for 3 or more consecutive digits in an integer.

No loop, no array, recursion only.

Assume there is no leading 0, i.e. no 0001

The function returns `TRUE` or `FALSE` according to user input `STDIN`.

## My Solution
For each level of function call, use the sliding window of the last 3 digits of a number.

Return true if they are equal, otherwise perform recursion on N/10 where N is the number.

## Sample Test Cases
* 12345 -> No
* 122223 -> Yes, 222
* 12321 -> No
* 1222333 -> Yes, 333 or 222
* 12223334 -> Yes, 333 or 222
