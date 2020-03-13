# 问题描述
# 给你一个数组，要求去除重复的元素后，将不重复的元素挪到数组前段，并返回不重复的元素个数。

# LintCode 练习地址：http: // www.lintcode.com/problem/remove-duplicate-numbers-in-array/

# 问题分析
# 这个问题有两种做法，第一种做法比较容易想到的是，把所有的数扔到 hash 表里，
# 然后就能找到不同的整数有哪些。但是这种做法会耗费额外空间 O(n)。
# 面试官会追问，如何不耗费额外空间。

# 此时我们需要用到双指针算法，首先将数组排序，这样那些重复的整数就会被挤在一起。
# 然后用两根指针，一根指针走得快一些遍历整个数组，
# 另外一根指针，一直指向当前不重复部分的最后一个数。
# 快指针发现一个和慢指针指向的数不同的数之后，
# 就可以把这个数丢到慢指针的后面一个位置，并把慢指针++。

# 哈希表：
# O(n) time, O(n) space
class Solution:
    def deduplication(self, nums):
        d, result = {}, 0
        for num in nums:
            if  num not in d:
                d[num] = True
                nums[result] = num
                result += 1
        return result

# two pointers:
# O(nlogn) time, O(1) extra space
class Solution:
    def deduplication(self, nums):
        if len(nums) == 0:
            return 0

        nums.sort()
        result = 1  #第一根指针
        for i in range(1, len(nums)): #第二根指针
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
        
        return result

