class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def reverseString(self, s):
        # 背向双指针问题:
        #注意： 'str' object does not support item assignment，python不允许字符串的修改
        # 于是每次都截取并组建新的字符串来实现前后指针内容的调换。
        # 时间复杂度O(n), 空间复杂度： O(n)
        left, right = 0, len(s) - 1
        while left < right:
            #注意： 'str' object does not support item assignment，
            # python不允许字符串的修改
            # s[left], s[right] = s[right], s[left]
            s = s[:left] + s[right] + s[left+1: right] + s[left] + s[right+1:]
            left += 1
            right -= 1
        return s

    # "hello"
    # s= o + ell + h = oellh
    # left = 1, right = 3
    # s = o + l + l + e + h

        # 最简单一句翻转字符串
        # return s[::-1]
