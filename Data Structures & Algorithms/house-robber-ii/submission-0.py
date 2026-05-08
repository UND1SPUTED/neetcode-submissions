class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev, curr = 0, 0
            for num in arr:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)