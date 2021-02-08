class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = dict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        try:
            self.keys[key] += 1
        except:
            self.keys[key] = 1
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        try:
            if self.keys[key] == 1:
                del self.keys[key]
                return
            else:
                self.keys[key] -= 1
        except:
            pass

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        try:
            x = [(k,v) for k,v in self.keys.items()]
            return sorted(x, key=lambda tup: tup[1])[-1][0]
        except:
            return ""
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        try:
            x = [(k,v) for k,v in self.keys.items()]
            return sorted(x , key=lambda tup: tup[1])[0][0]
        except:
            return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
