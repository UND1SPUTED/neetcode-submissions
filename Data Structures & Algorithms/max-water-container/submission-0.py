class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # initialize the two pointers
        l = 0
        r = len(heights) - 1

        # keep a track of the max area
        max_area = 0 

        #loop until the tw pointers meet
        while l < r:
            #calculate the height as the minimum of two lines
            h = heights[l] if heights[l] < heights[r] else heights[r]

            #calculate the width as the distance between the two pointers
            w = r - l

            #calcuklate the area and update max_area if its larger
            area  = h * w

            if area > max_area:
                max_area = area
            #move the pointer at the shorter line inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        # return the maximum area found
        return max_area

    