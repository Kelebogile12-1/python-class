# A function is a block of code that perform a specific task
# It only runs when you call it

def greet(): #def-keyword used to define a function
    print ("Hello,welcome to Python")

    #call the function
def greetings(name):
    #print ("Hello",name)
        print(f'Hello{name}')

# function to add numbers 
def getSum(x,y):
        z=x+y
        return z
# function to subtract two numbers
def subtract(x, y):
    return x - y

    
total = getSum(30,70)
difference = subtract(70, 30)

print(total)
print("Difference:", difference)

greetings("Kele")
greet()
    

    