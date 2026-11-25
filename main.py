import uuid
import datetime
from model.transaction import Transaction
from storage.textstorage import save_transaction, load_transaction

transaction_list = []
income_list = []
expense_list = []
monthly_transaction =[]

"""load all transactions"""
transaction_list = load_transaction()

print("Welcome To Finance Tracker App-made by @Gishan")
try:
    userChoice = input("please select one from the menu\n1.Add Income\n2.Add Expense\n3.View Transactions\n4.View Balance\n5.Monthly Report\n6.Search Transactions\n7.Exit\nchoose an option:")
except ValueError:
    print("please input a valid number! program terminating!")
    exit()

def addincome():
    incomeammount = int(input("please enter the income amount:"))
    income_list.append(incomeammount)
    incomecatogery = ["Salary", "Freelancing", "Business", "Investment", "Gift", "Other"]
    incomemethod = input("please select the income method:\n1.Salary\n2.Freelancing\n3.Business\n4.Investment\n5.Gift\n6.Other")
    if incomemethod == "1":
        incomemethod = incomecatogery[0]
    elif incomemethod == "2":
        incomemethod = incomecatogery[1]
    elif incomemethod == "3":
        incomemethod = incomecatogery[2]
    elif incomemethod == "4":
        incomemethod = incomecatogery[3]
    elif incomemethod == "5":
        incomemethod = incomecatogery[4]
    elif incomemethod == "6":
        incomemethod = incomecatogery[5]
    elif incomemethod == "7":
        incomemethod = incomecatogery[6]

    incomedescription = input("please enter the description for the income:")
    transaction_id = str(uuid.uuid4())
    transaction_date = datetime.datetime.now()
    new_income = Transaction(transaction_id, incomeammount,  incomedescription, transaction_date, incomemethod, transaction_type="income")

    transaction_list.append(new_income)
    save_transaction(transaction_list)
    income_list.append(new_income)




def addexpense():
    expenseamount = int(input("please enter the expense amount:"))
    expensecategory = input("please enter the expense category:")
    expensedescription = input("please enter the expense description:")
    expensedate = datetime.datetime.now()
    transaction_id = str(uuid.uuid4())
    expenseobj  = Transaction(transaction_id, expenseamount,expensecategory, expensedescription, expensedate, transaction_type="expense")

    transaction_list.append(expenseobj)
    expense_list.append(expenseobj)
    save_transaction(transaction_list)




def viewtransaction():
    transaction_duplicate = []
    for i in transaction_list:
        transaction_duplicate.append(i.Id)
        transaction_duplicate.append(i.Amount)
        transaction_duplicate.append(i.Category)
        transaction_duplicate.append(i.Description)
        transaction_duplicate.append(i.Date)
        transaction_duplicate.append(i.TransactionType)
    for x in transaction_duplicate:
        print(x)
    list_length = len(transaction_list)
    if list_length == 0:
        print("You dont have any transactions!")


def viewbalance():
    income_total = 0
    for i in income_list:
        income_total +=i

    expense_total = 0
    for i in expense_list:
        expense_total +=i

    balance = income_total - expense_total
    print("your balance is {}".format(balance))


def monthlyreport():
    month = input("Enter month:")
    try:
        month = int(month)
    except ValueError:
        print("please input a valid number! program terminating!")
    if int(month)<1 or int(month)>12:
        print("please input a valid month! program terminating!")

    for transaction in transaction_list:
        if transaction.date.month == month:
            monthly_transaction.append(transaction)

    total_income = 0
    total_expense = 0
    for item in monthly_transaction:
        if item.transaction_type == "income":
            total_income+=item.amount
        else:
            total_expense +=item.amount
    monthly_saving = total_income - total_expense
    print("you saved {}".format( monthly_saving))







def searchtransaction():
    print("expenses or incomes?")
    answer = input()
    for transaction in monthly_transaction:
        if transaction.transaction_type == answer:
            print(transaction)

def exits():
    print("thanks for using our service!.have a good day program exiting...!")
    exit()


if userChoice == "1":
    addincome()
elif userChoice == "2":
    addexpense()
elif userChoice == "3":
    viewtransaction()
elif userChoice == "4":
    viewbalance()
elif userChoice == "5":
    monthlyreport()
elif userChoice == "6":
    searchtransaction()
elif userChoice == "7":
    exits()
else:
    print("sorry wrong selection please read the menu and try again!.program terminating!")
