class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums, s):
        # 同向双指针问题
        # 首先声明一个滑动窗口。
        # 不断调整左右边界，使的l,r区间中的值一直约束内，并更新在约束范围内的指定值。

        if not nums or len(nums) < 2:
            return -1

        left, right = 0, -1  # nums[left...right]为我们的滑动窗口
        sub_sum = 0
        min_length = len(nums) + 1

        while left < len(nums):
            if right + 1 < len(nums) and sub_sum < s:
                right += 1
                sub_sum += nums[right]
            else:
                sub_sum -= nums[left]
                left += 1

            if sub_sum >= s:
                min_length = min(min_length, right - left + 1)

        # 跳出while循环后，需要判断min_length 的值是否有变，比如：
        # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2113,1,1]  12345
        # 尽管right指针一直在变, 但是sub_sum 始终小于s
        if min_length == len(nums) + 1:
            return -1
        return min_length
