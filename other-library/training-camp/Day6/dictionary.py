# 6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包
# 含键first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。
person = {
  'first_name': 'Qi',
  'last_name': 'Qi',
  'age': 25,
  'city': "Maya"
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字
# 用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人
# 的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
favorite_number = {
  'Eason': 0,
  'Jay': 1,
  'Leslie': 2,
  'Jacky': 3,
  'Edison': 4,
}
print('Eason liked' + str(favorite_number['Eason']))
print('Jay liked' + str(favorite_number['Jay']))
print('Leslie liked' + str(favorite_number['Leslie']))
print('Jacky liked' + str(favorite_number['Jacky']))
print('Edison liked' + str(favorite_number['Edison']))

# 6-3 词汇表：Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
# 想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇
# 的含义；也可在一行打印词汇，再使用换行符（\n）插入一个空行，然后在下一行以缩进的方式打印
# 词汇的含义。
glossary = {
  'array': '''This module defines an object type which can efficiently represent
    an array of basic values: characters, integers, floating point
    numbers.  Arrays are sequence types and behave very much like lists,
    except that the type of objects stored in them is constrained.''',
  'string': '''A collection of string constants.''',
  'bool': '''Returns True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed''',
  'range': '''Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).''',
  'print': '''Prints the values to a stream, or to sys.stdout by default.''',
}
print(glossary['array'])
print(glossary['string'])
print(glossary['bool'])
print(glossary['range'])
print(glossary['print'])

# 6-4 词汇表2：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其
# 中的一系列print语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，再在词
# 汇表中添加5个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
for key, value in glossary.items():
  print(key,':',value)
glossary['int'] = '''Convert a number or string to an integer, or return 0 if no arguments
 are given.  If x is a number, return x.__int__().  For floating point
 numbers, this truncates towards zero.'''
 
for key, value in glossary.items():
  print(key,':',value)

# 6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能
# 是'nile': 'egypt'。
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
# 使用循环将该字典中每条河流的名字都打印出来。
# 使用循环将该字典包含的每个国家的名字都打印出来。
river = {
	'nile':'egypt',
	'yellow river':'china',
	'mississippi river':'north America'
}
for key,value in river.items():
	print("The %s runs through %s"%(key.title(),value.title()))


# 6-6 调查：在6.3.1节编写的程序 favorite_languages.py 中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phill':'python',
}
interviewer = ['jen','sarah','edward','phill','alice','bob']
for user in interviewer:
	if user in favorite_languages.items():
		print('%s thank you for your intend'%user)
	else:
		print('welcome to here %s'%user)

# 6-7 人：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都
# 存储在一个名为people的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
people = {
	'person1' : {
	'first_name':'HandSome',
	'last_name':'Girl',
	'age':21,
	'city':'Zhuhai',
	},
	'person2':{
	'first_name':'albert',
	'last_name':'einstein',
	'age':34,
	'city':'princeton'
	},
	'person3':{
	'first_name':'marie',
	'last_name':'curie',
	'age':36,
	'city':'paris'
	},
}
for key,value in people.items():
	print(key+":")
	for key1,value2 in value.items():
		print("\t %s:%s"%(key1,value))

# 6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，
# 包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列表中，再遍历该列表，
# 并将宠物的所有信息都打印出来。
cat = {'name':'kitty','owner':'lucy'}
dog = {'name':'Da Huang','owner':'nancy'}
rabbit = {'name':'little white','owner':'mary'}
pets = [cat,dog,rabbit]
for pet in pets:
	for key ,value in pet.items():
		print('%s:%s'%(key,value.title()))

# 6-9 喜欢的地方：创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用
# 作键；对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练习更有趣些，可让一些朋友
# 指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_palces = {
	'alice':['Maldives','Daocheng','Lijiang'],
	'nancy':['Lijiang','Maldives','Lasa'],
	'bob':['Daocheng','Bali']
}
for key,value in favorite_palces.items():
	print(key.title()+":")
	if len(value) > 0:
		for place in value:
			print("\t",place)


# 6-10 喜欢的数字：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然
# 后将每个人的名字及其喜欢的数字打印出来。
favorite_number = {
  'Eason': [0],
  'Jay': [1,2],
  'Leslie': [2],
  'Jacky': [3,3],
  'Edison': [9,5,2,7],
}
for k,v in favorite_number.items():
  print(k+ ':')
  if len(v) > 0 :
    for num in v:
      print('\t', num)

# 6-11 城市：创建一个名为cities的字典，其中将三个城市名用作键；对于每座城市，都创建
# 一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每
# 座城市的字典中，应包含country、population和fact等键。将每座城市的名字以及有关它
# 们的信息都打印出来。
cities = {
	'A':{
	'country':'china',
	'population':32100,
	'fact':'A'
	},
	'B':{
	'country':'england',
	'population':36464,
	'fact':'B'
	},
	'C':{
	'country':'america',
	'population':465487,
	'fact':'C'
	},
}
for key,value in cities.items():
	print(key,":")
	for key1,value1 in value.items():
		print("\t",key1,":",value1)


# 6-12 扩展：本章的示例足够复杂，可以以很多方式进行扩展了。请对本章的一个示例进行扩
# 展：添加键和值、调整程序要解决的问题或改进输出的格式。
for k,v in glossary.items():
  print('%s:%s'%(k,v))
