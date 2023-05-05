#!/bin/python3

from ecars import Ecars

low = Ecars('i3', 30)
medium = Ecars('Apple Titan EV', 120)
high = Ecars('Lotus Eletre R', 400)

try:
    
        ecars_budget = float(input('What is your Ecars budget?'))

except ValueError:
        exit('Please enter a number')

for ecars in [high, medium, low]:
        ecars.buy(ecars_budget)        
