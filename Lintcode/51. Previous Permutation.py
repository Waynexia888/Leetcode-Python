class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        # 1. 从后往前找第一个降序
        # 2. 从后往前找到第一个比降序处小的元素，然后交换位置
        # 3. 从降序处到数组结尾，将其降序

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums

        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

        return nums[:i + 1] + list(reversed(nums[i + 1:]))
