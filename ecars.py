class Ecars: 
        def __init__(self, name, price):
                self.name = name
                self.price = float(price)
        
        def budget_check(self, budget): 
                if not isinstance(budget, (int, float)):
                        print('Invalid entry. Please enter a number.')
                        exit()