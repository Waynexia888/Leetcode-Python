class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results
        
    # Time Complexity: O(n)
    # space complexity: O(1)