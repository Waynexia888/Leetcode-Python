class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """

    def stringCount(self, str):
        # 使用同向双指针解决
        # 找到第一个为‘0’的数，以此开始，查看有多少个连续的‘0’， 直到找到非‘0’的数，以此结束
        # 时间复杂度 O(n), 空间复杂度O(1)

        if not str:
            return 0

        j, ans = 1, 0
        for i in range(len(str)):
            if str[i] != '0':
                continue
            j = max(j, i + 1)
            while j < len(str) and str[j] == '0':
                j += 1

            ans += j - i

        return ans
