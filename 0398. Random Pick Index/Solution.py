class Solution:

    def __init__(self, nums: List[int]):
        self.d = dict()
        for i,v in enumerate(nums):
            if v not in self.d:
                self.d[v] = [i]
            else:
                self.d[v].append(i)
                
    def pick(self, target: int) -> int:
        return random.choice(self.d[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
