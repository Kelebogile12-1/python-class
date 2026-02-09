# Correct Code

name = "Kabelo"         
age = "23"
print("My name is " + name + " and I am " + age + " years old")

age = 17
if age >= 18:           
    print("Adult")
else:                   
    print("Minor")

greeting = "hello CodeTribers"
print(greeting.swapcase())   

fruits = ["Apple", "Orange", "Banana"]
fruits.append("Mango")       
print(fruits)

for i in range(1, 5):        
    print(i)

# Check if number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:            
    print("Even number")
else:
    print("Odd number")

# File writing section
file = open("data.txt", "w")
file.write("Python is fun")
file.close()                 # Call close() method

# Check Age for Voting
age = int(input("Enter your age: "))   # Convert input to int
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
