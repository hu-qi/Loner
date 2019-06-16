height = input("How tall are you, in inches? ")
if height.isdigit():
  height =  int(height)
  if height >= 36:
    print("\nYou're tall enough to ride!")
  else:
      print("\nYou'll be able to ride when you're a little older.")
else:
  print('Sorry, your input error!')

