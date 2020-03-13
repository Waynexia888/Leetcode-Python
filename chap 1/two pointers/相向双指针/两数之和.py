# 双指针的鼻祖：两数之和
# 题目描述
# 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
# 返回这两个数。

# 使用哈希表来解决

# python:

def twoSum(numbers, target):
    hash_set = set()

    for i in range(len(numbers)):
        if target - numbers[i] in hash_set:
            return (numbers[i], target - numbers[i])
        hash_set.add(numbers[i])

    return None


# 我们使用一个HashSet，来记录每个值是否存在。
# 每次查找 target - numbers[i] 是否存在，存在即说明找到了，返回两个数即可。


# 使用双指针算法来解决

# python:

# http: // www.lintcode.com/problem/two-sum/

class Solution:
    def twoSum(self, numbers, target):
        numbers.sort()

        L, R = 0, len(numbers)-1
        while L < R:
            if numbers[L] + numbers[R] == target:
                return (numbers[L], numbers[R])
            if numbers[L] + numbers[R] < target:
                L += 1
            else:
                R -= 1
        return None


# 首先我们对数组进行排序。
# 用两个指针(L, R)从左右开始：
# 如果numbers[L] + numbers[R] == target, 说明找到，返回对应的数。
# 如果numbers[L] + numbers[R] < target, 此时L指针右移，只有这样才可能让和更大。
# 反之使R左移。
# L和R相遇还没有找到就说明没有解。


# 两个算法的对比
# Hash方法使用一个Hashmap结构来记录对应的数字是否出现，以及其下标。
# 时间复杂度为O(n)。空间上需要开辟Hashmap来存储, 空间复杂度是O(n)。

# Two pointers方法，基于有序数组的特性，不断移动左右指针，减少不必要的遍历，
# 时间复杂度为O(nlogn)， 主要是排序的复杂度。
# 但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)

# 参考资料
# https://blog.csdn.net/luoshengkim/article/details/52175440
