class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # recursion method:
        # if n == 1:
        #     return 0
        # if n == 2:
        #     return 1
        # return self.fibonacci(n - 1) + self.fibonacci(n - 2)

        a, b = 0, 1
        for _ in range(0, n - 1):
            c = a + b
            a = b
            b = c
        return a
