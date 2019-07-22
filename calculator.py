#prompt the user to select the operator
print("please choose the operator from 1-4")
print("1 == +")
print("2 == -")
print("3 == *")
print("4 == /")

#promt the user to choose the operator
operator = input() 

# prompt the user for first number for choosen integer
print("Enter first number please for choosen integer")
firstNumber = input()

# prompt the user for second number for Addition
print("Please enter the second number")
secondNumber= input()

if (operator == 1):
  print(firstNumber+secondNumber)

elif (operator == 2):
  print(firstNumber-secondNumber)

elif (operator == 3):
  print(firstNumber*secondNumber)
  
elif (operator == 4):
  print(firstNumber/secondNumber)