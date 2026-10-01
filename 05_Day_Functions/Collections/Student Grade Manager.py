students = {}

def add_student():
    student = input("Enter the name of student: ")
    student= student.capitalize()
    python = int(input("Enter Python marks: "))
    sql = int(input("Enter SQL marks: "))
    ai = int(input("Enter AI marks: "))

    students[student]={
        "PYTHON" : python ,
        "SQL" : sql ,
        "AI" : ai
    }

def view_student() :
    for student in students :
        print(student)

while True:
    print("=" * 31)
    print("     STUDENT GRADE MANAGER")
    print("=" * 31)
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Show class average")
    print("5. Show top student")
    print("6. Show all subjects")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    if choice == "2":
        view_student()

    elif choice == "7":
        break