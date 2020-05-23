class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """

    def reverseVowels(self, s):
        # python 中字符串是不能被修改的
        # 因此可以把string转变成列表list
        if not s or len(s) < 2:
            return s

        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        arr = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and arr[left] not in vowels:
                left += 1
            while left < right and arr[right] not in vowels:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return "".join(arr)  # python 中把字符数组转换成字符串的方法
