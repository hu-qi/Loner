# 8-1 消息：编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的
# 是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print('I learned function!')
display_message()

# 8-2 喜欢的图书：编写一个名为favorite_book()的函数，其中包含一个名为title的形
# 参。这个函数打印一条消息，如One of my favorite books is Alice in Wonderland。
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print('One of my favorite books is %s'%title)
favorite_book('Alice in Wonderland')

# 8-3 T 恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到 T 恤上的字
# 样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数。
def make_shirt(size, word):
    print("The size of the shirt is "+ size + ". The word which you want to print is '"+ word + "'.")
make_shirt('M','Hello python!')
make_shirt(size='M', word='Hello python!')

# 8-4 大号 T 恤：修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love 
# Python”的大号 T 恤。调用这个函数来制作如下 T 恤：一件印有默认字样的大号 T 恤、
# 一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）。
def make_shirt(size = "xxl", word = "I love Python"):
    print("The size of the shirt is "+ size + ". The word which you want to print is '"+ word + "'.")
make_shirt()
make_shirt(size='M')
make_shirt(word='Hello python!')

# 8-5 城市：编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属
# 的国家。这个函数应打印一个简单的句子，如Reykjavik is in Iceland。给用于存储国家
# 的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
def describe_city(city,contry='Iceland'):
    print('%s is in %s'%(city,contry))
describe_city('Reykjavik')
describe_city('NowYork', 'American')
describe_city('Guangzhou', 'China')

# 8-6 城市名：编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这
# 个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 至少使用三个城市-国家对调用这个函数，并打印它返回的值。
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

# 8-7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应
# 接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同
# 专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时
# 指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定
# 专辑包含的歌曲数。
def make_album(artist, title):
    """构建包含有关专辑信息的字典."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)


# 8-8 用户的专辑：在为完成练习8-7编写的程序中，编写一个while循环，让用户输入一个专辑的
# 歌手和名称。获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。
# 在这个while循环中，务必要提供退出途径。
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")



# 8-9 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()
# 的函数，这个函数打印列表中每个魔术师的名字。
magicians = ['harry houdini', 'david blaine', 'teller']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
show_magicians(magicians)

# 8-10 了不起的魔术师：在你为完成练习8-9而编写的程序中，编写一个名为make_great()
# 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。调用函
# 数show_magicians()，确认魔术师列表确实变了。
def make_great(magicians):
    """在每个魔术师后面添加'the Great!'"""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

make_great(magicians)
show_magicians(magicians)


# 8-11 不变的魔术师：修改你为完成练习8-10而编写的程序，在调用函数make_great()时，
# 向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后的列表，并将其存储到
# 另一个列表中。分别使用这两个列表来调用show_magicians()，确认一个列表包含的是原
# 来的魔术师名字，而另一个列表包含的是添加了字样“the Great”的魔术师名字。
def make_great(magicians):
    """在每个魔术师后面添加'the Great!'"""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians
print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)

# 8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个
# 形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
# 调用这个函数三次，每次都提供不同数量的实参。
def make_sandwich(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')


# 8-13 用户简介：复制前面的程序 user_profile.py，在其中调用build_profile()来创建有
# 关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Qi', 'Wei',
                             location='Beijing',
                             field='physics',
                             sex='man')
print(user_profile)

# 8-14 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和
# 型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，以及两个名称
# —值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)


# 8-15 打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_functions.py 的文
# 件中；在 print_models.py 的开头编写一条import语句，并修改这个文件以使用导入的函数。

# printing_functions.py:
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#printing_models.py:
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)


# 8-16 导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。在主程序文件
# 中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


# 8-17 函数编写指南：选择你在本章中编写的三个程序，确保它们遵循了本节介绍的函数编写指南。