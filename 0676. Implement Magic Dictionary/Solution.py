class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Simply use a list to store all words
        self.ls = list()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.ls.append(word)
        

    def search(self, searchWord: str) -> bool:
        # We only care if searchWord and word in dictionary have the same length
        candidates = [word for word in self.ls if len(word) == len(searchWord)]
        
        # A function to calculate the difference of character
        def delta(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
            return diff
        
        # Straight forward enough
        for cand in candidates:
            if delta(searchWord, cand) == 1:
                return True
        
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
