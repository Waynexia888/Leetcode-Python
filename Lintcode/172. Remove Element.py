class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        if not A:
            return 0

        slow, fast = 0, 0
        while fast < len(A):
            if A[fast] != elem:
                # A[slow] = A[fast]
                A[slow], A[fast] = A[fast], A[slow]
                slow += 1
            fast += 1
        return slow
