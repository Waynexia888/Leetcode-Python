class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # 双指针问题，两根指针分别指向A，B数组最后一个元素，从后往前遍历
        # 同时比较他们的大小，然后放入A数组下标为m-1+n的位置，依次循环
        index_A, index_B, insert_index = m - 1, n - 1, m - 1 + n

        # A, B两个数组，以比较小的数组结束循环
        while index_A >= 0 and index_B >= 0:
            if A[index_A] <= B[index_B]:
                A[insert_index] = B[index_B]
                index_B -= 1
            else:
                # swap过程，或者A[insert_index] = A[index_A]
                A[insert_index], A[index_A] = A[index_A], A[insert_index]
                index_A -= 1
            insert_index -= 1

        # 上述比较小的数组结束循环后， 比较大的数组需要重新插入元素
        #   但是由于是B往A插入元素并且合并， 所以只需要考虑B数组还有剩余的元素在上述循环中没插入的情况
        while index_B >= 0:
            A[insert_index] = B[index_B]
            index_B -= 1
            insert_index -= 1
