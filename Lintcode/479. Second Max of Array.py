class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """

    def secondMax(self, nums):
        # write your code here
        maxValue = max(nums[0], nums[1])
        secondValue = min(nums[0], nums[1])

        for i in range(2, len(nums)):
            if maxValue < nums[i]:
                secondValue = maxValue
                maxValue = nums[i]
            elif secondValue < nums[i]:
                secondValue = nums[i]
        return secondValue
