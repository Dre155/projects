# Import libraries needed.
import sqlite3
# Connect to database.
expense_db = sqlite3.connect('expensetracker.db')
cursor = expense_db.cursor()
expenses = []
# Create table in database.
cursor.execute('''CREATE TABLE IF NOT EXISTS
                expenses(id INTEGER PRIMARY KEY, category TEXT, amount INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS
                incomes(id INTEGER PRIMARY KEY, category TEXT, amount INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS
                budget(id INTEGER PRIMARY KEY, category TEXT, amount INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS
                goals(id INTEGER PRIMARY KEY, desc TEXT, goal INTEGER, current INTEGER)''')
expense_db.commit()
while True:
    print('''             1. add expense
             2. view expenses
             3. view expenses by category
             4. Add income
             5. view income
             6. View income by category
             7. Set budget for a category
             8. View budget for a category
             9. Set financial goals
             10. View progress towards goals
             11. Quit''')

    menu_option = int(input("Choose here: "))
    while menu_option not in range(1, 11):
        print('''             1. add expense
             2. view expenses
             3. view expenses by category
             4. Add income
             5. view income
             6. View income by category
             7. Set budget for a category
             8. View budget for a category
             9. Set financial goals
             10. View progress towards goals
             11. Quit''')
        menu_option = int(input("Choose here: "))
    if menu_option == 1:
        expense_cat = input("Add an expense category: ")
        expense_amount = int(input("Enter expense amount: "))
        expense = (expense_cat, expense_amount)
        expenses.append(expense)
        cursor = expense_db.cursor()
        cursor.execute(''' INSERT INTO expenses(category, amount) VALUES(?, ?)''', (expense_cat, expense_amount))
        expense_db.commit()

    elif menu_option == 2:
        cursor.execute('''SELECT * FROM expenses''')
        expenses_view = cursor.fetchall()
        for expense in expenses_view:
            print(f"{expense}\n")

    elif menu_option == 3:
        expense_category = int(input("I.D of the expense category to view: "))
        cursor.execute('''SELECT * FROM expenses WHERE ID = ?''', (expense_category,))
        expense_view = cursor.fetchall()
        print(expense_view)
    
    elif menu_option == 4:
        income = input("Add an income category: ")
        income_amount = int(input("Enter income amount: "))
        cursor.execute(''' INSERT INTO incomes(category, amount) VALUES (?, ?)''', (income, income_amount))
        expense_db.commit()
    
    elif menu_option == 5:
        cursor.execute('''SELECT * FROM incomes''')
        incomes_view = cursor.fetchall()
        print(incomes_view)
    
    elif menu_option == 6:
        income_category = int(input("I.D of the income category to view: "))
        cursor.execute('''SELECT * FROM incomes WHERE id = ?''', (income_category,))
        income_view = cursor.fetchall()
        print(income_view)
    
    elif menu_option == 7:
        cat_budget = input("Enter the category to set a budget for: ")
        budget_amount = int(input("Enter budget amount: "))
        cursor.execute('''INSERT INTO budget(category, amount) VALUES (?, ?)''', (cat_budget, budget_amount))
        expense_db.commit()
    
    elif menu_option == 8:
        cat_view_id = int(input("Enter the I.D of a category to view: "))
        cursor.execute('''SELECT * FROM budget WHERE id = ?''', (cat_view_id,))
        expense_db.commit()
    
    elif menu_option == 9:
        desc = input("Goal description: ")
        financial_goal = int(input("Goal amount: "))
        current_amount = int(input("Current amount: "))
        cursor.execute('''INSERT INTO goals(desc, goal, current ) VALUES(?, ?, ?)''', (desc, financial_goal, current_amount))
        expense_db.commit()

    elif menu_option == 10:
        goal_id = int(input("Enter the I.D of the goal you want to view: "))
        cursor.execute('''SELECT * FROM goals WHERE id = ?''', (goal_id,))
        calc_per = (current_amount / financial_goal * 100) 
        print(calc_per + "% towards your goal.")
    
    elif menu_option == 11:
        print("Goodbye!")
        expense_db.commit()
        expense_db.close()
        exit()
    