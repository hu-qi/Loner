motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'  # 覆盖第0个
print(motorcycles) 

motorcycles.append('Niu')
print(motorcycles)

motorcycles.insert(0, 'Mijia')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.pop(0)
print(motorcycles)

motorcycles.remove('Niu')
print(motorcycles)

motorcycle = 'yamaha'
motorcycles.append(motorcycle)
print(motorcycles)
motorcycles.remove(motorcycle)
print(motorcycles)
