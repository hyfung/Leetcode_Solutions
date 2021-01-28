class Solution:
    def reformat(self, s: str) -> str:
        aChar = []
        aDigit = []
        sRet = ""
        
        for i in s:
            if i.isdigit():
                aDigit.append(i)
            else:
                aChar.append(i)
                
        if abs(len(aChar)-len(aDigit)) > 1:
            return ""
        
        if len(aChar) == len(aDigit):
            for i in range(len(aChar)):
                sRet = sRet + aChar[i] + aDigit[i]
        
        if len(aChar) > len(aDigit):
            sRet += aChar.pop()
            for i in range(len(aChar)):
                sRet = sRet + aDigit[i] + aChar[i]
        
        if len(aChar) < len(aDigit):
            sRet += aDigit.pop()
            for i in range(len(aChar)):
                sRet = sRet + aChar[i] + aDigit[i]
        
            
        return sRet
