class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # 哈希表的做法， python中的dict()
        hashmap = dict()
        for i in range(len(numbers)):
            # 为什么先检测，在把数加进哈希表里呢？
            # 比如[2, 4, 5], target = 8； 如果先add num到哈希表里， 再检测，会返回结果的，但实际数组里只有一个4
            if target - numbers[i] in hashmap:
                return [hashmap[target - numbers[i]], i]
            hashmap[numbers[i]] = i
        return [-1, -1]
