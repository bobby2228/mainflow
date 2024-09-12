# Initialize an empty dictionary to store grades
student_grades = {}

# Function to add a grade to the dictionary
def add_grade(student_grades, student, grade):
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

# Function to calculate the average grade
def calculate_average(student_grades):
    total_grades = 0
    num_students = 0
    for students in student_grades.values():
        total_grades += sum(students)
        num_students += len(students)
    return total_grades / num_students

# List of students
students = ['Alice', 'Bob', 'Charlie']

# Loop to input grades for each student
for student in students:
    while True:
        try:
            # Input grade for the student
            grade_str = input(f"Enter grade for {student}: ")
            grade = float(grade_str)
            
            # Add grade to the dictionary
            add_grade(student_grades, student, grade)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Calculate and print the average grade
average = calculate_average(student_grades)
print(f"Student Grades: {student_grades}")
print(f"Average Grade: {average:.2f}")