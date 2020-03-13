# 相向双指针，指的是在算法的一开始，两根指针分别位于数组/字符串的两端，并相向行走。
# 如我们在小学的时候经常遇到的问题：

#小明和小红分别在铁轨A站和B站相向而行，小红的速度为 1m/s, 小明的速度为 2m/s，A站和B站相距 1km。
# 请问 ... 他们什么时候被火车撞死？

#  一个典型的相向双指针问题就是翻转字符串的问题。
# 在第二节课中我们学到的三步翻转法，就是一个典型的例子。

# python:

"""
@param s: a list of characters
"""


def reverse(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
