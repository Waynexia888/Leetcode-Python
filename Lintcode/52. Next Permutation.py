class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        # 从后往前寻找第一个升序
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums

        # 从最后一个下标开始到下标i之间，找到一个比nums[i] 大的元素，将其相互交换
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

        # 最后需要将[i + 1:]区间段的数组进行升序排列即可
        result = nums[:i + 1] + sorted(nums[i + 1:])
        return result
