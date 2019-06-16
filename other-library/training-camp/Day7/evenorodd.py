number = input("Enter a number, and I'll tell you if it's even or odd: ")
if number.isdigit():
  number =  int(number)
  if number % 2 == 0:
      print("\nThe number " + str(number) + " is even.")
  else:
      print("\nThe number " + str(number) + " is odd.")
else:
  print('Sorry, your input error!')