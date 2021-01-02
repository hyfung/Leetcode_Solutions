class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
        

    def sum(self, prefix: str) -> int:
        return sum([v for k,v in self.d.items() if k.startswith(prefix)])
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
