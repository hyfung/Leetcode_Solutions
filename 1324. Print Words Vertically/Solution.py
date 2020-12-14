class Solution:
    def printVertically(self, s: str) -> List[str]:
        # Tokenize        
        words = s.split(' ')
        
        # Obtain longest word
        longest = max([len(word) for word in words])
        res = longest * ['']
        
        # Rightpad with whitespaces
        words = [word + ' ' * (longest - len(word)) for word in words]

        for i in range(longest):
            res[i] = "".join([chars[i] for chars in words])
            
        res = [ele.rstrip(' ') for ele in res]
        
        return res
        
