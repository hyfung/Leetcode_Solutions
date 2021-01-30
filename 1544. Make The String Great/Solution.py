class Solution:
    def makeGood(self, s: str) -> str:
        l = 'abcdefghijklmnopqrstuvwxyz'
        cand = []
        
        for ch in l:
            cand.append(ch+ch.upper())
            cand.append(ch.upper()+ch)

        print(cand)
            
        def check(st, cand):
            for i in cand:
                if i in st:
                    return True
            return False
        
        while True:
            for i in cand:
                s = s.replace(i, '')
            if not check(s, cand):
                return s
                
        # print(s)
            
