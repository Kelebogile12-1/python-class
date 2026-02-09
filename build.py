# -----------------------------------------------------------
# Python Practical Assessment 3: Working with Built-in Modules
# Objective:
# - Demonstrate understanding of importing and using Python built-in modules:
#   math, os, datetime, random, and statistics
# -----------------------------------------------------------

# ========== IMPORTING REQUIRED MODULES ==========
import math
import os
import datetime
import random
import statistics

# ========== 1. MATH MODULE ==========
print("\n===== MATH MODULE =====")

# Calculate the area and circumference of a circle
radius = 7
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

print(f"Radius: {radius}")
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")

# Perform square root and factorial operations
number = 9
print(f"\nSquare root of {number}: {math.sqrt(number)}")
print(f"Factorial of {number}: {math.factorial(number)}")


# ========== 2. OS MODULE ==========
print("\n===== OS MODULE =====")

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# List all files and folders in the current directory
print("\nFiles and folders in the current directory:")
for item in os.listdir():
    print("-", item)


# ========== 3. DATETIME MODULE ==========
print("\n===== DATETIME MODULE =====")

# Get the current date and time
current_time = datetime.datetime.now()
print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Display a custom future date
future_date = current_time + datetime.timedelta(days=10)
print("Date 10 days from now:", future_date.strftime("%Y-%m-%d"))

# Extract year, month, and weekday
print(f"Year: {current_time.year}")
print(f"Month: {current_time.strftime('%B')}")
print(f"Weekday: {current_time.strftime('%A')}")


# ========== 4. RANDOM MODULE ==========
print("\n===== RANDOM MODULE =====")

# Generate random numbers
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# Randomly choose an item from a list
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
random_color = random.choice(colors)
print(f"Randomly selected color: {random_color}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")


# ========== 5. STATISTICS MODULE ==========
print("\n===== STATISTICS MODULE =====")

# Work with a dataset
data = [23, 45, 67, 23, 89, 45, 67, 23, 90]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
mode_value = statistics.mode(data)
stdev_value = statistics.stdev(data)

print(f"Data: {data}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Standard Deviation: {stdev_value}")

# -----------------------------------------------------------
print("\nAssessment complete! ✅")
# -----------------------------------------------------------
