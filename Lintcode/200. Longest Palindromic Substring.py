class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        # 基于中心线枚举的方法
        # O(n^2)
        if not s:
            return ""

        longest = ""
        for middle in range(len(s)):
            odd_palindrome = self.get_palindrome_from(s, middle, middle)
            if len(longest) < len(odd_palindrome):
                longest = odd_palindrome

            even_palindrome = self.get_palindrome_from(s, middle, middle + 1)
            if len(longest) < len(even_palindrome):
                longest = even_palindrome

        return longest

    def get_palindrome_from(self, s, left, right):
        while (left >= 0 and right < len(s)):
            if (s[left] != s[right]):
                break
            left -= 1
            right += 1

        return s[left + 1: right]
