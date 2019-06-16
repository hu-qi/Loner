# 制表符 换行符
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白 lstrip() rstrip() strip()
favorite_language = 'python'
second_language  = ' Javascript '
third_language  = 'Java'
print(favorite_language + "" + second_language + ""+ third_language)
print(favorite_language + "" + second_language.lstrip() + ""+ third_language)
print(favorite_language + "" + second_language.rstrip() + ""+ third_language)
print(favorite_language + "" + second_language.strip() + ""+ third_language)