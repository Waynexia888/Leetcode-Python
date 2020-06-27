class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # DFS
        # 对于切分类（partition)问题，我们枚举可能的切分位置， 然后一一递归尝试
        if not s:
            return True

        if not dict:
            return False

        return self.dfs(s, dict)

    def dfs(self, s, dict):
        # 递归的出口, s不断的被切分，当s被切成空字符串时，递归结束
        if not s:
            return True

        for i in range(1, len(s) + 1):      # [1, len(s)], 前闭后闭
            if s[:i] in dict:
                if self.dfs(s[i:], dict):
                    return True

        return False
