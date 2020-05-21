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

        # 打擂台方法
        maxNUmber = num1
        if num2 > num1 and num2 > num3:
            maxNUmber = num2
        elif num3 > num1 and num3 > num2:
            maxNUmber = num3

        return maxNUmber
