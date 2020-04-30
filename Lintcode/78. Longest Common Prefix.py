class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                # edge case: string index out of range
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        #  判断数组里第一个string是不是空字符串，[""]， 或者数组里只有一个string ["a"]
        return strs[0]
