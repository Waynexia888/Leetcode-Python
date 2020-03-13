# 两数之差问题:

# 问题描述
# 在一个数组中，求出满足两个数之差等于 target 的那一对数。返回他们的下标。

# LintCode 练习地址：
# http: // www.lintcode.com/problem/two-sum-difference-equals-to-target/

# 问题分析
# 作为两数之和的一个 Follow up 问题，在两数之和被问烂了以后，两数之差是经常出现的一个面试问题。
# 我们可以先尝试一下两数之和的方法，发现并不奏效，因为即便在数组已经排好序的前提下，
# nums[i] - nums[j] 与 target 之间的关系并不能决定我们淘汰掉 nums[i] 或者 nums[j]。

# 那么我们尝试一下将两根指针同向前进而不是相向而行，在 i 指针指向 nums[i] 的时候，
# j 指针指向第一个使得 nums[j] - nums[i] >= |target | 的下标 j：

# 如果 nums[j] - nums[i] == |target |，那么就找到答案
# 否则的话，我们就尝试挪动 i，让 i 向右挪动一位 = > i++
# 此时我们也同时将 j 向右挪动，直到 nums[j] - nums[i] >= |target|
# 可以知道，由于 j 的挪动不会从头开始，而是一直递增的往下挪动，那么这个时候，
# i 和 j 之间的两个循环的就不是累乘关系而是叠加关系。

# python:
nums.sort()
target = abs(target)

j = 1
for i in range(len(nums)):
    while j < len(nums) and nums[j] - nums[i] < target:
        j += 1
    if nums[j] - nums[i] == target
    