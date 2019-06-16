# 5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# 详细研究实际结果，直到你明白了它为何为True或False。
# 创建至少10个测试，且其中结果分别为True和False的测试都至少有5个。
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

num = 0
print("\nIs num == 0? I predict True.")
print(num == 0)
print("Is num == '0'? I predict False.")
print(num == '0')

boolean = False
print("\nIs boolean == False? I predict True.")
print(boolean == False)
print("Is boolean == True? I predict False.")
print(boolean == True)

boolean = 'False'
print("\nIs boolean == 'False'? I predict True.")
print(boolean == 'False')
print("Is boolean == True? I predict False.")
print(boolean == False)

boolean = 'True'
print("\nIs boolean == 'True'? I predict True.")
print(boolean == 'True')
print("Is boolean == True? I predict False.")
print(boolean == True)

myList = [0, 1, 2]
print("\nIs myList == [0,1,2]? I predict True.")
print(myList == [0, 1, 2])
print("Is myList == '[0,1,2]'? I predict False.")
print(myList == '[0, 1, 2]')

myList = []
print("\nIs myList == []? I predict True.")
print(myList == [])
print("Is myList == ''? I predict False.")
print(myList == '')

# 5-2 更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到 conditional_tests.py 中。对于下面列出的各种测试，至少编写一个结果为True和False的测试。
# 检查两个字符串相等和不等。
# 使用函数lower()的测试。
# 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
# 使用关键字and和or的测试。
# 测试特定的值是否包含在列表中。
# 测试特定的值是否未包含在列表中。
print('\nx' == 'x')
print('x' == 'X')
print('x' == 'X'.lower())
q = 1
w = 3
print(q > w , q < w , q == w , q != w , q >= w , q <= w)
print(q >= 1 and w >= 4)
print(q >= 1 or w >= 4)

numbers = [1,2,3,4,5,6,7]
print(2 in numbers)
print(7 not in numbers)


# 5-3 外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，并将其设置为'green'、'yellow'或 'red'。
# 编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
alien_color = 'green'
if alien_color == 'green':
  print('You got 5 points!')

if alien_color == 'red':
  print('You got 5 points!')


# 5-4 外星人颜色#2：像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
# 编写这个程序的两个版本，在一个版本中执行if代码块，而在另一个版本中执行else代码块。
alien_color = 'green'
if alien_color == 'green':
  print('You got 5 points!')
else:
  print('You got 10 points!')

# 5-5 外星人颜色#3：将练习5-4中的if-else结构改为if-elif-else结构。
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
# 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
alien_color = 'green'
if alien_color == 'green':
  print('You got 5 points!')
elif alien_color =='yellow':
  print('You got 10 points!')
elif alien_color =='red':
  print('You got 15 points!')


# 5-6 人生的不同阶段：设置变量age的值，再编写一个if-elif-else结构，根据age的值判断处于人生的哪个阶段。
# 如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
# 如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
# 如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
# 如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
# 如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
# 如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
age = 23
if age < 2:
  print('baby')
elif age < 4:
  print('bigbaby')
elif age < 13:
  print('child')
elif age < 20:
  print('teenager')
elif age < 65:
  print('adult')
else:
  print('oldman')

# 5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，检查列表中是否包含特定的水果。
# 将该列表命名为favorite_fruits，并在其中包含三种水果。
# 编写5条if语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。
favorite_fruits = ['apple','banana','pear']
if 'apple' not in favorite_fruits:
  print('You really like apple')
elif 'banana' in favorite_fruits:
  print('You really like banana')
elif 'pear' in favorite_fruits:
  print('You really like pear')

# 5-8 以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
# 如果用户名为'admin'，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。
# 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
users = ['aa','bb','cc','dd','admin']
for user in users:
  if user == 'admin':
    print('Hello ' + user.title() + ',would you like to see a status report?')
  else:
    print('Hello ' + user.title() + ',thank you for logging in again?')

# 5-9 处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if语句，检查用户名列表是否为空。
# 如果为空，就打印消息“We need to find some users!”。
# 删除列表中的所有用户名，确定将打印正确的消息。
users = []
if users == []:
  print('We need to find some users!')

# 5-10 检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
# 创建一个至少包含5个用户名的列表，并将其命名为current_users。
# 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
# 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
# 确保比较时不区分大小写；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。
current_users = ['aa','bb','cc','dd','ee']
new_users = ['ff','gg','bb','CC','zz']
for new_user in new_users:
  if new_user.lower() in current_users:
    print(new_user + ' has been used.')
  else:
    print(new_user + ' has not been used.')

# 5-11 序数：序数表示位置，如 1st 和 2nd。大多数序数都以 th 结尾，只有1、2和3例外。
# 在一个列表中存储数字1~9。
# 遍历这个列表。
# 在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为1st、2nd、3rd、4th、5th、6th、7th、8th和9th，但每个序数都独占一行。
numbers = list(range(1,10))
for number in numbers:
  if number == 1:
    print("\n1st")
  elif number == 2:
    print('2nd')
  elif number == 3:
    print('3rd')
  else:
    print('%sth'%number)

# 5-12 设置if语句的格式：审核你在本章编写的程序，确保正确地设置了条件测试的格式。
# 感觉代码还是不规范 

# 5-13 自己的想法：与刚拿起本书时相比，现在你是一名能力更强的程序员了。鉴于你对如何在程序中模拟现实情形有了更深入的认识，
# 你可以考虑使用程序来解决一些问题。随着编程技能不断提高，你可能想解决一些问题，请将这方面的想法记录下来。想想你可能想编
# 写的游戏、想研究的数据集以及想创建的 Web 应用程序。
# 打飞机、大数据、人才库