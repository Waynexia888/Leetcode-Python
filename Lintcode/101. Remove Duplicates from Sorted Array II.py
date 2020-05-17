class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # 最常见的解法,特点是，读指针 right 一直匀速往前，写入指针 left 有时遇到重复的数会停一下。
        # if not nums:
        #     return 0

        # left = 0
        # count = 1
        # for right in range(1, len(nums)):
        #     if nums[right] == nums[left]:
        #         count += 1
        #     else:
        #         count = 1

        #     if count <= 2:
        #         left += 1
        #         nums[left] = nums[right]

        # return left + 1

        # 增加1个判断条件 即left前后不连续两个出现
        # if not nums:
        #     return 0

        # left, right = 1, 2
        # while right < len(nums):
        #     if nums[left] != nums[right] or nums[left] != nums[left - 1]:
        #         left += 1
        #         nums[left] = nums[right]
        #     right += 1
        # return left + 1

        # 最简练，借助于一个巧妙的观察：虽然不能和 left 比较来直接判定重复的数是否要并入（因为可允许一个重复的数），但可以和 left 前两个比。
        if not nums:
            return 0

        left = 2
        for right in range(2, len(nums)):
            if nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
        return left
