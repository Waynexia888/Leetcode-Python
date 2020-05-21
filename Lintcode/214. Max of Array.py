class Solution:
    """
    @param A: An integer
    @return: a float number
    """

    def maxOfArray(self, A):
        # python中内置函数max()

        # return max(A)

        # 打擂台方法
        maxNumber = A[0]

        for i in range(1, len(A)):
            if A[i] > maxNumber:
                maxNumber = A[i]

        return maxNumber
