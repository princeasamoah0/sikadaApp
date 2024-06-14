class BudgetRanger:
    def __init__(self, query):
        self.price_range = "" 
        if int(query.price) <= 10000:
            self.price_range = 'Low Budget'
        elif int(query.price) <= 30000:
            self.price_range = 'Medium Budget'
        else:
            self.price_range = 'High Budget'
