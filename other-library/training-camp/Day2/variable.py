# 变量（variable）
name = "hello"
print(name)
name = "hello python"
print(name)
message = "Hello Python Crash Course reader!"
print(message)

#2-8 数字8：编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。为使用print语
# 句来显示结果，务必将这些表达式用括号括起来，也就是说，你应该编写4行类似于下面的代码：
# print(5 + 3)
# 输出应为4行，其中每行都只包含数字8。
print(1+7)
print(9-1)
print(2*4)
print(int(16/2))

# 2-9 最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，
# 然后将这条消息打印出来。
favorite_number = 9
print("My favorite number is " + str(favorite_number))

# 2-10 添加注释：选择你编写的两个程序，在每个程序中都至少添加一条注释。如果程序太简单，实在没有什么需要说明
# 的，就在程序文件开头加上你的姓名和当前日期，再用一句话阐述程序的功能。
'''
@Description: 学习变量
@Author: huqi
@GitHub: https://github.com/hu-qi
@Email: me@huqi.me
@Date: 2019-06-11 19:49:17
@LastEditors: huqi
@LastEditTime: 2019-06-12 19:57:02
'''
# 输出hello world
print("Hello World!")

# 2-11 Python 之禅：在 Python 终端会话中执行命令import this，并粗略地浏览一下其他的指导原则。
import this
import codecs
print("Python 之禅")
codecs.encode(this.s, 'rot13')
