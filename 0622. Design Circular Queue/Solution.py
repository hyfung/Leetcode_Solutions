class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.element = []
        

    def enQueue(self, value: int) -> bool:
        if len(self.element) < self.k:
            self.element.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        try:
            self.element.pop(0)
            return True
        except:
            return False    
        

    def Front(self) -> int:
        try:
            return self.element[0]
        except:
            return -1
        

    def Rear(self) -> int:
        try:
            return self.element[-1]
        except:
            return -1
        

    def isEmpty(self) -> bool:
        return self.element == []
        

    def isFull(self) -> bool:
        return len(self.element) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
