# 无需分层遍历的宽度优先搜索

# Python:

# from collections import deque

# queue = deque()
# seen = set()  #等价于Java版本中的set

# seen.add(start)
# queue.append(start)
# while len(queue):
#     head = queue.popleft()
#     for neighbor in head.neighbors:
#         if neighbor not in seen:
#             seen.add(neighbor)
#             queue.append(neighbor)


# 上述代码中：

# neighbor 表示从某个点 head 出发，可以走到的下一层的节点。
# set/seen 存储已经访问过的节点（已经丢到 queue 里去过的节点）
# queue 存储等待被拓展到下一层的节点
# set/seen 与 queue 是一对好基友，无时无刻都一起出现，往 queue 里新增一个节点，就要同时丢到 set 里。
