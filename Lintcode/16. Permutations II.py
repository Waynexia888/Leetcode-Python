class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        results = []
        if nums is None:
            return [results]
        nums = sorted(nums)
        isUsed = [False] * len(nums)
        # isUsed = {i: False for i in range(len(nums))}
        self.dfs(nums, isUsed, [], results)
        return results

    def dfs(self, nums, isUsed, temp, results):
        if len(nums) == len(temp):
            results.append(list(temp))     # deep copy
            return

        for i in range(len(nums)):
            if isUsed[i] == True:
                continue

            if i != 0 and nums[i] == nums[i - 1] and isUsed[i - 1] == False:
                continue

            isUsed[i] = True
            temp.append(nums[i])
            self.dfs(nums, isUsed, temp, results)
            isUsed[i] = False
            temp.pop()
