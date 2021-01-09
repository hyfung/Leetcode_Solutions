class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return len([i for i in range(0, len(startTime)) if startTime[i] <= queryTime and endTime[i] >= queryTime])
