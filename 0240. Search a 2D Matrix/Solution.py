class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for row in matrix:
            flatten += row
        
        flatten.sort()
        return target in flatten
        
