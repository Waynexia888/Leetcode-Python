class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # 排序（方便结果去重） + DFS
        # 因为本题元素可以重复使用，所以在递归的时候，向下传递的start值还是i，在下层递归函数中依然会考虑加入candidates[i]是否能够满足条件的情形
        # 本题属于DFS中的组合类， 所以考虑用startIndex

        if not candidates:
            return []

        results = []
        candidates.sort()    # 排序
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, startIndex, temp, results):
        # 递归的出口
        if target == 0:
            results.append(list(temp))   # deep copy
            return
        for i in range(startIndex, len(candidates)):
            # 去重
            if i != 0 and candidates[i] == candidates[i - 1] and i > startIndex:
                continue
            # 缩小dfs范围
            if candidates[i] > target:
                return

            temp.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, temp, results)
            temp.pop()
