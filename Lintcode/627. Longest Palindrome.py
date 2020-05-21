class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # 巧妙的运用hash 来实现O(1)
        if not s or len(s) == 0:
            return 0

        dict = {}
        count = 0
        for c in s:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1

        #有三种情况，1: dict[i] = 偶数；成对字母， count + 2
        # 2. dict[i] = 非1的基数，例如3， 那么count + 3 - 1
        # 3. dict[i] = 1 可能这种单个数字比较多，所以在此不作任何处理

        for i in dict:
            if dict[i] % 2 == 0:
                count += dict[i]
            elif dict[i] != 1 and dict[i] % 2 == 1:
                count += dict[i] - 1

        # 对于dict[i] = 1这种情况， 需要判断一下
        # 有两种情况： "aaaa", "bacab"
        if count < len(s):
            return count + 1
        else:
            return count
