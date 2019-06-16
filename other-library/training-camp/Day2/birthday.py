age = 23 
# message = "Happy " + age + "rd Birthday!"  # TypeError can only concatenate str (not "int") to str
message = "Happy " + str(age) + "rd Birthday!" 
print(message)
