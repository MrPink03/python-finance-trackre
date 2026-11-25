
class Transaction:
    def __init__(self, transid, amount, category, description, date, transaction_type):
        self.Id = transid
        self.Amount = amount
        self.Category = category
        self.Description = description
        self.Date = date
        self.TransactionType = transaction_type
