# 9-1 餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：
# restaurant_name和cuisine_type。创建一个名为describe_restaurant()
# 的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，
# 而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前
# 述两个方法。
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()



# 9-2 三家餐馆：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例
# 调用方法describe_restaurant()。
mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()


# 9-3 用户：创建一个名为User的类，其中包含属性first_name和last_name，
# 还有用户简介通常会存储的其他几个属性。在类User中定义一个名为
# describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('hu', 'qi', 'hogo', 'me@huqi.me', 'China')
willie.describe_user()
willie.greet_user()


# 9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，
# 并将其默认值设置为0。根据这个类创建一个名为restaurant的实例；打印有多少人在这
# 家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并
# 向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这
# 个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))


# 9-5 尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts
#  的属性。编写一个名为increment_login_attempts()的方法，它将属性login_attempts
# 的值加1。再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的
# 值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性
# login_attempts的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，
# 并再次打印属性login_attempts的值，确认它被重置为0。
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它
# 继承你为完成练习9-1或练习9-4而编写的Restaurant类。这两个版本的Restaurant类都可
# 以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的
# 冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调
# 用这个方法。
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()


# 9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习
# 9-3或练习9-5而编写的User类。添加一个名为privileges的属性，用于存储一个由字符串
# （如"can add post"、"can delete post"、"can ban user"等）组成的列表。编写一
# 个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用
# 这个方法。
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []
    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()


# 9-8 权限：编写一个名为Privileges的类，它只有一个属性——privileges，其中存储了
# 练习9-7所说的字符串列表。将方法show_privileges()移到这个类中。在Admin类中，
# 将一个Privileges实例用作其属性。创建一个Admin实例，并使用方法
# show_privileges()来显示其权限。
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()


# 9-9 电瓶升级：在本节最后一个 electric_car.py 版本中，给Battery类添加一个名为
# upgrade_battery()的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85
# 。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级
# 并再次调用get_range()。你会看到这辆汽车的续航里程增加了。
class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

# 9-10 导入Restaurant类：将最新的Restaurant类存储在一个模块中。在另一个文件中，
# 导入Restaurant类，创建一个Restaurant实例，并调用Restaurant的一个方法，以确
# 认import语句正确无误。
# restaurant.py:
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

# my_restaurant.py:
# from restaurant import Restaurant

# channel_club = Restaurant('the channel club', 'steak and seafood')
# channel_club.describe_restaurant()
# channel_club.open_restaurant()


# 9-11 导入Admin类：以为完成练习9-8而做的工作为基础，将User、Privileges和Admin
# 类存储在一个模块中，再创建一个文件，在其中创建一个Admin实例并对其调用方法
# show_privileges()，以确认一切都能正确地运行。
# user.py:
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])
  
class Privileges():
    def __init__(self, privileges):
        self.privilege = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)
# my_user.py:
# from user import Admin

# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()

# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
#     ]
# eric.privileges.privileges = eric_privileges

# print("\nThe admin " + eric.username + " has these privileges: ")
# eric.privileges.show_privileges()


# 9-12 多个模块：将User类存储在一个模块中，并将Privileges和Admin类存储在另一个
# 模块中。再创建一个文件，在其中创建一个Admin实例，并对其调用方法
# show_privileges()，以确认一切都依然能够正确地运行。
# user.py:
class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
# admin.py:
# from user import User


# class Admin(User):
#     def __init__(self, first_name, last_name, username, email, location):
#         """Initialize the admin."""
#         super().__init__(first_name, last_name, username, email, location)

#         # Initialize an empty set of privileges.
#         self.privileges = Privileges([])
    

# class Privileges():
#     def __init__(self, privileges):
#         self.privilege = privileges

#     def show_privileges(self):
#         for privilege in self.privileges:
#             print("- " + privilege)

# my_admin.py:
# from admin import Admin

# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()

# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
#     ]
# eric.privileges.privileges = eric_privileges

# print("\nThe admin " + eric.username + " has these privileges: ")
# eric.privileges.show_privileges()



# 9-13 使用OrderedDict：在练习6-4中，你使用了一个标准字典来表示词汇表。请使用
# OrderedDict类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的顺序一致。
from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)


# 9-14 骰子：模块random包含以各种方式生成随机数的函数，其中的randint()返回一个位
# 于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：
# from random import randint
# x = randint(1, 6)
# 请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。编写一个名为
# roll_die()的方法，它打印位于1和骰子面数之间的随机数。创建一个6面的骰子，再掷10次。
#  创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
from random import randint
x = randint(1, 6)
print(x)
x = randint(1, 6)
print(x)
x = randint(1, 6)
print(x)

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)


# 9-15 Python Module of the Week：要了解 Python 标准库，一个很不错的资源是网站 
# Python Module of the Week。请访问 http://pymotw.com/ 并查看其中的目录，
# 在其中找一个你感兴趣的模块进行探索，或阅读模块collections和random的文档。


