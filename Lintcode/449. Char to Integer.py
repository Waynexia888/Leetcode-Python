class Solution:
    """
    @param character: a character
    @return: An integer
    """

    def charToInteger(self, character):
        # ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
        # 参考资料： https://www.runoob.com/python3/python3-func-ord.html
        if character is None:
            return 0

        return ord(character)
