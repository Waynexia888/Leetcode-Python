# 如下的一些场景是使用宽度优先搜索的常见场景：

# 图的遍历 Traversal in Graph
# 图的遍历，比如给出无向连通图(Undirected Connected Graph)中的一个点，找到这个图里的所有点。这就是一个常见的场景。
# LintCode 上的 Clone Graph 就是一个典型的练习题。

# 更细一点的划分的话，这一类的问题还可以分为：

# 层级遍历 Level Order Traversal
# 由点及面 Connected Component
# 拓扑排序 Topological Sorting
# 层级遍历，也就是说我不仅仅需要知道从一个点出发可以到达哪些点，还需要知道这些点，分别离出发点是第几层遇到的，比如 Binary Tree Level Order Traversal 就是一个典型的练习题。

# 由点及面，前面已经提到。

# 拓扑排序，让我们在后一节中展开描述。

# 最短路径 Shortest Path in Simple Graph
# 最短路径算法有很多种，BFS 是其中一种，但是他有特殊的使用场景，即必须是在简单图中求最短路径。
# 大部分简单图中使用 BFS 算法时，都是无向图。当然也有可能是有向图，但是在面试中极少会出现。

# 什么是简单图（Simple Graph）？
# 即，图中每条边长度都是1（或边长都相同）。
