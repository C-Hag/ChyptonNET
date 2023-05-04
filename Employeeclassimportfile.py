#!/bin/python3

from Employees import Employees

e1 = Employees("Bart", "Sales", "Director of Sales", 100000, 20)
e2 = Employees("Marge", "Executive", "CIO", 150000, 10)

print(e1.name) 
print(e2.role)
print(e1.eligible_for_retirement())
