
employees=["aaaa" , "ababa" , "deddd"]

file_path = "ouput.txt"
try :
    with open(file_path,"a") as file:
        for employee in employees:
            file.write(employee + " ")
        # file.write(text)
        print("file created ")
except FileExistsError :
    print("file exits")

with open (file_path, "r") as file:
    content = file.read()
    print(content)