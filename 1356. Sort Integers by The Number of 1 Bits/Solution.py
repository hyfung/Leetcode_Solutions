class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        arr.sort()
        
        def bits(v):
            return len([char for char in "{0:b}".format(v) if char == '1'])
        
        return sorted(arr, key = bits)
        
