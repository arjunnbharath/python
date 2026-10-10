# # test file input

# text = "hi i am an arjun nlkj"
# employees=["arjun" , "jacob" , "henry"]

# file_path = "ouput.txt"
# try :
#     with open(file_path,"a") as file:
#         for employee in employees:
#             file.write(employee)
#         # file.write(text)
#         print("file created ")
# except FileExistsError :
#     print("file exits")


# #json file input 
# import json
# dictionary ={

#     "name" : "arjun",
#     "age" : 20 ,
#     "job" : "SWE"
# }

# file_path ="json_output.json"

# try :
#     with open(file_path,"w") as file :
#         json.dump(dictionary, file , indent=4) #indent == we use this to give space
#         print("file created ")
# except FileExistsError :
#     print("FILE ALREADY EXITS")

# # CSV file input 

# import json
# import csv

# employee =[["name","age","job"],
#            ["Arjun",25,"SWE"],
#            ["Athul",23,"QA"],
#            ["Henry",37,"dev1"]]

# file_path = "csv_output.csv"
# try :
#     with open(file_path,"w",newline="")as file :
#         writer = csv.writer(file)
#         for row in employee:
#             writer.writerow(row)
#         print("FILE CREATED")
# except FileExistsError :
#     print("FILE ALREADY EXITS")


