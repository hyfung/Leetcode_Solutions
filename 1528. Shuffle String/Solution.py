class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x = zip(s, indices)
        
        new_str = sorted(x, key=lambda x: x[1])
        
        return "".join(list(zip(*new_str))[0])
        
        
        
