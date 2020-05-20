class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, A):
        # Quick Select 算法
        # 时间复杂度O(n), 空间复杂度O(1)
        if not A or len(A) == 0:
            return None

        return self.quickSelect(A, 0, len(A) - 1, k)

    def quickSelect(self, A, start, end, k):
        if start == end:
            return A[start]

        # partition
        left, right = start, end
        pivot = A[(start + end) // 2]
        while left <= right:
            while left <= right and A[left] > pivot:
                left += 1
            while left <= right and A[right] < pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        # [start,....., right, x, left, ......, end]
        if (start + k - 1) <= right:
            return self.quickSelect(A, start, right, k)

        if (start + k - 1) >= left:
            return self.quickSelect(A, left, end, k - (left - start))

        return A[right + 1]
