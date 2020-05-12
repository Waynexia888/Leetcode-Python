class TwoSum:
    def __init__(self):
        self.counter = {}  # hashmap
    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        # hash, O(1)
        if number in self.counter:
            self.counter[number] += 1
        else:
            self.counter[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # O(n)
        for num in self.counter:  # iterate all keys in counter
            if value - num in self.counter and (value - num != num or self.counter[num] > 1):
                return True
        return False
