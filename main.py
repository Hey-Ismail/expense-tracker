import time
import os
import numpy as np


class ExpenseTracker:
    def __init__(self):
        self.name = ""
        self.expenses = {
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

        self.expenseCatagory = {
            1: "food",
            2: "transportation",
            3: "mobile bill",
            4: "rent",
            5: "utilities",
            6: "groceries",
            7: "entertainment",
            8: "health",
            9: "others",
        }

    def showMenu(self):
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

    def addExpense(self):
        while True:
            try:
                category = int(input("\nChoose your category: "))

                if category == 0:
                    print("-" * 10 + "Exiting menu" + "-" * 10)
                    break

                if category < 1 or category > 9:
                    print("Invalid choice! Please enter a number between 1 and 9.")
                    continue

                amount = int(input("Enter the amount: "))

                if amount < 0:
                    print("Invalid amount! Please enter a numerical value > 0.")
                    continue

                key = self.expenseCatagory[category]
                self.expenses[key] += amount

                print(f"Added ৳ {amount} successfully!")

            except ValueError:
                print("Please enter valid numbers only!")

        print("-" * 50)
        print("You have successfully added all your expenses.")
        print("Do you need any changes in your expense list?")
        print("If yes press/type: 1")
        print("If no  press/type: 0")

        while True:
            try:
                user_choice = int(input("Enter your wish: "))
                if user_choice not in (0, 1):
                    print("Enter/press 0 or 1. Nothing else.")
                    continue
                elif user_choice == 1:
                    self.updateExpense()
                else:
                    print("Exiting...")
                    print("Let's see total invoice of your list.")
                    self.expenseDetailes()
                    self.saveExpenseData()
                    break
            except ValueError:
                print("Please enter numbers only!")

    def updateExpense(self):
        print("\nYou can now update anything in your tracker list.")
        self.showMenu()

        while True:
            try:
                category = int(input("\nChoose your category: "))

                if category == 0:
                    print("-" * 10 + "Quitting update menu" + "-" * 10)
                    break

                if category < 1 or category > 9:
                    print("Invalid choice! Please enter a number between 1 and 9.")
                    continue

                amount = int(input("Enter the amount: "))

                if amount < 0:
                    print("Invalid amount! Please enter a numerical value > 0.")
                    continue

                key = self.expenseCatagory[category]
                self.expenses[key] += amount
                print(f"Added ৳ {amount} successfully!")

            except ValueError:
                print("Please enter valid numbers only!")

    def expenseDetailes(self):
        width = 50

        print("\n" + "-" * width)
        print(f"| {'Expense Summary':^{width - 4}} |")
        print("-" * width)

        print(f"| {'1. Food':<25} : ৳ {self.expenses['food']:<16} |")
        print(f"| {'2. Transportation':<25} : ৳ {self.expenses['transportation']:<16} |")
        print(f"| {'3. Mobile Bill':<25} : ৳ {self.expenses['mobile bill']:<16} |")
        print(f"| {'4. Rent':<25} : ৳ {self.expenses['rent']:<16} |")
        print(f"| {'5. Utilities':<25} : ৳ {self.expenses['utilities']:<16} |")
        print(f"| {'6. Groceries':<25} : ৳ {self.expenses['groceries']:<16} |")
        print(f"| {'7. Entertainment':<25} : ৳ {self.expenses['entertainment']:<16} |")
        print(f"| {'8. Health':<25} : ৳ {self.expenses['health']:<16} |")
        print(f"| {'9. Others':<25} : ৳ {self.expenses['others']:<16} |")

        print("|" + "-" * (width - 2) + "|")
        print(f"| {'Total Expense':<25} : ৳ {np.sum(list(self.expenses.values())):<16} |")
        print(f"| {'average Expense':<25} : ৳ {np.mean(list(self.expenses.values())):<16} |")
        print(f"| {'maximum Expense':<25} : ৳ {np.max(list(self.expenses.values())):<16} |")
        print(f"| {'minimum Expense':<25} : ৳ {np.min(list(self.expenses.values())):<16} |")
        print("-" * width)

    def saveExpenseData(self):
        folder = "data"
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, "expenses.txt")

        next_id = 1
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                next_id = content.count("Record ID") + 1
        except FileNotFoundError:
            next_id = 1

        time_tuple = time.localtime()
        date = time.strftime("%m/%d/%Y", time_tuple)
        timee = time.strftime("%I:%M %p", time_tuple)

        width = 50
        lines = [
            "=" * width,
            f"| {'Record ID : ' + str(next_id):<{width - 4}} |",
            f"| {'Date      : ' + date:<{width - 4}} |",
            f"| {'Time      : ' + timee:<{width - 4}} |",
            f"| {'Name      : ' + self.name:<{width - 4}} |",
            "-" * width,
            f"| {'Expense Summary':^{width - 4}} |",
            "-" * width,
            f"| {'1. Food':<25} : {self.expenses['food']:<18} |",
            f"| {'2. Transportation':<25} : {self.expenses['transportation']:<18} |",
            f"| {'3. Mobile Bill':<25} : {self.expenses['mobile bill']:<18} |",
            f"| {'4. Rent':<25} : {self.expenses['rent']:<18} |",
            f"| {'5. Utilities':<25} : {self.expenses['utilities']:<18} |",
            f"| {'6. Groceries':<25} : {self.expenses['groceries']:<18} |",
            f"| {'7. Entertainment':<25} : {self.expenses['entertainment']:<18} |",
            f"| {'8. Health':<25} : {self.expenses['health']:<18} |",
            f"| {'9. Others':<25} : {self.expenses['others']:<18} |",
            "|" + "-" * (width - 2) + "|",
            f"| {'Total Expense':<25} : ৳ {np.sum(list(self.expenses.values())):<16} |"
            f"| {'average Expense':<25} : ৳ {np.mean(list(self.expenses.values())):<16} |"
            f"| {'maximum Expense':<25} : ৳ {np.max(list(self.expenses.values())):<16} |"
            f"| {'minimum Expense':<25} : ৳ {np.min(list(self.expenses.values())):<16} |"

            "=" * width,
            "",
        ]

        # print(f"| {'Total Expense':<25} : ৳ {np.sum(list(self.expenses.values())):<16} |")
        # print(f"| {'average Expense':<25} : ৳ {np.mean(list(self.expenses.values())):<16} |")
        # print(f"| {'maximum Expense':<25} : ৳ {np.max(list(self.expenses.values())):<16} |")
        # print(f"| {'minimum Expense':<25} : ৳ {np.min(list(self.expenses.values())):<16} |")
        #  print(f"| {'Total Expense':<25} : ৳ {np.sum(list(self.expenses.values())):<16} |")
        #   print(f"| {'average Expense':<25} : ৳ {np.mean(list(self.expenses.values())):<16} |")


        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

        print(f"\n✓ Record saved as ID {next_id} in '{filename}'")

    def run(self):
        line_width = 50
        print("-" * line_width)
        print(f"| {'Welcome to your personal expense tracker!':<{line_width - 4}} |")

        time_tuple = time.localtime()
        date = time.strftime("%m/%d/%Y", time_tuple)
        timee = time.strftime("%I:%M %p", time_tuple)
        print(f"| {'Todays Date : ' + date:<{line_width - 4}} |")
        print(f"| {'Todays Time : ' + timee:<{line_width - 4}} |")
        print("-" * line_width)

        self.name = input("\nEnter your name: ")
        print(f"\nWelcome, {self.name}!")
        print("-" * line_width)

        self.showMenu()
        self.addExpense()


def main():
    tracker = ExpenseTracker()  # object creation
    tracker.run()               # calling class method


if __name__ == "__main__":
    main()
