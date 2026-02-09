
#Ask the user to enter two numbers.
num1 = float (input ("Enter the first number"))
num2 = float (input ("Enter the second number"))

operation = input("Enter an operation(+,-,x,/)")
if operation == '+':
  #Addition 
    result = num1 + num2
    print(f"The result of {num1} + {num2} = {result}")

elif operation == '-':
  #Subtration
    result = num2 - num1
    print(f"The result of {num2} - {num1} = {result}")

elif operation == '*':
  #Multiplication
    result = num1 * num2
    print(f"The result of {num1} * {num2} = {result}")

elif operation == '/':
  #Division
    if num2 != 0:
      result = num2 / num1 
    print(f"The result of {num2} / {num1} = {result}")

   # Handle division by zero error 
else:
    print("Error: Division by zero is not allowed.")
  
