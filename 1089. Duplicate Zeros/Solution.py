class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        N = len(arr)
        
        zero_index = [i for i,v in enumerate(arr) if v == 0][::-1]
        
        for i in zero_index:
            arr.insert(i+1, 0)
        
        for i in range(len(arr) - N):
            arr.pop()
        
        print(arr)
        
