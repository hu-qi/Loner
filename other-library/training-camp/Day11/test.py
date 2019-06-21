# 11-1 城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回
# 一个格式为City, Country的字符串，如Santiago, Chile。将这个函数存储在一个名为 
# city_functions.py 的模块中。

# 创建一个名为 test_cities.py 的程序，对刚编写的函数进行测试（别忘了，你需要导入模块
# unittest以及要测试的函数）。编写一个名为test_city_country()的方法，核实使用类似于
# 'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。运行
# test_cities.py，确认测试test_city_country()通过了。



# 11-2 人口数量：修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格
# 式为City,Country-population xxx的字符串，如Santiago,Chile-population 5000000。
# 运行 test_cities.py，确认测试test_city_country()未通过。

# 修改上述函数，将形参population设置为可选的。再次运行 test_cities.py，确认测试
# test_city_country()又通过了。

# 再编写一个名为test_city_country_population()的测试，核实可以使用类似于'santiago'、
# 'chile'和'population=5000000'这样的值来调用这个函数。再次运行 test_cities.py，
# 确认测试test_city_country_population()通过了。