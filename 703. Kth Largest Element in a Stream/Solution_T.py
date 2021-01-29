class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.dCount = dict()
        self.k = k
        
        for num in nums:
            if num not in self.dCount:
                self.dCount[num] = 1
            else:
                self.dCount[num] += 1

    def add(self, val: int) -> int:
        if val not in self.dCount:
                self.dCount[val] = 1
            else:
                self.dCount[val] += 1
        dCount.items()
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
