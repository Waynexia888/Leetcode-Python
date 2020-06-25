class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        result = []
        if nums is None:
            return [result]

        self.dfs(nums, set(), [], result)
        return result

    def dfs(self, nums, isUsed, temp, result):
        if len(nums) == len(temp):
            result.append(list(temp))     # deep copy
            return

        for num in nums:
            if num in isUsed:
                continue

            temp.append(num)
            isUsed.add(num)
            self.dfs(nums, isUsed, temp, result)
            temp.pop()
            isUsed.remove(num)
