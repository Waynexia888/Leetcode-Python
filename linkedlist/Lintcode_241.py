# Lintcode 241: 转换字符串到整数（容易版）  · string to integer

# 题目描述: Given a string, convert it to an integer. You may assume the 
# string is a valid integer number that can be presented by a 
# signed 32bit integer (-2^31 ~ 2^31-1).
# 给一个字符串, 转换为整数. 你可以假设这个字符串是一个有效的整数的字符串形式， 
# 且范围在32位整数之间 (-231 ~ 231 - 1)。


class Solution:
    # @param {string} str a string
    # @return {int} an integer
    def stringToInteger(self, str):
        # Write your code here
        # 考虑是正是负, 如果是正的，转换的起始位置是0； 如果是负的，转换的起始位置是1；
        # 字符串：S_1S_2S_3S_4 -> 数字：((S_1*10+S_2)*10+S_3)*10+S_4
        # -123        123
        # num = 0     0 * 10 + 1 = 1
        # num = 1     1 * 10 + 2 = 12
        # num = 12   12 * 10 + 3 = 123

        signed = 1
        start = 0
        if str[0] == '-':
            signed = -1
            start = 1

        num = 0
        for idx in range(start, len(str)):
            num = num * 10 + int(str[idx]) # + ord(str[idx]) - ord('0')

        return num * signed

        # 优化后的代码：
        signed = 1

        if str[0] = '-':
            signed = -1
            str = str[1:]

        num = 0
        for c in str:
            num = num * 10 + int(c)  # + ord(c) - ord('0')

        return num * signed


        

