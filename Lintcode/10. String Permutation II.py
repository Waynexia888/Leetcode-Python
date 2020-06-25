class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        # write your code here
        chars = sorted(list(str))
        isUsed = [False] * len(str)
        permutations = []

        self.stringPermutation2Helper(chars, isUsed, [], permutations)
        return permutations

    def stringPermutation2Helper(self, chars, isUsed, temp, permutations):
        if len(temp) == len(chars):
            permutations.append(''.join(temp))
            return

        for i in range(len(chars)):
            # 如果已经用过了该字符，跳过即可
            if isUsed[i] == True:
                continue

            # 去重步骤
            # 不能跳过一个a选下一个a
            if i != 0 and chars[i] == chars[i - 1] and isUsed[i - 1] == False:
                continue

            # make change
            isUsed[i] = True
            temp.append(chars[i])

            # 找到所有 temp 开头的排列
            self.stringPermutation2Helper(chars, isUsed, temp, permutations)

            # backtracking
            temp.pop()
            isUsed[i] = False
