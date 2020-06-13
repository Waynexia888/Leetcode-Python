class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid  # return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1

##############################################################
# 用递归的方法实现二分法

# class Solution:
#     """
#     @param nums: An integer array sorted in ascending order
#     @param target: An integer
#     @return: An integer
#     """

#     def findPosition(self, nums, target):
#         # 用递归的方法实现二分法
#         return self.binarySearch(nums, 0, len(nums) - 1, target)

#     def binarySearch(self, nums, start, end, target):
#         if start > end:
#             return -1

#         mid = (start + end) // 2
#         if nums[mid] == target:
#             return mid

#         if nums[mid] < target:
#             return self.binarySearch(nums, mid + 1, end, target)

#         return self.binarySearch(nums, start, mid - 1, target)
