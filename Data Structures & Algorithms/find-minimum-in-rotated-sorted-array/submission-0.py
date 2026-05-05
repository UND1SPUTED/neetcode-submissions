class Solution:
    def findMin(self, nums: List[int]) -> int:

        #initilaize pointers for binary search
        left = 0
        right = len(nums) - 1

        #loo unitl the serach is narrowed down to one element
        while left < right:
            mid = (left + right) // 2
        # if middle element is less that the irhgtmost, min is in the left
            if nums[mid] < nums[right]:
                right = mid             #include mid in the next search space
            else:
                left = mid + 1      #exclude mid, search in the right half

        return nums[left]       #when left == right, we've found the minimum
