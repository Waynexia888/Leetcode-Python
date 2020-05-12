class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # two pointer
        # 跳过相等元素避免重复方案。
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                count, left, right = count + 1, left + 1, right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return count
