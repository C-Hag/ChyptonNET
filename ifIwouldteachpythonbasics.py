#!/bin/python3

#Print string
print("Hello, world!")
print('Hello, world!')
print("""This string runs
multiple lines!""") #Triple quote for multi-line
print("This string is "+"awesome!") #We can also concatenate
print('\n') #new line
print('Test that new line out.')



#MATH BASICS
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents 
print(50 % 6) #modulo takes what is left over
print(50 / 6) #division with remainder (or a float).
print(50 // 6) #No remainder

print('\n') 
#VARIABLES AND METHODS
quote = "The way to get started is to quit talking and begin doing."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Chris" #string
age = 99 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? NO.

print("My name is " + name +" and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1 
age + birthday

print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
        name = "Chris" #local variable
        age = 99
        print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()
print(age)

def add_one_hundred(num):
        print(num + 100)

add_one_hundred(100)
def add(x,y):
        print(x + y)