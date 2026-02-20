  # Student Information & Grade Evaluation1

# Function to calculate the grade based on average marks
def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "E"

# Function to add a student
def add_student(students):
    name = input("Enter student's name: ")
    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    # Calculate average and grade
    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    # Store the student's information
    students[name] = {"Marks": marks, "Average": average, "Grade": grade}
    print(f"\n{name}'s data has been added successfully!\n")

# Function to view all students
def view_students(students):
    if not students:
        print("\nNo students available.\n")
    else:
        print("\n--- Student Records ---")
        for name, info in students.items():
            print(f"Name: {name}")
            print(f"Marks: {info['Marks']}")
            print(f"Average: {info['Average']:.2f}")
            print(f"Grade: {info['Grade']}\n")

# Function to display the menu
def display_menu():
    print("Student Information & Grade Evaluation")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

def main():
    students = {}  # Dictionary to store student records

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
