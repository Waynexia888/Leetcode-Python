class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []
    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack2.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if (len(self.stack1) == 0):
            self.move()

        return self.stack1.pop()

    """
    @return: An integer
    """

    def move(self):
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if (len(self.stack1) == 0):
            self.move()

        return self.stack1[-1]
