class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # not nums 可能是 nums = None 也可能是 nums = [].
        result = []
        if nums is None:
            return result
        nums = sorted(nums)
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, startIndex, temp, result):
        result.append(list(temp))   # deep copy

        for i in range(startIndex, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, result)

            temp.pop()
