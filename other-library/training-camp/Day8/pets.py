def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')

describe_pet(pet_name='harry', animal_type='hamster')

def describe_dog(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_dog(pet_name='willie')

describe_dog(pet_name='harry', animal_type='hamster')


# 一条名为 Willie 的小狗
describe_dog('willie')
describe_dog(pet_name='willie')

# 一只名为 Harry 的仓鼠
describe_dog('harry', 'hamster')
describe_dog(pet_name='harry', animal_type='hamster')
describe_dog(animal_type='hamster', pet_name='harry')

