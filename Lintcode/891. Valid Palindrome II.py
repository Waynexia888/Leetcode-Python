class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """

    def validPalindrome(self, s):
        # Write your code here
        if s is None:
            return False

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.removeOneCharacter(s, left + 1, right) or self.removeOneCharacter(s, left, right - 1)

        return True

    def removeOneCharacter(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
