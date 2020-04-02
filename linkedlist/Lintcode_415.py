# Lintcode 415: 有效回文串  · Valid Palindrome

# 题目描述: Given a string, determine if it is a palindrome, considering only 
# alphanumeric characters and ignoring cases.
# 给定一个字符串，判断其是否为一个回文串。只考虑字母和数字，忽略大小写。

# 样例1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama"

# 样例2:
# Input: "race a car"
# Output: false
# Explanation: "raceacar"


# # 使用两根指针遍历整个字符串即可.
# 假定有指针i, j, 其中i是从前往后遍历, j是从后往前遍历.
# 当i在j左边时继续循环, 每一次将i右移到数字/字母上, j左移到数字/字母上,
# 比较二者对应的字符串内的字符是否相同, 不相同则原字符串不是回文串.
# 如果全部的比较都相同, 说明是回文串.
# The isalpha() method checks whether the string consists of alphabetic characters only.   参考： https://www.tutorialspoint.com/python3/string_isalpha.htm
# The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
# 参考： https://www.programiz.com/python-programming/methods/string/isdigit
# The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
# 参考： https://www.programiz.com/python-programming/methods/string/isalnum

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if start < end and s[start].lower() != s[end].lower()
                return False
            start += 1
            end -= 1

        return True
