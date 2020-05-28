class Solution:
    """
    @param str: A string
    @return: An integer
    """

    def stringToInteger(self, str):
        # 要考虑给的字符串是否有符号。
        # 然后从高位开始循环累加。
        # 转换公示如下
        # 5468 -> ((5 * 10 + 4) * 10 + 6) * 10 + 8

        num, sig = 0, 1

        if str[0] == '-':
            sig = -1
            str = str[1:]

        for c in str:
            num = num * 10 + ord(c) - ord('0')

        return num * sig
