capitals = {"France": "Paris",
            "Germany": "Berlin", 
            "Italy": "Rome",
            "Spain": "Madrid",
            "United Kingdom": "London"}

# print(capitals["France"])  # Output: Paris
# print(capitals["Germany"])  # Output: Berlin
# print(capitals["Italy"])  # Output: Rome
# print(capitals["Spain"])  # Output: Madrid
# print(capitals["United Kingdom"])  # Output: London

# print(capitals.get("France"))  # Output: Paris
# print(capitals.get("Spain")) 

# if(capitals.get("japan")):
#     print("capital exits")
# else :
#     print("oops wrong choice")    

# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# print(keys)

# for keys in capitals.keys():
#     print (keys)

# values = capitals.values()
# print(values)

# items = capitals.items()
# print(items)


for key, value in capitals.items():
    print (f"{key},{value}")