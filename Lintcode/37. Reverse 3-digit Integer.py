class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """

    def reverseInteger(self, number):
        # write your code here
        #python 中的简写，一句代码
        # return int(str(number)[::-1])

        #注意，python 中整除是//， 浮点除是/
        #取出个位数
        a = number % 10
        #取出十位数
        b = number // 10 % 10
        #取出百位数
        c = number // 100 % 10
        return a * 100 + b * 10 + c
