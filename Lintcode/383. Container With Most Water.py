class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """

    def maxArea(self, heights):
        # 使用相向双指针，然后每次记录capacity的值， 使之最大
        left, right = 0, len(heights) - 1
        capacity = 0

        while left < right:
            result = min(heights[left], heights[right]) * (right - left)
            if result > capacity:
                capacity = result

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return capacity
