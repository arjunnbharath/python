def calculate_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + (units - 100) * 5
    else:
        bill = (100 * 3) + (100 * 5) + (units - 200) * 8

    return bill


def print_bill(name, units, total):
    print("\n----- ELECTRICITY BILL -----")
    print(f"Customer Name: {name}")
    print(f"Units Consumed: {units}")
    print(f"Total Bill: ₹{total:.2f}")


a = input("Enter your name: ")
b = int(input("Enter units consumed: "))

total = calculate_bill(b)

print_bill(a, b, total)