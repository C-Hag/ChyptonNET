#!/bin/python3

# name=input("Enter your name: ")
# car = input("What is your favourite car? ")
# print("Hello "+name+"! Let's go for a drive with the "+car+". ")

# Let's try a simple calculator. 
x = float(input("Give me a number: "))
o = input("Give me an operator: ") #Give the user an operator to put in...like subtraktion or exponents. 
y = float(input("Give me yet another number: "))   #this uses strings, change to int or float for x & y. 

if o == "+": 
        print(x + y)
elif o == "-": 
        print(x - y)
elif o == "/":
        print(x / y)
elif o == "*":
        print(x * y)
elif o== "**" or o == "^":
        print(x ** y)
else: 
        print("Not a valid operator!")

