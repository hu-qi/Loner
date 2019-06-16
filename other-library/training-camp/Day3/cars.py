cars = ['bmw', 'audi', 'benz', 'beijing']
cars.sort() # 反序传入reverse=True
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'benz', 'beijing']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)
print(len(cars))