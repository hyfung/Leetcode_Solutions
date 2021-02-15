class Solution:       
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def power(i):
            p = 0            
            tmp = i
            
            while tmp != 1:
                if tmp % 2 == 0:
                    tmp //= 2
                    p += 1
                else:
                    tmp = 3 * tmp + 1
                    p += 1
                
            return p

        ls = list(range(lo, hi+1))
        power_d = dict()
        
        for i in ls:
            power_d[i] = power(i)
        
        print(power_d)
        
        res = sorted(ls, key=lambda x: power_d[x])

        return res[k-1]
        
