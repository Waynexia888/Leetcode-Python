class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        # write your code here
        # 使用哈希表解决， 时间O(n), 空间O(n)
        # dict = {}
        # result = 0
        # for num in nums:
        #     if num not in dict:
        #         dict[num] = True
        #         nums[result] = num
        #         result += 1

        # return result

        # 使用双指针，O(nlogn) time, O(1) extra space
        if len(nums) == 0:
            return 0

        nums.sort()
        result = 1  # 慢指针，指向第二个数
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1

        return result
