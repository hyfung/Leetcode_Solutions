class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = []
        

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()
        

    def findMedian(self) -> float:
        if len(self.stream) % 2 == 1:
            return self.stream[len(self.stream)//2]
        else:
            return (self.stream[len(self.stream)//2 - 1] + self.stream[len(self.stream)//2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
