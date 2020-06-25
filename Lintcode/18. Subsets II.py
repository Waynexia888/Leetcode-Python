class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results
        nums = sorted(nums)
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, startIndex, temp, results):
        results.append(list(temp))

        for i in range(startIndex, len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i > startIndex:
                continue

            temp.append(nums[i])
            self.dfs(nums, i + 1, temp, results)
            temp.pop()
