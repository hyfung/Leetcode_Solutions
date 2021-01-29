OFF = 0
ON = 1
BLUE = 2

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        vStates = [0] * len(light)
        iTimes = 0
        
        for i in light:
            vStates[i-1] = ON
            # print(vStates)
            
            iOnMax = -1
            for i,v in enumerate(vStates):
                if v > 0:
                    iOnMax = i
                else:
                    break
            # print(iOnMax)
            
            for i in range(0, iOnMax + 1):
                vStates[i] = BLUE
            
            if 2 in vStates and 1 not in vStates:
                iTimes += 1
            
        return iTimes
            
