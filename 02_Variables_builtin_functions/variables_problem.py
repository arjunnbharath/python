# 1. Take user's name, age, and years of experience as input()
# 2. Convert age and experience to int
# 3. Print a formatted sentence using an f-string
# 4. Print the type of each converted variable
# 5. Bonus: use min()/max() to compare two numbers of your choice

name = input("enter your name :")
age = input("enter your age :")
exp = input("enter your experience :")

age = int(age)
exp=int(exp)

full = f" Hi I am {name} and my age is {age} ,I am having experience of {exp} years."
print(full)

# just example of min and max function.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Bigger:", max(a, b))
print("Smaller:", min(a, b))

# Swap two variables in one line, no temp variable
x = "first"
y = "second"
x,y=y,x
print(x, y)  # should print: second first