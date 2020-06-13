class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        # 排序 + 双指针

        if nums is None or len(nums) < 2:
            return 0

        nums.sort()

        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count
