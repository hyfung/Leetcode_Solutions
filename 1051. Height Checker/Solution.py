class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        counter = 0
        
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                counter += 1
        
        return counter
