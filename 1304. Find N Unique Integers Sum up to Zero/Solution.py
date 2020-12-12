class Solution:
    def sumZero(self, n: int) -> List[int]:
        # If n is even, we can do +1 -1 +2 -2
        # If n is odd, we can do +1 -1 +2 -2 0
        
        ret_arr = []
        if n % 2 == 1:
            ret_arr.append(0)
            
        n //= 2
        for i in range(1,n+1):
            ret_arr.append(i)
            ret_arr.append(-i)
                
        return ret_arr
        
