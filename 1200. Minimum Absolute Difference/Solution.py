class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # First sort the array
        arr.sort()
        
        min_diff = 2147483647
        keys = []
        
        for i in range(0, len(arr)-1):
            min_diff = min(min_diff, arr[i+1]-arr[i])
        
        for i in range(0, len(arr)-1):
            if arr[i+1]-arr[i] == min_diff:
                keys.append([arr[i], arr[i+1]])
        
        return keys
