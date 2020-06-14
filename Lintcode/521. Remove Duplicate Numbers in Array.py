# class Solution:
#     """
#     @param nums: an array of integers
#     @return: the number of unique integers
#     """

#     def deduplication(self, nums):
#         # write your code here
#         # 使用哈希表解决， 时间O(n), 空间O(n)
#         dict = {}
#         count = 0
#         for num in nums:
#             if num not in dict:
#                 dict[num] = True
#                 nums[count] = num
#                 count += 1
#         return count

#########################################################

        # 使用双指针，O(nlogn) time, O(1) extra space
        # if not nums or len(nums) == 0:
        #     return 0
        # nums.sort()

        # left, right = 0, 1
        # while right < len(nums):
        #     if nums[right] != nums[left]:
        #         left += 1
        #         nums[left] = nums[right]
        #     right += 1

        # return left + 1

##########################################################


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # 数组去重的问题是基于排好序的前提下进行的
        if nums is None or len(nums) == 0:
            return 0

        nums.sort()
        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if (j >= len(nums)):
                break
            nums[i + 1] = nums[j]
        return i + 1
