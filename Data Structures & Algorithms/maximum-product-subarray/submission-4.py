class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = max_prod = nums[0]

        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)

            max_prod = max(max_prod, cur_max)
        return max_prod



