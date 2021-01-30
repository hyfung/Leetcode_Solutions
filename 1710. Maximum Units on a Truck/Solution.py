class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        boxes = [x[0] * [x[1]] for x in boxTypes]
        boxes_ = []
        for b in boxes:
            boxes_ += b
        return sum(boxes_[0:truckSize])
        
