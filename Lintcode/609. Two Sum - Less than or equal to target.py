class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        # write your code here
        length = len(nums)
        if not nums or length < 2:
            return 0

        nums.sort()
        ans = 0
        left, right = 0, length - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                ans += right - left
                left += 1
            else:
                right -= 1

        return ans
