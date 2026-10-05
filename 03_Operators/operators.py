# 1. Arithmetic Operators
a = 10
b = 3
print("---------------------------")
print("Arithmetic Operators")
print("---------------------------")

print(a + b)    # 13   addition
print(a - b)    # 7    subtraction
print(a * b)    # 30   multiplication
print(a / b)    # 3.333...  division — ALWAYS returns float
print(a // b)   # 3    floor division — drops decimal
print(a % b)    # 1    modulus — remainder
print(a ** b)   # 1000 exponent — a to the power b

print("---------------------------")

# 2. Comparison Operators
print("Comparison Operators")
print("---------------------------")
print(a == b)   # False  equal to
print(a != b)   # True   not equal to
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False

# 1. Take two numbers as input (convert to int)
# 2. Print results of all arithmetic operators between them
# 3. Check if the two numbers are equal using ==
# 4. Check if the first number is in a list you define, using 'in'
# 5. Bonus: demo the difference between == and is using two separate but equal-valued lists

# 1. Take two numbers as input (convert to int)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# 2. Print results of all arithmetic operators
print("\nArithmetic Operations:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Division, Floor Division, and Modulus cannot be performed (division by zero).")

print("Exponentiation:", num1 ** num2)

# 3. Check if the two numbers are equal using ==
print("\nEquality Check:")
print("num1 == num2:", num1 == num2)

# 4. Check if the first number is in a list
numbers = [5, 10, 15, 20, 25]
print("\nMembership Check:")
print(f"Is {num1} in {numbers}? ->", num1 in numbers)

# 5. Bonus: Difference between == and is
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("\nDifference between == and is:")
print("list1 == list2:", list1 == list2)  # Compares values
print("list1 is list2:", list1 is list2)  # Compares object identity