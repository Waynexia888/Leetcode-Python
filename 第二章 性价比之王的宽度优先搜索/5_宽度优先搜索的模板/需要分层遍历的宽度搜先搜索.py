# 需要分层遍历的宽度搜先搜索

# Python：

# from collections import deque

# queue = deque()
# seen = set()

# seen.add(start)
# queue.append(start)
# while len(queue):
#     size = len(queue)
#     for _ in range(size):
#         head = queue.popleft()
#         for neighbor in head.neighbors:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue.append(neighbor)

# 上述代码中：

# size = queue.size() 是一个必须的步骤。如果在 for 循环中使用 for (int i = 0; i < queue.size(); i++) 
# 会出错，因为 queue.size() 是一个动态变化的值。所以必须先把当前层一共有多少个节点存在局部变量 size 中，才不会把下一层的节点也在当前层进行扩展。
