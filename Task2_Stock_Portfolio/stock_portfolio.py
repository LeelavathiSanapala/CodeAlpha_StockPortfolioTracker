# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")

while True:
    print("\n1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter stock name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per share: "))

        investment = quantity * price

        portfolio[name] = {
            "quantity": quantity,
            "price": price,
            "investment": investment
        }

        total_investment = sum(
            stock["investment"] for stock in portfolio.values()
        )

        print("Stock added successfully!")
        print("Investment:", investment)

    elif choice == "2":
        print("\nYour Stock Portfolio:")

        if not portfolio:
            print("No stocks added yet.")
        else:
            for name, stock in portfolio.items():
                print("\nStock:", name)
                print("Quantity:", stock["quantity"])
                print("Price per share:", stock["price"])
                print("Investment:", stock["investment"])

            print("\nTotal Investment:", total_investment)

    elif choice == "3":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")