correct_pin = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("Access Granted!")
        break
    else:
        attempts = attempts + 1
        print("Wrong PIN!")

if attempts == max_attempts:
    print("Account Locked!")