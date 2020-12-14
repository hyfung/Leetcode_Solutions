class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        products = reduce(lambda x,y: x*y, [int(char) for char in str(n)])
        sums = sum([int(char) for char in str(n)])
        
        return products - sums
        
