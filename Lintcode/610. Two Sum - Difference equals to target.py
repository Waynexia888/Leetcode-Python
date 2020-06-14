# class Solution:
#     """
#     @param nums: an array of Integer
#     @param target: an integer
#     @return: [num1, num2] (num1 < num2)
#     """

#     def twoSum7(self, nums, target):
#         # 二分法解法, 时间复杂度O(nlogn), 空间复杂度O(1)

#         if nums is None or len(nums) < 2:
#             return [-1, -1]

#         target = abs(target)
#         for i in range(len(nums)):
#             j = self.binarySearch(nums, i + 1, len(nums) - 1, target + nums[i])
#             if j != -1:
#                 return [nums[i], nums[j]]
#         return [-1, -1]

#     def binarySearch(self, nums, start, end, target):

#         while start + 1 < end:
#             mid = (start + end) // 2
#             if nums[mid] == target:
#                 return mid

#             if nums[mid] < target:
#                 start = mid
#             else:
#                 end = mid

#         if nums[start] == target:
#             return start
#         if nums[end] == target:
#             return end

#         return -1

####################################################


class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """

    def twoSum7(self, nums, target):
        # 同向双指针的模版

        if nums is None or len(nums) < 2:
            return [-1, -1]

        target = abs(target)
        j = 1
        for i in range(len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and nums[j] - nums[i] < target:
                j += 1
            if j >= len(nums):
                break

            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
        return [-1, -1]
