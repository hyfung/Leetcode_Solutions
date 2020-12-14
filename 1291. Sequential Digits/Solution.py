class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        cand = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 2, 23, 234, 2345, 23456, 234567, 2345678, 23456789, 3, 34, 345, 3456, 34567, 345678, 3456789, 4, 45, 456, 4567, 45678, 456789, 5, 56, 567, 5678, 56789, 6, 67, 678, 6789, 7, 78, 789, 8, 89, 9]
        # base = '123456789'
        # cand = []
        # for i in range(9):
        #     for j in range(1,10):
        #         if j >= i:
        #             try:
        #                 cand.append(int(base[i:j]))
        #             except:
        #                 continue
        return sorted([x for x in cand if x in range(low, high+1)])
