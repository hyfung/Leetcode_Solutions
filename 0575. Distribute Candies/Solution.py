class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyCount = len(candyType)
        types = len(set(candyType))
        
        # Alice can either eats N / 2 or 2 * each type
        return min(candyCount//2, types)
        
