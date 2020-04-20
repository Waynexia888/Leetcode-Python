# 使用两个队列的BFS实现

# 我们可以将当前层的所有节点存在第一个队列中，然后拓展（Extend）出的下一层节点存在另外一个队列中。
# 来回迭代，逐层展开。

# 参考代码如下：
# Python:

# from collections import deque 

# queue1, queue2 = deque(), deque()
# seen = set()

# seen.add(start)
# queue1.append(start)
# currentLevel = 0
# while len(queue1):
#     size = len(queue1)
#     for _ in range(size):
#         head = queue1.popleft()
#         for neighbor in head.neighbors:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue2.append(neighbor)
#     queue1, queue2 = queue2, queue1
#     queue2.clear()
#     currentLevel += 1