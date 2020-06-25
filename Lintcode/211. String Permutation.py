class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        return sorted(A) == sorted(B)
