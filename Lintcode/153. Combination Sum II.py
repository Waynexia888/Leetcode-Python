class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        # 本题与Combination Sum不一样的是，每一个元素只能使用一次
        if not num:
            return []

        num.sort()
        results = []
        self.dfs(num, target, 0, [], results)
        return results

    def dfs(self, num, target, startIndex, temp, results):
        # 递归的出口
        if target == 0:
            results.append(list(temp))
            return

        for i in range(startIndex, len(num)):
            # 去重
            if i != 0 and num[i] == num[i - 1] and i > startIndex:
                continue

            if num[i] > target:
                return

            temp.append(num[i])
            self.dfs(num, target - num[i], i + 1, temp, results)
            temp.pop()
