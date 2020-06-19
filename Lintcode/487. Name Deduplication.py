class Solution:
    """
    @param names: a string array
    @return: a string array
    """

    def nameDeduplication(self, names):
        # write your code here
        dict = {}
        result = []

        for name in names:
            s = name.lower()
            if s not in dict:
                dict[s] = 1
                result.append(s)
        return result
