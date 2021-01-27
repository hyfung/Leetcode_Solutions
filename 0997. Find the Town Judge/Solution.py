class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        sVoted = set()
        dVotes = dict()
        
        if trust == []:
            return 1 if N == 1 else -1
        
        for t in trust:
            sVoted.add(t[0])
            if t[1] not in dVotes:
                dVotes[t[1]] = 1
            else:
                dVotes[t[1]] += 1
        
        for i in range(1, N+1):
            try:
                if (i not in sVoted) and dVotes[i] == N-1:
                    return i
            except:
                pass
        
        return -1
