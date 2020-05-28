class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # set() 函数创建一个无序不重复元素集
        # set.add() 添加元素
        # set.remove() 删除元素
        # 资料参考： https://liuzhichao.com/p/1645.html
        # Time complexity : O(2n) = O(n). In the worst case each character will 
        # be visited twice by i and j.
        # Space complexity : O(min(m, n)). Same as the previous approach. We 
        # need O(k) space for the sliding window, where k is the size of the Set. 
        # The size of the Set is upper bounded by the size of the string nn and 
        # the size of the charset/alphabet m.

        hash_set = set()
        left, right = 0, 0
        max_length = 0

        while left < len(s) and right < len(s):
            if s[right] not in hash_set:
                hash_set.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                hash_set.remove(s[left])
                left += 1

        return max_length
