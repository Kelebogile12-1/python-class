#A module is basically a file containing a set of function to include in your application.
#PIP modules 
import math
import os
import datetime 
import random
import statistics

# Maths module
print(math.sqrt(64))
print(math.sqrt(12))
print(math.sqrt(92))
print(math.pi)

#OS module
#the module that let's Python interact wih your operating system .
#os.mkdir make directory 
#mkdir a function that creates a new folder in the specific loation

current_dir = os.getcwd()
print(f"Learner's current directory: {current_dir}")

home_dir = os.path.expanduser("~")
print(f"Learner's home directory: {home_dir}")

# Create and remove a folder for demonstration
folder_name = "Learner_Folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
os.rmdir(folder_name)
print(f"Removed folder: {folder_name}")



#Datetime module
today = datetime.date.today()
month = datetime .date.today().month
day = datetime.date.today().day
time = datetime.datetime.now().time()
print(today)
print(month)
print(day)
print(time)

#Random module
learners = ["Kele", "Tricia", "Naledi", "Theo", "Dora"]

learner_of_the_day = random.choice(learners)
print(f"Learner of the Day: {learner_of_the_day}")
quiz_score = random.randint(25, 50)
print(f"{learner_of_the_day}'s random quiz score: {quiz_score}")

# Work with a dataset
data = [23, 47, 69, 31, 89, 67, 45, 63, 90]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)
stdev_value = statistics.stdev(data)

print(f"Data: {data}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Standard Deviation: {stdev_value}")