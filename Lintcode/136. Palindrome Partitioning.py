class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # DFS
        if not s:
            return []

        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, temp, results):
        # 递归的出口
        if len(s) == 0:
            results.append(list(temp))
            return

        # 注意这里的分区是： 1 ～ len(s) + 1
        # 比如： "a", 1 ~ 2 是空字符串""; 如果是1 ~ 1 会报错
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):   # s[:1] 代表s[0],
                temp.append(s[:i])
                self.dfs(s[i:], temp, results)
                temp.pop()

    def isPalindrome(self, s):
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True
