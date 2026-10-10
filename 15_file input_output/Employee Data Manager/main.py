import json
file_path ="employee.json"

def load_employee() :
    try:
        with open (file_path ,"r") as file :
          return json.load(file)
    except FileNotFoundError :
        print("file didnt existes") 
        return []   


def save_employees(employees):
    with open(file_path, "w") as file:
        json.dump(employees, file, indent=4)

def add_employee():
    employees = load_employee()

    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    job = input("Enter job title: ")
    salary = float(input("Enter salary: "))

    employee = {
        "name": name,
        "age": age,
        "job": job,
        "salary": salary
    }

    employees.append(employee)
    save_employees(employees)

    print("Employee added successfully!")


def view_employees():
    employees = load_employee()

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(employee)

def search_employees():
    employees = load_employee()

    name= input("Enter the name of employee : ")
    for employee in employees :
     if employee["name"].lower() == name.lower():

            print("\nEmployee found!")
            print("Name:", employee["name"])
            print("Age:", employee["age"])
            print("Job:", employee["job"])
            print("Salary:", employee["salary"])

            return

    print("Employee not found.")
    
def delete_employees():
    employees = load_employee()
    name= input("Enter the name of employee : ")
    for employee in employees :
        if employee["name"].lower() == name.lower():

         employees.remove(employee)
         save_employees(employee)
         print("done")
def main():

    while True:
        print("\n--- Employee Manager ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("5. Delete employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employees()

        elif choice == "4":
            delete_employees()
        
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

main()