class Ecars: 
        def __init__(self, name, price):
                self.name = name
                self.price = float(price)
        
        def budget_check(self, budget): 
                if not isinstance(budget, (int, float)):
                        print('Invalid entry. Please enter a number.')
                        exit()
        
        def change(self, budget):
                return (budget - self.price)
        
        def buy(self, budget):
                self.budget_check(budget)
                
                if budget >= self.price: 
                        print(f'You can cop some {self.name}')
                        
                        if budget == self.price: 
                                print('You have enough money to buy this Electric Vehicle.')
                                
                        else: 
                            
                                print(f'You can buy these cars and have $ {self.change(budget)} left over')
                        
                        exit('Thanks for using the ecars budget app!') 