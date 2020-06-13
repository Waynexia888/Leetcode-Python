class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        # https://pynative.com/python-range-function/
        # time O(n^2)

        if target is None or target == "":
            return 0

        for i in range(len(source) - len(target) + 1):
            if source[i:i + len(target)] == target:
                return i

        return -1