""" Python 3 Module of the Week
PyMOTW-3 is a series of articles written by Doug Hellmann to demonstrate how to use the modules of the Python 3 standard library. It is based on the original PyMOTW series, which covered Python 2.7. See About Python Module of the Week for details including the version of Python and tools used.

Text
string — Text Constants and Templates
textwrap — Formatting Text Paragraphs
re — Regular Expressions
difflib — Compare Sequences
Data Structures
enum – Enumeration Type
collections — Container Data Types
array — Sequence of Fixed-type Data
heapq – Heap Sort Algorithm
bisect — Maintain Lists in Sorted Order
queue — Thread-Safe FIFO Implementation
struct — Binary Data Structures
weakref — Impermanent References to Objects
copy — Duplicate Objects
pprint — Pretty-Print Data Structures
Algorithms
functools — Tools for Manipulating Functions
itertools — Iterator Functions
operator — Functional Interface to Built-in Operators
contextlib — Context Manager Utilities
Dates and Times
time — Clock Time
datetime — Date and Time Value Manipulation
calendar — Work with Dates
Mathematics
decimal — Fixed and Floating Point Math
fractions — Rational Numbers
random — Pseudorandom Number Generators
math — Mathematical Functions
statistics — Statistical Calculations
The File System
os.path — Platform-independent Manipulation of Filenames
pathlib — Filesystem Paths as Objects
glob — Filename Pattern Matching
fnmatch — Unix-style Glob Pattern Matching
linecache — Read Text Files Efficiently
tempfile — Temporary File System Objects
shutil — High-level File Operations
filecmp — Compare Files
mmap — Memory-map Files
codecs — String Encoding and Decoding
io — Text, Binary, and Raw Stream I/O Tools
Data Persistence and Exchange
pickle — Object Serialization
shelve — Persistent Storage of Objects
dbm — Unix Key-Value Databases
sqlite3 — Embedded Relational Database
xml.etree.ElementTree — XML Manipulation API
csv — Comma-separated Value Files
Data Compression and Archiving
zlib — GNU zlib Compression
gzip — Read and Write GNU zip Files
bz2 — bzip2 Compression
tarfile — Tar Archive Access
zipfile — ZIP Archive Access
Cryptography
hashlib — Cryptographic Hashing
hmac — Cryptographic Message Signing and Verification
Concurrency with Processes, Threads, and Coroutines
subprocess — Spawning Additional Processes
signal — Asynchronous System Events
threading — Manage Concurrent Operations Within a Process
multiprocessing — Manage Processes Like Threads
asyncio — Asynchronous I/O, event loop, and concurrency tools
concurrent.futures — Manage Pools of Concurrent Tasks
Networking
ipaddress — Internet Addresses
socket — Network Communication
selectors — I/O Multiplexing Abstractions
select — Wait for I/O Efficiently
socketserver — Creating Network Servers
The Internet
urllib.parse — Split URLs into Components
urllib.request — Network Resource Access
urllib.robotparser — Internet Spider Access Control
base64 — Encode Binary Data with ASCII
http.server — Base Classes for Implementing Web Servers
http.cookies — HTTP Cookies
webbrowser — Displays web pages
uuid — Universally Unique Identifiers
json — JavaScript Object Notation
xmlrpc.client — Client Library for XML-RPC
xmlrpc.server — An XML-RPC server
Email
smtplib — Simple Mail Transfer Protocol Client
smtpd — Sample Mail Servers
mailbox — Manipulate Email Archives
imaplib — IMAP4 Client Library
Application Building Blocks
argparse — Command-Line Option and Argument Parsing
getopt — Command Line Option Parsing
readline — The GNU readline Library
getpass — Secure Password Prompt
cmd — Line-oriented Command Processors
shlex — Parse Shell-style Syntaxes
configparser — Work with Configuration Files
logging — Report Status, Error, and Informational Messages
fileinput — Command-Line Filter Framework
atexit — Program Shutdown Callbacks
sched — Timed Event Scheduler
Internationalization and Localization
gettext — Message Catalogs
locale — Cultural Localization API
Developer Tools
pydoc — Online Help for Modules
doctest — Testing Through Documentation
unittest — Automated Testing Framework
trace — Follow Program Flow
traceback — Exceptions and Stack Traces
cgitb — Detailed Traceback Reports
pdb — Interactive Debugger
profile and pstats — Performance Analysis
timeit — Time the execution of small bits of Python code.
tabnanny — Indentation validator
compileall — Byte-compile Source Files
pyclbr — Class Browser
venv — Create Virtual Environments
ensurepip — Install the Python Package Installer
Runtime Features
site — Site-wide Configuration
sys — System-specific Configuration
os — Portable access to operating system specific features
platform — System Version Information
resource — System Resource Management
gc — Garbage Collector
sysconfig — Interpreter Compile-time Configuration
Language Tools
warnings — Non-fatal Alerts
abc — Abstract Base Classes
dis — Python Bytecode Disassembler
inspect — Inspect Live Objects
Modules and Packages
importlib — Python’s Import Mechanism
pkgutil — Package Utilities
zipimport — Load Python Code from ZIP Archives
Unix-specific Services
pwd — Unix Password Database
grp — Unix Group Database
Porting Notes
References
New Modules
Renamed Modules
Removed Modules
Deprecated Modules
Summary of Changes to Modules
Outside of the Standard Library
Text
Algorithms
Dates and Times
Mathematics
Data Persistence and Exchange
Cryptography
Concurrency with Processes, Threads, and Coroutines
The Internet
Email
Application Building Blocks
Developer Tools
About Python Module of the Week
Subscribe
Tools
Translations and Other Versions
Copyright and Licensing """