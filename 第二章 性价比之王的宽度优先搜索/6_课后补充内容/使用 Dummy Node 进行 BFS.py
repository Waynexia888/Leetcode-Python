# 使用 Dummy Node 进行 BFS

# 什么是 Dummy Node
# Dummy Node，翻译为哨兵节点。Dummy Node 一般本身不存储任何实际有意义的值，通常用作"占位"，
# 或者链表的“虚拟头”。
# 如很多的链表问题中，我们会在原来的头head的前面新增一个节点，这个节点没有任何值，
# 但是 next 指向 head。这样就会方便对 head 进行删除或者在前面插入等操作。

# head -> node -> node -> node ...
# =>
# dummy -> head -> node -> node -> node...

# Dummy Node 在 BFS 中如何使用
# 在 BFS 中，我们主要用 dummy node 来做占位符。即，在队列中每一层节点的结尾，都放一个 null
# （or None in Python，nil in Ruby），来表示这一层的遍历结束了。这里 dummy node 就是一个 null。

# Python:

# from collections import deque

# queue = deque()
# seen = set()

# seen.add(start)
# queue.append(start)
# queue.append(None)
# currentLevel = 0
# while len(queue) > 1:
#     head = queue.popleft()
#     if head == None:
#         currentLevel += 1
#         queue.append(None)
#         continue
#     for neighbor in head.neighbors:
#         if neighbor not in seen:
#             seen.add(neighbor)
#             queue.append(neighbor)