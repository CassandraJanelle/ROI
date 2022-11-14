class calc():
    def __init__(self):

        self.cashflow = 0
        self.expenselist = []
        self.incomelist = []
        self.incomesdict = {}
        self.expensesdict = {}
            
    def income(self):
        #inputs
        print(f"Current income(s) : {self.incomelist}")
        income_name = input("Enter income name : ")
        income_num = float(input(f"What is the value of {income_name}?"))
        #store values to attributes
        self.incomesdict[income_name] = income_num #{income_name|income.num}
        self.cashflow += income_num
        #add income_name to incomelist
        self.incomelist.append(income_name) 
        #print attributes
        print(self.incomelist)
        print(f"Cashflow: {self.cashflow}")
        more_incomes = input("Would you like to add another source of income? (y/n) : ")
        if more_incomes.lower() == "y":
            self.income() 
        elif more_incomes.lower() == "n":
            pass
        else:
            print("Invalid input, please try again")

    def expenses(self):
        print("- - - - - Current Expenses - - - - - ")
        print(self.expenselist)
        expense_name = input("Enter the expense as a string : ")
        self.expenselist.append(expense_name)
        expense_num = float(input(f"What is the cost of {expense_name}?"))
        self.expensesdict[expense_name] = expense_num #{expense_name | expense_num}
        self.cashflow -= expense_num
        print(self.expensesdict)
        print(f"Cashflow: {self.cashflow}")
        more_expenses = input("Would you like to add another expense? (y/n) : ")
        if more_expenses.lower() == "y":
            self.expenses() 
        elif more_expenses.lower() == "n":
            pass
        else:
            print("Invalid input, please try again")


    def cashFlow(self):
        print(f"Your incomes are: {self.incomesdict}.") 
        print(f"Your expenses are: {self.expensesdict}.")
        print(f"Your cash flow is {self.cashflow}.")

    def roi(self):
        investment = float(input("Please enter your initial investment : "))
        output = float(float(self.cashflow) / investment)
        output * 100.0
        print(f"Your return on investment is {output}%.")

# - - - - - - - - - - - - - - - Main- - - - - - - - - - - - - - - - 
class Main():
    def showInstructions():
        print("""
Welcome to BLL ROI Calculator by Cassandra
Options:
[1] Add Source of Income
[2] Add Expenses
[3] Cash Flow
[4] Calculate ROI
[5] Quit
        """)
    def run():
        Main.showInstructions()
        self = calc()
        while True:
            choice = input("What is your next option?")
            print("""
                Welcome back to BLL ROI Calculator 
                Options:
                [1] Add Source of Income
                [2] Add Expenses
                [3] Cash Flow
                [4] Calculate ROI
                [5] Quit
                 """)
            if choice == "1":
                self.income()
            elif choice == "2":
                self.expenses()    
            elif choice == "3":
                self.cashFlow()
            elif choice == "4":
                self.roi()
            elif choice == "5":
                print("Thank you for using this program")
                break
            elif choice.lower.strip() == "print instructions: #SECRET COMMAND":
                print("""[1] Add Source of Income
[2] Add Expenses
[3] Cash Flow
[4] Calculate ROI""")
            else:
                print("invalid input... please try again.")

Main.run()