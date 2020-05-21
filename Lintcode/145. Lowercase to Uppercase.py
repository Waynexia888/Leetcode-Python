class Solution:
    """
    @param character: a character
    @return: a character
    """

    def lowercaseToUppercase(self, character):
        # 简单提一下：
        # 1. python中 string.upper()， 字符串的全部字母变成大写
        # 2. string.capitalize() method converts the first character of a string to capital (uppercase) letter.
        # 3. string.lower()

        #ASCII码中小写字母与对应的大写字母相差32
        # return chr(ord(character) - 32)

        return chr(ord(character) - (ord('a') - ord('A')))
