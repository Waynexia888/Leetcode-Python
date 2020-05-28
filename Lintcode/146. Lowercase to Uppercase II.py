class Solution:
    """
    @param str: A string
    @return: A string
    """

    def lowercaseToUppercase2(self, str):
        # 使用python中String.upper()内置方法
        # return str.upper()

        # 把str转换成list（列表）
        # 遍历整个字符串，将所有的小写字母转成大写字母
        arr = list(str)
        for i in range(len(arr)):
            if arr[i] >= 'a' and arr[i] <= 'z':
                arr[i] = chr(ord(arr[i]) - 32)

        return "".join(arr)
