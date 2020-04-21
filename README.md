# Leetcode-Python
* 参考官方文档： https://docs.python.org/3/tutorial/controlflow.html
### Lession 1: Variable & Control flow
* 基础语法： https://www.tutorialspoint.com/python3/python_lists.htm
* Fizz Buzz
* Reverse 3-digit Integer
* int变量： a = 1， a = b = c = 1, a = b = c = 1, 100, "linpz"
* float, double 变量
* boolean 变量只有两个取值：True & False 对应 真和假; 常见的三个操作：and 与, or 或, not 非
* 程序的三大结构：
  * 顺序结构： 顺序执行语句，从上到下执行
  * 控制结构：根据条件，选择进入程序执行的分支
  * 循环结构：不断重复的做一件事情
* 如何遍历从0～100， 或者从0到n？
  * for num in xrange（n + 1）
  * 使用xrange 实际上是使用了迭代器，不需要内存； 使用range，实际上是生成一个list， 需要内存去存这些数据
* 如何遍历从m到n？
  * for num in xrange（m，n + 1）
* 如何遍历从10到5？
  * for num in xrange（10，4，-1） -> 【10， 9， 8， 7， 6， 5】
* 如何遍历从n到m，但是每隔2个（如：100，98，96…..）？
  * for num in xrange（10，4，-2） -> 【10，8，6】
  * for num in xrange（n，m，-2）
* For 循环中的enumerate函数：使用enumerate函数：
  * 可以获得下标
  * 可以获得数值
  * for index， value in enumerate（【2， 3， 4， 5】）
  * print index， value
  * 0->2, 1->2, 2->4, 3->5
* While 循环的使用
  * sum = 0
  * i = 0
  * while i <= 100:
  *     sum += 1
  *     i += 1
  * print sum [->5050]
* For循环 (range的用法)
  * range(101) 会生成一个0～100的list
  * range(m, n) 会生成一个m～n-1的list m < n
  * range(n, m, -1) 会生成一个n到m-1的降序的list
  * range(n, m, -2) 会生成一个n到m-1的降序的每隔一个数的list
* 循环中的continue语句
  * 如果条件满足， 跳过该条件的条件框（eg：跳过 print i）
  * for i in range(10):
  *     if i == 5:
  *         continue
  *     print i     (the answer is : 0, 1, 2, 3, 4, 6, 7, 8, 9)
* 循环中的Break语句
  * 如果条件满足，整个for 循环都退出，不再执行了
  * for i in range(10):
  *     if i == 5:
  *         break
  *     print i     (the answer is : 0, 1, 2, 3, 4)
* if else 循环语句：
  * 参考： https://docs.python.org/3/tutorial/controlflow.html
  * if -> elif -> else
* lintcode 练习
  * 479 second max of array
  * 478 simple calculator
  * 283 max of 3 numbers
  * 145 lowercase to uppercase
  * 37 reverse 3-digit integer
  * 9 fizz buzz
### Lession 2: Function & Class
* lintcode 练习
  * 454 Rectangle Area
  * 222 Setter and Getter
  * 455 Student ID
  * 218 Student Level
  * 497 Shape Factory
### Lession 3: 线性数据结构 string, list, tuple & linkedlist
* 字符串 String
  * 可以使用单引号或者双引号, 在一份代码中保持统一 , eg: str1 = 'hello world!'
  * 连接两个字符串 eg: print str1 + str2
  * 如何给子串连接一个整数，或者一个实数？ -> str 函数: 其他任何类型的变量转变成为字符串; str()
  * 字符串的长度计算 -> print len(str1)
  * 访问字符串中的字符 -> print str1[6]; 通过name[index]的方式访问
  * 遍历String中的每一个字符 -> 两种for循环方式，取决于是否需要index: 1 for c in str:    2 for idx in range(len(str)):
  * 面试真题: String To Integer -> https://www.jiuzhang.com/solution/string-to-integer/
  * 面试真题: Rotate String -> https://www.lintcode.com/problem/rotate-string/description
  * 字符串在python里是不能修改的； eg：错误示范: str1[2] = 'c'
  * str = 'jiuzhang'  print str[1:3] -> iu;   print str[1:] -> iuzhang;    print str[:5] -> jiuzh;    print str[:] -> jiuzhang;
* List 列表
  * Python的基本数据结构之一： eg: a = ['1', '2', '3']
  * 列表的常见操作：加(array + array); 乘(array * 3 备份3遍）; 元素检测(eg: 3 in array -> return true or false)
  * 列表的常见操作：加入元素（array.append()); 合并（array.extend(); eg: [1, 2, 3].extend([4, 5, 6]) -> [1, 2, 3, 4, 5, 6])
  * 列表的常见操作：删除元素（del array[1]); 索引(eg: array[3]); 切片(eg: array[2:5] 不包含5这个位置)；反转（array[5:2:-1])
  * 列表的常见操作：求list的最大，最小值 (max(); min()); pop 操作 (b = [1, 2, 3], print b.pop(1) -> 2)
  * 面试真题: Remove Element     (http://www.lintcode.com/en/problem/remove-element/)
  * 如何把一个整数变成一个list？ eg: n = 19, print(list(str(n))) -> ['1', '9']
* Tuple 元祖
  * 提问：为什么我们需要tuple？ (元祖tuple的存在是 为了优化我们的list，因为list消耗内存太大了，然后list的数据是可变的，导致list一定不能作为hash的key。 然而tuple里的数据是不可以修改的，节省内存空间的问题，并且解决了可以hash的问题）
  * Tuple 元组的创建： 使用小括号扩起来的， eg：tup1 = （'hello', 'jiuzhang', 5)
  * tup5 = (10,)  如果tuple里只有一个元素， 需要加一个逗号， 否则就是一个整数10， 而不是元祖
  * Tuple 元组的访问与修改： 访问第i个元素（tup3[i]); 提取一段sub tuple(tup3[3:5]); 
  * Tuple 元组的访问与修改：tuple中的元素是无法修改的: tup2[2] = 4 出错
  * Tuple 元组连接和删除: 连接操作生成了新的tuple -> 因为tuple不支持修改，所以只能生成新的
  * Tuple 元组连接和删除: 使用del语法删除已经存在的tuple -> del tup2
  * 获取tuple的元素个数: len((1,2,3)) -> 3
  * 判断元素是否在tuple中出现: 4 in (4,5,6) -> True
  * 遍历tuple: for x in (4,5,6): print x -> 4, 5, 6
  * 连接生成新的tuple: (1,2,3)+(4,5,6) -> (1, 2, 3, 4, 5, 6)
  * List 列表和tuple 元组之间的转换: tuple([]) -> tuple([1,2,3]) => (1,2,3)
  * List 列表和tuple 元组之间的转换: list(()) -> list((1,2,3)) => [1,2,3]
* LinkedList 链表 自定义数据结构
  * 对象去哪儿了？ node = ListNode(10); node不是对象本身，是对象的引用; 
  * 对象存储在堆空间（heap space）上（画图) -> 堆空间 heap space; 栈空间 stack space (演示stack overflow); 注意区别于数据结构的heap & stack
  * 什么是reference(引用)?   引用好比遥控器，对象好比电视机
  * 引用的赋值: node1 = ListNode(10); node2 = ListNode(20); -> 这里有两个对象, node1和node2是这两个对象的引用
  * 引用的好处与用处：1 引用也存的是数据，存的是指向这个对象的地址; 2 使得数据更加的整齐; 3 需要专递引用去修改数据
  * 什么是数据结构（data structure）? -> 数据: 存储数据的功能; 结构: 如何组织排列存储的数据; 操作: 如何查询，添加，删除维护存在的数据
  * 什么是链表（linked list）? -> 由节点构成的列表, 线性的数据结构； 参考：https://blog.csdn.net/qq_39422642/article/details/78988976
  * 链表的基本元素有：1 节点：每个节点有两个部分，左边部分称为值域，用来存放用户数据；右边部分称为指针域，用来存放指向下一个元素的指针.
  * 2 head:head节点永远指向第一个节点
  * 3 tail: tail永远指向最后一个节点
  * 4 None:链表中最后一个节点的指针域为None值
  * class ListNode:
  *     def __init__(self, value):
  *         self.val = value
  *         self.next = None
  * 基于ListNode实现一个Linked List:  see attached code above...
  * 不得不提的dummy Node：伟大的哨兵节点：dummyNode-> null; 作用（前驱节点的重要性）：使得每一个元素都有前驱节点
  * 哨兵节点,也是头结点,是一个 dummy node. 可以用来简化边界条件. 是一个附加的链表节点.该节点作为第一个节点,它的值域不存储任何东西. 只是为了操作的方便而引入的. 如果一个链表有哨兵节点的话,那么线性表的第一个元素应该是链表的第二个节点.
  * 链表的操作: 遍历（traverse）; 插入（insert）; 查找（find）; 删除（delete）
  * LinkedList Class的接口：1 读取操作 get(location) // 获取location位置上的node的value, Time Complexity: O(n)
  * LinkedList Class的接口：2 查找操作 contains(val) // 判断链表中是否含有val值的node, Time Complexity: O(n)
  * LinkedList Class的接口：3 插入操作 add(location, val) // 在location的位置上插入一个值为val的node, Time Complexity: O(1)
  * LinkedList Class的接口：4 删除操作 remove(location) // 删除location位置上的元素, Time Complexity: O(n)
  * 面试真题: Reverse Linked List -> http://www.lintcode.com/en/problem/reverse-linked-list/
  * 面试真题: Remove Nth Node From End of List -> http://www.lintcode.com/en/problem/remove-nth-node-from-end-of-list/
* lintcode 练习
  * 483 Convert Linked List to Array List
  * 225 Find Node in Linked List
  * 219 Insert Node in Sorted Linked List
  * 452 Remove Linked List Elements
  * 241 String to Integer
  * 415 Vaild Palindrome
  * 174 Remove Nth Node from End of list
  * 165 Merge Two Sorted Lists
* leetcode 总结面试题：
  * https://www.jianshu.com/p/490cb181946f
  * https://zhuanlan.zhihu.com/p/62242201
### Lession 4: 线性数据结构 Queue & Stack
* 数据结构Recap
  * 数据结构 = 数据 + 存储方式 + 操作
  * 数据： 存储什么数据？ 如int， string类型
  * 存储方式： 如何组织数据， 数据之间的关系？
  * 操作： 如何快速的读取查询数据， 写入数据到数据结构中？
  * 不要求数据的顺序， 维护成本低， 比如： list列表
  * 要求数据的顺序，维护成本高，使用成本低， 比如： 排序的list
* 栈 Stack
  * 什么是栈（stack）： 栈是一种先进后出（last in first out，LIFO)的线性数据结构
  * 栈的操作： push：放入一个元素； pop：弹出一个元素； top：获取栈顶元素； empty：判断栈是否为空
  * 栈的实现 -> 使用基于list实现stack
  * 面试真题： Implement Stack -> https://www.lintcode.com/en/problem/implement-stack/
  * 面试真题： Valid Parentheses -> https://www.lintcode.com/en/problem/valid-parentheses/
* Queue 队列
  * 什么是队列（queue）：队列是一种先进先出（first in first out, FIFO)的线性数据结构。例如： 食堂里排队打饭， 过安检的时候排队
  * Queue提供的接口方法：
  * 1 Queue() 定义一个空队列，无参数，返回值是空队列
  * 2 enqueue(item)在队列尾部加入一个数据项，参数是数据项，无返回值
  * 3 dequeue()删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化
  * 4 isEmpty()检测队列是否为空， 无参数，返回布尔值
  * 5 size()返回队列数据项的数量，无参数，返回一个整数
  * Queue模块中队列的提供的结构： put (enqueue)：元素进队列； get (dequeue)：元素出队列； empty： 判断队列是否为空
  * 队列的实现： 1 使用ListNode实现Queue； 2 使用Queue模块
  * 面试真题： Implement Queue by Linked List -> http://www.jiuzhang.com/solution/implement-queue-by-linked-list/
  * Python提供的Queue模块：Python中队列是线程间最常用的交换数据的方式, 如下：
  * import Queue
  * queue = Queue.Queue(maxsize = 10)
  * 注意：如果maxsize小于1就表示队列长度无限
  * put 元素放入队列： queue.put(10) -> put()方法在队尾插入一个元素， 如果队列是满的，该线程会阻塞（等待），直到空出一个位置来，然后在队尾放入元素  
  * get 获取队列的元素： queue.get() -> get()方法从队头删除并返回一个项目，队列为空默认为阻塞线程（等待），直到有元素放入到队列之后，将其取走
  * Python使用Queue实现生产者消费者模型：
  * 什么是生产者消费者模型：1 当某模块或者组件负责生产数据， 然后这些数据由其他模块或者组件来负责处理（此处的模块可能是：函数，线程，进程等）
  * 2 产生数据的模块或者组件称为生产者，而处理数据的模块称为消费者
  * 3 在生产者与消费者之间有缓冲区，生产者负责往缓冲区放数据，消费者负责从缓冲区读取数据，这就形成了生产者消费者模式
  * 生产者消费者模式的优点：
  * 1 解耦：如果消费者直接调用生产者的代码，那么代码会相互产生依赖（耦合），通过中间的缓冲区可以解耦两者
  * 2 并发： 由于生产者和消费者是两个不同的模块，对于生产者而言它负责生产数据，只要往缓存区中丢数据完成，就可以继续生产下一个数据，不会因为数据是否被消费而阻塞
  * 队列的应用：Message queue 消息队列； https://github.com/apache/kafka   ； https://github.com/rabbitmq/rabbitmq-server
  * 队列的应用：BFS 广度优先搜索
* Dict 字典 -> 相当于哈希表
  * 生成一个dict有两种方法： 1 d = {} ; 2 d = dict()
  * 如何赋值？ d['a'] = 100 ; d['b'] = 200
  * print d['a'] -> 100;  print d['b'] -> 200;
  * 检验key是否存在在dict里？  print 'a' in d
  * 获取所有的keys： print d.keys()
  * 获取所有的values： print d.values()
  * 如何循环字典里的key， value？ -> for key, value in d.items():  print key, value
  * 如何循环字典里的key？ -> for key in d.keys():  print key
  * 如何循环字典里的value？  -> for value in d.values():  print value 
* lintcode 练习
  * 495 Implement Stack
  * 494 Implement Stack by Two Queues
  * 423 Valid Parentheses
  * 40 Implement Queue by Two Stacks
### Lession 5: 树结构与递归  Tree & Recursion
* 树 Tree
  * 由节点（node）组成, 每个节点有零个或多个子节点（child node）, 没有父节点的是根节点（root node）, 一棵树中，只有一个root node
  * 每个非根节点只有一个父节点（parent node）, 没有任何子节点的节点叫叶子节点（leaf node）
* 二叉树 Binary Tree
  * 每个节点最多有两个子节点, 两个子节点分别被称为左孩子（left child）和右孩子（right child）, 叶子节点：没有孩子节点的节点
  * 子树（sub-tree）: 树中的每个节点代表以它为根的一棵树, 左孩子所代表的树成为左子树（left sub-tree）, 右孩子所代表的树成为右子树（right sub-tree）
  * 树结构，随处可见的数据结构: eg: 文件系统 B+树 ; 数据库的索引－第七节课; 字典树，平衡树等 - 高级数据结构
  * 剖析LintCode TreeNode:
  * class TreeNode:
  *     def __init__(self, val):
  *         self.val = val
  *         self.left, self.right = None, None
* 学习目标1:
  * 构造一棵二叉树 Construct a binary tree
  * 打印出这课二叉树 print a binary tree
  * Coding & Print: 构造和打印二叉树. -> see attached files
* 树（二叉树）的遍历 （Binary Tree Traversal）:
  * 先序遍历（Preorder traversal）: 口诀：根左右
  * 中序遍历（Inorder traversal）: 口诀：左根右.  https://zh.wikipedia.org/wiki/%E6%A0%91%E7%9A%84%E9%81%8D%E5%8E%86
  * 后序遍历（Postorder traversal）: 口诀：左右根
* 如何遍历一棵树？: 使用递归的方式!!
* 程序实现一般有两种方式：
  * 递归的实现方式
  * 非递归的实现方式
* 什么是递归 (Recursion)？
  * 数据结构的递归 -> 树就是一种递归的数据结构
  * 算法（程序）的递归 -> 函数自己调用自己
* 递归三要素
  * 递归的定义: 首先这个问题或者数据结构得是递归定义的
  * 递归的出口: 什么时候递归终止
  * 递归的拆解: 递归不终止的时候，如何分解问题
* 经典例题: Fibonacci. -> http://www.lintcode.com/en/problem/fibonacci/
  * 递归的定义：因为斐波那契数列满足F(n) = F(n - 1) + F(n - 2)
  * 递归的出口：n = 0 和 n = 1的时候，问题规模足够小的时候
  * 递归的拆解：return self.fibonacci(n - 1) + self.fibonacci(n - 2)
* Coding: 打印出一个树的中序遍历 -> see attached files
* 学习目标2:
  * 获取所有叶子节点的和 Get leaf sum
  * 获取树的高度 Get tree height
  * 获取所有root到叶子节点的路径 Get root-to-leaf paths
* Recursion 获取叶子节点的和
  * 访问一个Node：1 如果这个Node是叶子节点，则sum就是他本身;
  * 2 如果这个Node不是叶子节点，则sum等于左子树的叶子节点和 + 右子树之和
  * 实战例题: Binary Tree Leaf Sum -> http://www.lintcode.com/en/problem/binary-tree-leaf-sum/
* Recursion 获取树的高度
  * 访问一个Node：1 如果这个Node是叶子节点，则高度是1
  * 如果这个Node不是叶子节点，则高度等于 = max(左子树的高度, 右子树的高度) + 1
  * 实战例题: Maximum Depth of Binary Tree -> http://www.lintcode.com/en/problem/maximum-depth-of-binary-tree/
* Recursion 获取树中root到leaf的所有路径:
  * 能否根据之前两个问题，我们来做同样的分析？
  * 实战例题: Identical Binary Tree -> http://www.lintcode.com/en/problem/identical-binary-tree/
  * 题目大意：判断两棵Tree是否同构，同构的定义是可以通过交换左右子树是的他们相同
* Recursion 判断子树是否同构:
  * 访问一个A树中的Node1, 和B树中的Node2：
  * 1 如果这个Node1和Node2都是NULL，则同构
  * 2 如果这个Node1和Node2都不是NULL，则同构的条件是: 1 Node1和Node2节点val相同; 2 Node1和Node2的left subtree同构且Node1和Node2的right subtree同构
  * 3 他们不同构
* LintCode 树的遍历问题:
  * Binary Tree Preorder Traversal -> http://www.lintcode.com/en/problem/binary-tree-preorder-traversal/
  * Binary Tree Inorder Traversal -> http://www.lintcode.com/en/problem/binary-tree-inorder-traversal/
  * Binary Tree Postorder Traversal -> http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/
  * 更多Traversal的问题: ->  http://www.lintcode.com/en/tag/binary-tree-traversal/
* lintcode 练习
  * 376 Binary Tree Path Sum
  * 482 Binary Tree Level Sum
  * 481 Binary Tree Leaf Sum
  * 480 Binary Tree Paths
  * 97 Maximum Depth of Binary Tree
* lintcode 练习: Hash Table
  * 647 Substring Anagrams
  * 644 Mirror Numbers
  * 557 Count Characters
  * 487 Name Deduplication
### Lession 6: 常用排序算法原理与应用  Principle and Application of Sorting Algorithm
* 本节重点
  * 如何用分治法(Divide and Conquer)解决排序问题
  * 如何分析分治算法的时间和空间复杂度
  * 如何有效避免快速排序的最坏情况
  * 归并排序 Merge Sort
  * 快速排序 Quick Sort
  * 在Python中使用排序
* 自学内容，以下三种排序时间复杂度均为O(n^2):
  * 选择排序 Selection Sort, 不是稳定的排序算法
  * 插入排序 Insertion Sort, 稳定的排序算法
  * 冒泡排序 Bubble Sort, 稳定的排序算法
  * 演示界面：http://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
* 归并排序和快速排序 Merge sort & Quick sort
  * Merge sort: 最坏时间复杂度O(nlogn), 稳定的排序算法
  * 什么是稳定的排序算法：简单的来说，就是数组里有两个相同的数，那么不管排序前还是排序后，原来在前面的一定还是在前面。
  * Quick sort: 均摊复杂度(亦或者是平均复杂度)O(nlogn), 不是稳定的排序算法
* Merge Sort
* lintcode 练习
  * 463 Sort Integers
  * 464 Sort Integers II
  * 173 Insertion Sort List
  * 184 Largest Number
  * 148 Sort Colors
  * 143 Sort Colors II
  * 139 Subarray Sum Closest
  * 98 Sort List
  * 5 Kth Largest Element
### Lession 8: 性价比之王的宽度优先搜索 Breadth First Search
* 先修内容
  * 请在随课教程中先修如下内容：http://www.jiuzhang.com/tutorial/algorithm/14
  * 什么是队列，如何自己实现一个队列
  * 什么是 Interface，LinkedList 和 Queue 之间的关系是什么？ Java 才需要学习，Python和C++可以直接跳过（爽不爽！）
  * 什么是拓扑排序 Topological Sorting
  * 如何定义一个图的数据结构
* 大纲 Outline
  * 宽度优先搜索算法是一个性价比极高的算法, 如果你只有很短的时间准备面试（比如一周），那么你应该把时间花在宽度优先搜索上
  * 什么时候使用 BFS
  * 二叉树上的 BFS
  * 图上的 BFS
  * 矩阵上的 BFS
  * 拓扑排序 Topological Sorting
* 什么时候应该使用BFS？
  * 图的遍历 Traversal in Graph: 1 层级遍历 Level Order Traversal 2 由点及面 Connected Component 3 拓扑排序 Topological Sorting
  * 最短路径 Shortest Path in Simple Graph: 仅限简单图求最短路径, 即，图中每条边长度都是1，或者边长都相等
  * 非递归的方式找所有方案 Iteration solution for all possible results(这一点我们将在后面 DFS 的课上提到)
* 如果题目问最短路径, 除了BFS还可能是什么算法？(动态规划DP), 如果问最长路径呢？
* 题型与算法的对应关系
  * 最短路径: 简单图 → BFS, 复杂图 → Dijkstra, SPFA, Floyd（一般面试不考这个）
  * 最长路径: 图可以分层 → Dynamic Programming, 分层：比如走到第i一定会经过第 i-1 层（棋盘格子图是典型的例子）; 不可以分层 → DFS
* 二叉树上的宽度优先搜索 BFS in Binary Tree
  * Binary Tree Level Order Traversal, 图的遍历（层级遍历）, 注：树是图的一种特殊形态，树属于图
  * http://www.lintcode.com/problem/binary-tree-level-order-traversal/
  * http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal/
* 宽搜要点 BFS Key Points
  * 使用队列作为主要的数据结构 Queue; 思考：用栈（Stack）是否可行？为什么行 or 为什么不行？
  * 是否需要实现分层？ 需要分层的算法比不需要分层的算法多一个循环
  * Java / C++: size=queue.size(); 如果直接 for (int i = 0; i < queue.size(); i++) 会怎么样？ 问：为什么 Python 可以直接写 for i in range(len(queue)) ？
* Binary Tree Serialization (M+Y); 问：什么是序列化？
  * 将“内存”中结构化的数据变成“字符串”的过程
  * 序列化：object to string
  * 反序列化：string to object
* 什么时候需要序列化？
  * 将内存中的数据持久化存储时; 内存中重要的数据不能只是呆在内存里，这样断电就没有了，所需需要用一种方式写入硬盘，在需要
的时候，能否再从硬盘中读出来在内存中重新创建
  * 网络传输时; 机器与机器之间交换数据的时候，不可能互相去读对方的内存。只能讲数据变成字符流数据（字符串）后通过网络传输过去。接受的一方再将字符串解析后到内存中。
  * 常用的一些序列化手段：XML, Json, Thrift (by Facebook), ProtoBuf (by Google)
* 序列化算法
  * 一些序列化的例子：
  * 比如一个数组，里面都是整数，我们可以简单的序列化为”[1,2,3]”
  * 一个整数链表，我们可以序列化为，”1->2->3”
  * 一个哈希表(HashMap)，我们可以序列化为，”{\”key\”: \”value\”}”
  * 序列化算法设计时需要考虑的因素：
  * 压缩率。对于网络传输和磁盘存储而言，当然希望更节省。如 Thrift, ProtoBuf 都是为了更快的传输数据和节省存储空间而设计的。
  * 可读性。我们希望开发人员，能够通过序列化后的数据直接看懂原始数据是什么。如 Json，LintCode 的输入数据
* 二叉树如何序列化？
  * 你可以使用任何你想要用的方法进行序列化，只要保证能够解析回来即可。LintCode 采用的是 BFS 的方式对二叉树数据进行序列化，这样的好处是，你可以更为容易的自己画出整棵二叉树。
  * 算法描述：http://www.lintcode.com/en/help/binary-tree-representation/
  * 题目及解答：http://www.lintcode.com/en/problem/binary-tree-serialization/ ; http://www.jiuzhang.com/solutions/binary-tree-serialization/
* 相关问题 Related Problems
  * Binary Tree Level Order Traversal II
  * http://www.lintcode.com/en/problem/binary-tree-level-order-traversal-ii/
  * http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal-ii/
  * Binary Tree Zigzag Order Traversal
  * http://www.lintcode.com/en/problem/binary-tree-zigzag-level-order-traversal/
  * http://www.jiuzhang.com/solutions/binary-tree-zigzag-level-order-traversal/
  * Convert Binary Tree to Linked Lists by Depth
  * http://www.lintcode.com/en/problem/convert-binary-tree-to-linked-lists-by-depth/
  * http://www.jiuzhang.com/solutions/convert-binary-tree-to-linked-lists-by-depth/
* 图上的宽度优先搜索, BFS in Graph; 问：和树上有什么区别？
* 哈希表: 图中存在环, 存在环意味着，同一个节点可能重复进入队列; Java: HashMap / HashSet; C++: unordered_map / unordered_set; Python: dict / set
  * Clone Graph (F); 图的遍历（由点及面）
  * http://www.lintcode.com/problem/clone-graph/
  * http://www.jiuzhang.com/solutions/clone-graph/
  * BFS 的时间复杂度; O(N + M); 其中 N 为点数，M 为边数
  * Word Ladder; 最典型的BFS问题 —— 隐式图 (Implicit Graph) 最短路径
  * http://www.lintcode.com/problem/word-ladder/
  * http://www.jiuzhang.com/solution/word-ladder/
* 矩阵中的宽度优先搜索, BFS in Matrix
* 矩阵 vs 图
  * 图 Graph, N个点，M条边, M最大是 O(N^2) 的级别, 图上BFS时间复杂度 = O(N + M); 说是O(M)问题也不大，因为M一般都比N大; 所以最坏情况可能是 O(N^2)
  * 矩阵 Matrix, R行C列, R*C个点，R*C*2 条边（每个点上下左右4条边，每条边被2个点共享）; 矩阵中BFS时间复杂度 = O(R * C)
* Number of Islands
  * http://www.lintcode.com/problem/number-of-islands/
  * http://www.jiuzhang.com/solutions/number-of-islands/
  * 图的遍历（由点及面）
* 坐标变换数组
  * int[] deltaX = {1,0,0,-1};
  * int[] deltaY = {0,1,-1,0};
  * 问：写出八个方向的坐标变换数组？
* 更多 Union Find 有关的问题, 将在《九章算法强化班》中讲解, 并查集 Union Find
* Knight Shortest Path
  * http://www.lintcode.com/problem/knight-shortest-path/
  * http://www.jiuzhang.com/solutions/knight-shortest-path/
  * 简单图最短路径
  * follow up: speed up?（见随课教程）
* 拓扑排序 Topological Sorting; 几乎每个公司都有一道拓扑排序的面试题！ BFS or DFS?
  * 独孤九剑——破剑式: 能够用 BFS 解决的问题，一定不要用 DFS 去做！因为用 Recursion 实现的 DFS 可能造成 StackOverflow! (Iteration 的 DFS 一来你不会写，二来面试官也看不懂)
  * 入度（In-degree）： 有向图（Directed Graph）中指向当前节点的点的个数（或指向当前节点的边的条数）
  * 算法描述：
  * 1. 统计每个点的入度
  * 2. 将每个入度为 0 的点放入队列（Queue）中作为起始节点
  * 3. 不断从队列中拿出一个点，去掉这个点的所有连边（指向其他点的边），其他点的相应的入度 - 1
  * 4. 一旦发现新的入度为 0 的点，丢回队列中
  * 拓扑排序并不是传统的排序算法; 一个图可能存在多个拓扑序（Topological Order），也可能不存在任何拓扑序
  
  
