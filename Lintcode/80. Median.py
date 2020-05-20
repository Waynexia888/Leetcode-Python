class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        if not nums and len(nums) == 0:
            return None

        return self.quickSelect(nums, 0, len(nums) - 1, (len(nums) + 1) // 2)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right, pivot = start, end, nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # [start, ..... right,  x, left, ........end]
        if (start + k - 1) <= right:
            return self.quickSelect(nums, start, right, k)

        if (start + k - 1) >= left:
            return self.quickSelect(nums, left, end, k - (left - start))

        return nums[right + 1]
