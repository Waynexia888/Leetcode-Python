class Calculator:
    """
    @param a: An integer
    @param operator: A character, +, -, *, /.
    @param b: An integer
    @return: The result
    """

    def calculate(self, a, operator, b):
        # 注意： Python中是不提供switch/case语句的
        if operator == "+":
            return a + b
        if operator == "-":
            return a - b
        if operator == "*":
            return a * b
        if operator == "/":
            return a // b
