class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        ls = []
        
        for word in words:
            r1 = 0
            r2 = 0
            r3 = 0
            for char in word:
                if char in row1:
                    r1 += 1
                if char in row2:
                    r2 += 1
                if char in row3:
                    r3 +=1
            
            # In row 1, not in row 2,3
            if r1 != 0 and r2 == 0 and r3 == 0:
                ls.append(word)
            # In row 2, not in row 1,3
            if r1 == 0 and r2 != 0 and r3 == 0:
                ls.append(word)
            # In row 3, not in row 1,2
            if r1 == 0 and r2 == 0 and r3 != 0:
                ls.append(word)
        
        return ls
        
