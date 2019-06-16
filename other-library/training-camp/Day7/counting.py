current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

current_number = 0
array = []
while current_number < 1000:
  current_number += 1
  if current_number%2 == 0:
    continue
  array.append(current_number)
print(array)

x = 1
while x <= 5:
    print(x)
    x += 1 # 如果这行没有 while一直循环执行