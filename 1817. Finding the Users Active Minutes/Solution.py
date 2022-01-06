class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        dataStructure = dict()
        
        for log in logs:
            if log[0] not in dataStructure:
                dataStructure[log[0]] = set([log[1]])
            else:
                dataStructure[log[0]].add(log[1])
                
        print(dataStructure)
        
        UAM = [0] * k
        
        for k,v in dataStructure.items():
            UAM[len(v)-1] += 1
            
        return UAM
        
