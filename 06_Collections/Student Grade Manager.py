students = {}


def add_student():
    student = input("Enter the name of student: ")
    student = student.capitalize()

    python = int(input("Enter Python marks: "))
    sql = int(input("Enter SQL marks: "))
    ai = int(input("Enter AI marks: "))

    students[student] = {
        "PYTHON": python,
        "SQL": sql,
        "AI": ai
    }


def view_student():
    print("=" * 31)
    print("     LIST OF STUDENTS")
    print("=" * 31)

    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)


def search_student():
    student = input("Enter student name: ")
    student = student.capitalize()

    if student in students:
        print("=" * 31)
        print("       STUDENT DETAILS")
        print("=" * 31)

        print("Name:", student)
        print("Python:", students[student]["PYTHON"])
        print("SQL:", students[student]["SQL"])
        print("AI:", students[student]["AI"])

    else:
        print("Student not found.")


def class_avg():
    total = 0
    count = 0

    for student in students:
        for subject in students[student]:
            total += students[student][subject]
            count += 1

    if count == 0:
        print("No marks available.")
    else:
        average = total / count
        print(f"Class average: {average:.2f}")


def top_student():
    if not students:
        print("No students found.")
        return

    top_name = ""
    top_average = 0

    for student in students:
        marks = students[student]

        average = (
            marks["PYTHON"] +
            marks["SQL"] +
            marks["AI"]
        ) / 3

        if average > top_average:
            top_average = average
            top_name = student

    print("=" * 31)
    print("        TOP STUDENT")
    print("=" * 31)
    print("Name:", top_name)
    print(f"Average: {top_average:.2f}")


def all_subjects():
    subjects = set()

    for student in students:
        for subject in students[student]:
            subjects.add(subject)

    print("=" * 31)
    print("        ALL SUBJECTS")
    print("=" * 31)

    if subjects:
        for subject in subjects:
            print(subject)
    else:
        print("No subjects available.")


while True:

    print()
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

    elif choice == "2":
        view_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        class_avg()

    elif choice == "5":
        top_student()

    elif choice == "6":
        all_subjects()

    elif choice == "7":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice. Please try again.")