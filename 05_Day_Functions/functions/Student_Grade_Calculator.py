def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        g = "A"
    elif marks >= 80 and marks <= 89:
        g = "B"
    elif marks >= 70 and marks <= 79:
        g = "C"
    elif marks >= 60 and marks <= 69:
        g = "D"
    else:
        g = "F"

    return g

def report(name,mark,grade):
    print("----- STUDENT REPORT -----")
    print(f"Student Name: {name}")
    print(f"Marks: {mark}")
    print(f"Grade: {grade}")
    print("--------------------------")    

a=input("Enter Student Name : ")
mark=int(input("Enter Student Mark : "))

std_grade=calculate_grade(mark)

report(a,mark,std_grade)
