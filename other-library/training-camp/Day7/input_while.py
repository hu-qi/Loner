# 7-1 汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me 
# see if I can find you a Subaru”。
car = input("Let me see if what can  I find you?")
print("Let me see if I can find you a %s"%car)

# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出
# 没有空桌；否则指出有空桌。
number = input('How many people eat?')
if number.isdigit():
  number = int(number)
  if number > 8:
    print('Sorry, there is no empty table.')
  else:
    print('Congratulations, there is an empty table here.')
else:
  print('Sorry, please enter the number')



# 7-3 10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍。
number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
if number.isdigit():
  number = int(number)
  if number%10 == 0:
    print('%s is a multiple of 10'%number)
  else:
    print("%s isn't a multiple of 10"%number)
else:
  print('Sorry, please enter the number')

# 7-4 比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时
# 结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
prompt = "Please input the ingredient of the pizza.Thank you!"
prompt += "\nEnter 'quit' to end the program. "
while True:
  name = input(prompt)
  if name == 'quit':
    break
  else:
    print("The " + str(name) + ' have been added! ')

# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的
# 观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指
# 出其票价。
prompt = "Please input the age of the audience.Thank you!"
prompt += "\nEnter 'quit' to end the program. "
while True:
  age = input(prompt)
  if age == 'quit':
    break
  if not age.isdigit():
    print('Please enter the number')
    continue
  elif int(age) < 3:
    print("The price of you is free.")
  elif 3 <= int(age) <12:
    print("The price of you is $10.")
  elif 12 <= int(age) :
    print("The price of you is $15.")


# 7-6 三个出口：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
# 在while循环中使用条件测试来结束循环。
# 使用变量active来控制循环结束的时机。
# 使用break语句在用户输入'quit'时退出循环。
flag = True
while flag:
  age = input(prompt)
  if age == 'quit':
    flag = False
  if not age.isdigit():
    print('Please enter the number')
    continue
  elif int(age) < 3:
    print("The price of you is free.")
  elif 3 <= int(age) <12:
    print("The price of you is $10.")
  elif 12 <= int(age) :
    print("The price of you is $15.")

# 7-7 无限循环：编写一个没完没了的循环，并运行它（要结束该循环，可按 Ctrl+C，也可关
# 闭显示输出的窗口）。
# while True:
  # print('I love you!')

# 7-8 熟食店：创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；再创建
# 一个名为finished_sandwiches的空列表。遍历列表sandwich_orders，对于其中的每种三明
# 治，都打印一条消息，如I made your tuna sandwich，并将其移到列表
# finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['Bacon', 'Lettuce', 'Tomato', 'Tuna']
finished_sandwiches = []
while sandwich_orders:
  finished_sandwich = sandwich_orders.pop()
  print('I made your %s sandwich'%str(finished_sandwich).lower())
  finished_sandwiches.append(finished_sandwich)
print(str(finished_sandwiches))
for finished_sandwich in finished_sandwiches:
  print(finished_sandwich.title()) 

# 7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习7-8而创建的列表sandwich_orders，
# 并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息，
# 指出熟食店的五香烟熏牛肉卖完了；再使用一个while循环将列表sandwich_orders中的
# 'pastrami'都删除。确认最终的列表finished_sandwiches中不包含'pastrami'。
sandwich_orders = ['Bacon', 'Lettuce', 'Tomato', 'Tuna', 'pastrami', 'pastrami', 'pastrami']
print("The pastrami has been sold.")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could 
# visit one place in the world, where would you go?”的提示，并编写一个打印调查结
# 果的代码块
place = []
print("If you could visit one place in the world, where would you go?")
flag = True
while flag:
  new_place = input("\n Please input the place?")
  place.append(new_place)
  repeat = input("Would you want to input another place?(Y/N)")
  if repeat == 'N':
    flag = False
for i in place:
  print("The %s you want to go."%i)