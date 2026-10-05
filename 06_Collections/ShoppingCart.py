# shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want to buy (q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("\n" + "-" * 15)
print("   YOUR CART")
print("-" * 15)

for food in foods:
    print(food, end=" ")

print()

for price in prices:
    total += price

print(f"Your total amount is: ${total}")