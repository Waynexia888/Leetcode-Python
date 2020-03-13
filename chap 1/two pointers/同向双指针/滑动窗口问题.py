# 问题描述:
# 求出一个数组每 kk 个连续整数的和的数组。如 nums = [1, 2, 3, 4], k = 2 的话，
# window sum 数组为[3, 5, 7]。
# http: // www.lintcode.com/problem/window-sum/

# 问题分析:
# 这个问题并没有什么难度，但是如果你过于暴力的用户 O(n * k) 的算法去做是并不合适的。
# 比如当前的 window 是 | 1, 2 |, 3, 4。那么当 window 从左往右移动到 1, | 2, 3|, 4 的时候，
# 整个 window 内的整数和是增加了3，减少了1。
# 因此只需要模拟整个窗口在滑动的过程中，整数一进一出的变化即可。这就是滑动窗口问题。

class Solution:
    def winSum(self, nums, k):

        n = len(nums)
        if n < k or k <= 0:


# 滑动窗口类的其他问题
# 以下两个高频的滑动窗口类问题我们在《九章算法强化班》中会讲解：

# http: // www.lintcode.com/problem/sliding-window-median/
# http: // www.lintcode.com/problem/sliding-window-maximum/

# 在 LintCode 中直接搜索 sliding window 能找到所有和 sliding window 相关的练习题。
