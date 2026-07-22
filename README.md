# Expense Tracker Project

This is a Python-based expense tracker application that helps users keep track of their daily expenses. It is a command-line program where users can add their expenses, update them, and save the records to a file.

## About This Project

Many people struggle to manage their monthly expenses. This project helps users to:
- Keep a record of where their money is going
- See a summary of total, average, maximum, and minimum expenses
- Save all records with date, time, and user name for future reference

## Features

1. **User Name Entry** - The program asks for your name at the start and saves it with each record

2. **Add Expenses** - Users can add expenses in 9 different categories:
   - Food
   - Transportation
   - Mobile Bill
   - Rent
   - Utilities
   - Groceries
   - Entertainment
   - Health
   - Others

3. **Update Expenses** - If you made a mistake or want to add more money to a category, you can update it

4. **Expense Summary** - After entering all expenses, the program shows:
   - Total Expense (how much you spent in total)
   - Average Expense (average spending per category)
   - Maximum Expense (highest spending category)
   - Minimum Expense (lowest spending category)

5. **Save to File** - All your expense data is saved in a text file called `expenses.txt` inside the `data` folder. Each record includes:
   - Record ID
   - Date
   - Time
   - User Name
   - All expense amounts

6. **Formatted Output** - The program displays data in a neat table format using borders and proper spacing

## How to Use

1. Run the program: **py main.py**

2. Enter your name when asked

3. Choose a category by entering the number (1-9)

4. Enter the amount you spent

5. Press 0 when done adding expenses

6. Choose if you want to update anything (1 for yes, 0 for no)

7. Your data will be saved automatically

## Project Files

- `main.py` - This is the main file that contains all the code
- `data/expenses.txt` - This file is created automatically and stores all your expense records
- `requirements.txt` - Lists the libraries needed to run this project

## Requirements

- Python 3 or higher
- NumPy library (used for calculating total, average, max, and min)


## Example Output

When you run the program, it will look like this:

```
--------------------------------------------------
| Welcome to your personal expense tracker!      |
| Todays Date : 07/22/2026                       |
| Todays Time : 02:30 PM                         |
--------------------------------------------------

Enter your name: John

Welcome, John!
--------------------------------------------------
Choose your category by entering the number:
1  -> Food
2  -> Transportation Cost
...
```

<!--  -->

---

## MADE BY

| Name | ID |
| :--- | :--- |
| **Ismail Hossain Fahim** | **23-50009-1** |
| **MD. Moudud Ahamed Alve** | **23-50224-1** |