class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        # python 中: 检验key是否存在在dict里？ print 'a' in d

        dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in dict or dict[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True
