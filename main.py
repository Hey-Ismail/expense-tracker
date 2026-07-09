import time

def expenseTracker():
    # print("Enter todays date :")
    pass

def addExpnese():
    # creating a dict to save the catagory amount
    expenses = {
        "food": 0,
        "transportation": 0,
        "mobile bill": 0,
        "rent": 0,
        "utilities": 0,
        "groceries": 0,
        "entertainment": 0,
        "health": 0,
        "others": 0,
    }

    # flag=True
    while True:
        try:
            category = int(input("\nChoose your category: "))

            if category == 0:
                print("-" * 10 + "Exiting menu" + "-" * 10)
                break

            if category < 1 or category > 9:
                print("Invalid choice! Please enter a number between 1 and 9.")
                continue

            # Add amount to the correct category
            amount = int(input("Enter the amount: "))

            if amount < 0:
                print("Invalid amount ! Please numerical value  > 0 ")
                continue

            if category == 1:
                expenses["food"] += amount
            elif category == 2:
                expenses["transportation"] += amount
            elif category == 3:
                expenses["mobile bill"] += amount
            elif category == 4:
                expenses["rent"] += amount
            elif category == 5:
                expenses["utilities"] += amount
            elif category == 6:
                expenses["groceries"] += amount
            elif category == 7:
                expenses["entertainment"] += amount
            elif category == 8:
                expenses["health"] += amount
            elif category == 9:
                expenses["others"] += amount

            print(f"Added ট {amount} successfully!")

        except ValueError:
            print("Please enter valid numbers only!")

    # searchExpense(expenses)
    # print("\n")
    print("-" * 50)
    print("You have successfully added all of you expense.")
    print(
        "Do you need any changes in your expense list? \nif yes press / type : 1 \nif no  press / type : 0"
    )

    while True:
        try:
            userChoice = int(input("Enter your wish : "))
            if userChoice < 0 or userChoice > 1:
                print("Enter / press 0 or 1 . Nothing Else.")
                continue
            elif userChoice == 1:
                updateExpense(expenses)
            elif userChoice==0:
                print("So everything is correct.")
                print("Let's See total invoice of your list.")
                viewExpenseDetailes(expenses)
                break
        except ValueError:
            # passValueError:
            print("Please enter 'numbers' only!")


def updateExpense(expenses):
    # pass
    # print(expense)
    print("You can now update anything in your tracker list.")
    print("Which item you can to update?")
    print("-" * 20)
    print("Choose your category by entering the number:")
    print("1  -> Food")
    print("2  -> Transportation Cost")
    print("3  -> Mobile Bill")
    print("4  -> Rent")
    print("5  -> Utilities")
    print("6  -> Groceries")
    print("7  -> Entertainment")
    print("8  -> Health")
    print("9  -> Others")
    print("0  -> Exit")

    while True:
        try:
            category = int(input("\nChoose your category: "))

            if category == 0:
                print("-" * 10 + "Exiting menu" + "-" * 10)
                break

            if category < 1 or category > 9:
                print("Invalid choice! Please enter a number between 1 and 9.")
                continue

            # Add amount to the correct category
            amount = int(input("Enter the amount: "))

            if amount < 0:
                print("Invalid amount ! Please numerical value  > 0 ")
                continue

            if category == 1:
                expenses["food"] += amount
            elif category == 2:
                expenses["transportation"] += amount
            elif category == 3:
                expenses["mobile bill"] += amount
            elif category == 4:
                expenses["rent"] += amount
            elif category == 5:
                expenses["utilities"] += amount
            elif category == 6:
                expenses["groceries"] += amount
            elif category == 7:
                expenses["entertainment"] += amount
            elif category == 8:
                expenses["health"] += amount
            elif category == 9:
                expenses["others"] += amount

            print(f"Added ট {amount} successfully!")

        except ValueError:
            print("Please enter valid numbers only!")


def searchExpense(expense):
    pass


def viewExpenseDetailes(expense):
    # pass
    # Show summary at the end
    width = 50

    print("\n" + "-" * width)
    print(f"| {'Expense Summary':^{width - 4}} |")
    print("-" * width)

    print(f"| {'1. Food':<25} : ৳ {expense['food']:<16} |")
    print(f"| {'2. Transportation':<25} : ৳ {expense['transportation']:<16} |")
    print(f"| {'3. Mobile Bill':<25} : ৳ {expense['mobile bill']:<16} |")
    print(f"| {'4. Rent':<25} : ৳ {expense['rent']:<16} |")
    print(f"| {'5. Utilities':<25} : ৳ {expense['utilities']:<16} |")
    print(f"| {'6. Groceries':<25} : ৳ {expense['groceries']:<16} |")
    print(f"| {'7. Entertainment':<25} : ৳ {expense['entertainment']:<16} |")
    print(f"| {'8. Health':<25} : ৳ {expense['health']:<16} |")
    print(f"| {'9. Others':<25} : ৳ {expense['others']:<16} |")

    print("|" + "-" * (width - 2) + "|")

    print(f"| {'Total Expense':<25} : ৳ {sum(expense.values()):<16} |")

    print(
        "-" * width
    )  # total = food + transportation + mobile_bill + rent + utilities + groceries + entertainment + health + others
    # print(f"Total Expense        : ট {total}")
    # print("="*40)


def main():
    # date = input("Enter today's date: ")
    # print(f"Todays Date :{datetime.datetime.now()}")

    line_width = 50
    print("-" * line_width)
    print(f"| {'Welcome to your personal expense tracker!':<{line_width - 4}} |")

    # formating time and date...
    time_tuple = time.localtime()
    date = time.strftime("%m/%d/%Y", time_tuple)
    timee = time.strftime("%I:%M %p", time_tuple)
    print(f"| {'Todays Date : ' + date:<{line_width - 4}} |")
    print(f"| {'Todays Time : ' + timee:<{line_width - 4}} |")
    print("-" * line_width)

    print("Choose your category by entering the number:")
    print("1  -> Food")
    print("2  -> Transportation Cost")
    print("3  -> Mobile Bill")
    print("4  -> Rent")
    print("5  -> Utilities")
    print("6  -> Groceries")
    print("7  -> Entertainment")
    print("8  -> Health")
    print("9  -> Others")
    print("0  -> Exit")

    addExpnese()


# Run the function
main()
