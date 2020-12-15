class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        N = len(nums)
        total_distance = 0
        
        lut = [
            0,1,1,2,1,2,2,3,
            1,2,2,3,2,3,3,4,            
        ]
        
        for i in range(N):
            for j in range(i,N):
                
                num = nums[i] ^ nums[j]
                
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                num >>= 4
                total_distance += lut[num % 16]
                
                # total_distance += len([char for char in "{0:b}".format(nums[i] ^ nums[j]) if char == '1'])
        
        return total_distance
        
