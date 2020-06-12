class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # 使用列表list模拟一个栈stack
        # 注意list.pop(index)语法， 如果index不传，默认是-1，即最后一个元素
        # 参考资料： https://www.programiz.com/python-programming/methods/list/pop

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            if c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False

            if c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False

            if c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False

        return len(stack) == 0
