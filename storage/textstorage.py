from model.transaction import Transaction

transactionstrack = []
def save_transaction(transaction_list):
    with open("D:\\PythonProject\\PyCharmHome\\FinanceTracker\\data\\transaction.txt", "w") as File:
        for transaction in transaction_list:
                File.write("transaction id is {}\ntransaction amount is {}\ntransaction type is {}\ntransaction description is {}\ntransaction catogery is {}\ntransaction date is {}\n".format(transaction.Id, transaction.Amount, transaction.TransactionType , transaction.Category, transaction.Date,transaction.Description))

def load_transaction():
    with open("D:\\PythonProject\\PyCharmHome\\FinanceTracker\\data\\transaction.txt", "r") as file:
        transaction_list = file.readlines()
        for transaction in range(0, len(transaction_list), 6):
            if transaction + 5 >= len(transaction_list):
                break
            transaction_id = transaction_list[transaction].strip("\n")
            transaction_amount = transaction_list[transaction + 1].strip("\n")
            transaction_category = transaction_list[transaction + 2].strip("\n")
            transaction_description = transaction_list[transaction + 3].strip("\n")
            transaction_date = transaction_list[transaction + 4].strip("\n")
            transaction_type = transaction_list[transaction + 5].strip("\n")

            transaction_obj = Transaction(transaction_id, transaction_amount, transaction_category, transaction_description,transaction_date, transaction_type)
            transactionstrack.append(transaction_obj)
    return transactionstrack
