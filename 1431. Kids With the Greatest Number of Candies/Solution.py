class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max_candies = max(candies)
        return [(i + extraCandies >= current_max_candies) for i in candies]
        
