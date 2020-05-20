class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        results = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                results.append('fizz buzz')
            elif i % 5 == 0:
                results.append('buzz')
            elif i % 3 == 0:
                results.append('fizz')
            else:
                results.append(str(i))
        return results
