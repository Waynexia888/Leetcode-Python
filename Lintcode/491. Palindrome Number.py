class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):

        # python中简单的方法
        # return num == int(str(num)[::-1])

        #第二种方法:
        # 翻转整个数字， 然后与之判断
        # 负数肯定不对称，肯定不是回文数字

        if num < 0:
            return False

        temp = num
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp = temp // 10

        return num == rev
