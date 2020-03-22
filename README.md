# Leetcode-Python
### Lession 1: Variable & Control flow
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
