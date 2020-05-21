class Solution:
    """
    @param num1: An integer
    @param num2: An integer
    @param num3: An integer
    @return: an interger
    """

    def maxOfThreeNumbers(self, num1, num2, num3):
        # python中max() 内置函数
        # return max(num1, num2, num3)

       if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
 
