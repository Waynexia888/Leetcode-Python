class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # a + b > c, 两边之和 > 第三边
        # 1， 2， 3， 4， 5， 6， 7， 8
        #     ^           ^   ^
        #     L           R   c

        # 1 + 5 <= 6,说明当两数之和< c，左指针向右移动
        # 2 + 5 > 6， 当两数之和> c, 右指针向左移动，同时记录结果（R- L种结果）
        # 2 + 5 > 6，说明 后面的数 + 5 也是大于6
        # 使用双指针算法。
        # for 循环最大边的位置 i，接下来的任务就是在 0~i-1 之间找到两数之和 > S[i]
        #时间复杂度：O(n^2) 因为for 循环O(n) ，双指针while循环O(n)

        S.sort()
        ans = 0
        for i in range(len(S)):
            left, right = 0, i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans
