# Leetcode-Python
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
* lintcode 练习
  * 479 second max of array
  * 478 simple calculator
  * 283 max of 3 numbers
  * 145 lowercase to uppercase
  * 37 reverse 3-digit integer
  * 9 fizz buzz
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
  * 什么是链表（linked list）? -> 由节点构成的列表, 线性的数据结构
  * class ListNode:
  *     def __init__(self, value):
  *         self.val = value
  *         self.next = None
  * 基于ListNode实现一个Linked List:  see attached code above...
  * 不得不提的dummy Node：伟大的哨兵节点：dummyNode-> null; 作用（前驱节点的重要性）：使得每一个元素都有前驱节点
  * 链表的操作: 遍历（traverse）; 插入（insert）; 查找（find）; 删除（delete）
  * LinkedList Class的接口：1 读取操作 get(location) // 获取location位置上的node的value
  * LinkedList Class的接口：2 查找操作 contains(val) // 判断链表中是否含有val值的node
  * LinkedList Class的接口：3 插入操作 add(location, val) // 在location的位置上插入一个值为val的node
  * LinkedList Class的接口：4 删除操作 remove(location) // 删除location位置上的元素
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
  * Python提供的Queue模块：Python中队列是线程间最常用的交换数据的方式
  
  
   
  
  
  
