class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31]
        
        counter = 0
        for i in range(L,R+1):
            if len([bit for bit in "{0:b}".format(i) if bit == '1']) in primes:
                counter += 1
        return counter
        
