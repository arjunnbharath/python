# ==============================
#        CALCULATOR FUNCTIONS
# ==============================

def add():
    try:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))

        answer = a + b
        print(f"Answer: {answer}")

    except ValueError:
        print("❌ Please enter numbers only.")

    except Exception:
        print("❌ Something went wrong.")

    finally:
        print("Calculation finished.")


def sub():
    try:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))

        answer = a - b
        print(f"Answer: {answer}")

    except ValueError:
        print("❌ Please enter numbers only.")

    except Exception:
        print("❌ Something went wrong.")

    finally:
        print("Calculation finished.")


def mul():
    try:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))

        answer = a * b
        print(f"Answer: {answer}")

    except ValueError:
        print("❌ Please enter numbers only.")

    except Exception:
        print("❌ Something went wrong.")

    finally:
        print("Calculation finished.")


def div():
    try:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))

        answer = a / b
        print(f"Answer: {answer}")

    except ValueError:
        print("❌ Please enter numbers only.")

    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")

    except Exception:
        print("❌ Something went wrong.")

    finally:
        print("Calculation finished.")


# ==============================
#        MAIN PROGRAM
# ==============================

print("=" * 25)
print("     SIMPLE CALCULATOR")
print("=" * 25)

while True:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        sub()

    elif choice == "3":
        mul()

    elif choice == "4":
        div()

    elif choice == "5":
        print("\nTHANK YOU! 👋")
        break

    else:
        print("❌ Invalid choice. Please select 1-5.")