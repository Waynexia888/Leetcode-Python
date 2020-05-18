class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """

    def sortColors(self, nums):
        # 使用一次扫描的办法。
        # 设立三根指针，left, index, right。定义如下规则：
        # left 的左侧都是 0（不含 left）
        # right 的右侧都是 2（不含 right）
        # index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管。
        # 时间复杂度：O(n), 空间复杂度:O(1)

        # left, index, right = 0, 0, len(nums) - 1
        # while index <= right:
        #     if nums[index] == 0:
        #         nums[left], nums[index] = nums[index], nums[left]
        #         left += 1
        #         index += 1
        #     elif nums[index] == 2:
        #          nums[right], nums[index] = nums[index], nums[right]
        #          right -= 1
        #     else:
        #         index += 1

        # 使用暴力的方法，数一下0， 1， 2各自有多少个， 然后把整个array override
        # 但是这样做，相当于使用了2次扫描的方法，第一遍统计0， 1， 2 的频率， 第2遍将相应的元素放回数组
        # 时间复杂度：O(n), 空间复杂度:O(k), k为元素的取值范围， 在这题中， k为3， 所以空间复杂度也可以说是O(3), 即O(1)

        count_0, count_1, count_2 = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1
            else:
                count_2 += 1

        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_0 + count_1):
            nums[i] = 1
        for i in range(count_0 + count_1, len(nums)):
            nums[i] = 2
