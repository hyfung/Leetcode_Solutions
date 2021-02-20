class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Allocate what we need
        d = dict() # Used to keep counting
        to_be_deleted = [] # Store the index of member to be popped
        old_length = len(nums) # Original length of the array
        
        for i, v in enumerate(nums):
            try:
                d[v] += 1
            except:
                d[v] = 1
            
            if d[v] > 2:
                to_be_deleted.append(i)
                
        iRet = old_length - len(to_be_deleted)
        
        for i in to_be_deleted[::-1]:
            nums.pop(i)
        
        return iRet
        
