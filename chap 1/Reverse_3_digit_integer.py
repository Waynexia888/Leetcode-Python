#  reverse a 3-digit integer
# example: 123 -> 321; 900 -> 9

# Solution 1:
# 可以先把每个数字先取出来，然后拼接起来

class Solution:
    def reverseInteger(self, number):
        # abc
        c = number % 10
        b = number / 10 % 10 
        a = number / 100 

        return c * 100 + b * 10 + a