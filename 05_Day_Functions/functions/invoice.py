def invoice(username, amount, exp_date):
    print("\n" + "=" * 40)
    print("            INVOICE")
    print("=" * 40)

    print(f"Customer Name : {username}")
    print(f"Amount Due    : ₹{amount:.2f}")
    print(f"Due Date      : {exp_date}")

    print("-" * 40)
    print(f"Total         : ₹{amount:.2f}")
    print("=" * 40)
    print("Thank you for your business!")
    print("=" * 40)


invoice("Arjun", 2500.50, "30-09-2026")