class Solution:
    def reverse(self, x: int) -> int:
        if x is 0:
            return 0
        new_x = int(str(x)[::-1].strip('-').lstrip('0')) if x >= 0 else int('-' + str(x)[::-1].strip('-').lstrip('0'))
        if new_x > 2147483647 or new_x < -2147483648:
            return 0
        return new_x
