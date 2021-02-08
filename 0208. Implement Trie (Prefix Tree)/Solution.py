class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.d
        for ch in word:
            if ch not in current:
                current[ch] = dict()

            current = current[ch]
        
        current['?'] = dict()
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        word += "?"
        current = self.d
        for ch in word:
            try:
                current = current[ch]
            except:
                return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.d
        for ch in prefix:
            try:
                current = current[ch]
            except:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
