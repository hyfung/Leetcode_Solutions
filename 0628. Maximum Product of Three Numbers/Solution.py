class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # N = len(nums)
        # product = -2147483648
        
        # for i in range(N):
        #     for j in range(N):
        #         for k in range(N):
        #             if i == j or j == k or k == i:
        #                 continue
        #             product = max(product, nums[i]*nums[j]*nums[k])
            
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        
