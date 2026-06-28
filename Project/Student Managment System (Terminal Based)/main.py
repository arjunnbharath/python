import json
def load_students():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students_list):
    with open("students.json", "w") as f:
        json.dump(students_list, f)

students = load_students()

def display_students(students_list) :
    for student in students_list :
        print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

def avg_marks(students_list):
    if(len(students_list)==0):
        return 0
    else:
      total = 0
      for student in students_list:
        total = total + student['marks']
      avgmarks = total / len(students_list)
      return avgmarks

def add_student(students_list):
    name = input("Enter student name: ")

    try:
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))
    except ValueError:
        print("Invalid input. Age and marks should be integers.")
        return

    new_student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students_list.append(new_student)
    save_students(students_list)
    print(f"Student {name} added successfully")

def delete_student(students_list):
    name_to_delete = input("Enter name to delete: ")
    student_to_remove = None

    for student in students_list:
        if student['name'].lower() == name_to_delete.lower():
            student_to_remove =student

    if student_to_remove is not None:
        students_list.remove(student_to_remove)
        save_students(students_list)
        print(f"{name_to_delete} removed successfully")
    else:
        print("Student not found")



while True:
    print("===== Student Menu =====")
    print("1. Add student")
    print("2. Display all students")
    print("3. Show average marks")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        print(f"Average Marks: {avg_marks(students)}")
    elif choice =='4':
        delete_student(students)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")