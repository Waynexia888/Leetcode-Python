class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # 因为是有序的数组， sorted, 考虑用两根指针， 背向而行
        # 时间复杂度O(n); 空间复杂O(1)

        left, right = 0, len(nums) - 1
        while left < right:  # 因为返回的是两个不想等索引，所以此处不是<=
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return []  # 如果没找到， 返回一个空数组
