class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # a + b + c = 0 => -a = b + c, a <= b <= c
        numbers.sort()
        results = []
        length = len(numbers)
        for i in range(0, length - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.find_two_sum(numbers, i + 1, length - 1, -numbers[i], results)
        return results

    def find_two_sum(self, numbers, left, right, target, results):
        while left < right:
            if numbers[left] + numbers[right] == target:
                results.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
