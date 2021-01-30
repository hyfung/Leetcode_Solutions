class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        divisorCandidates = []
        answerCandidates = []
        
        for i in range(0, len(str2)):
            if set(str2.split(str2[0:i+1])) == set(['']):
                divisorCandidates.append(str2[0:i+1])
        print(divisorCandidates)
        
        for div in divisorCandidates:
            if set(str1.split(div)) == set(['']):
                answerCandidates.append(div)
        print(answerCandidates)
        
        if answerCandidates:
            return sorted(answerCandidates)[-1]
        else:
            return ""
        
