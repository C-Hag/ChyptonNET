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

add(7,7)       
 
def multiply(x,y):
        return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
        print(x ** .5)

square_root(64)

def nl(): #new line
        print('\n')
         
nl()
#BOOLEAN EXPRESSION (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*4 != 9

print(bool1, bool2, bool3, bool4)
print (type(bool1))

bool5 = "True"
print(type(bool5))
nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <=7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 > 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False #CHECK THE PYTHON TRUTH TABLE JUST GOOGLE IT. 

nl()
#CONDITIONAL STATEMENTS  - if/else

def car(money):
        if money >= 2: 
                return "You got yourself a new car!"
        else:
                return "No new car for you!"

print(car(3))
print(car(1))

def license(age,money):
        if (age >= 18) and (money >=5):
                return "We're buying a car"
        elif (age >=18) and (money < 5):
                return "Come back with more money."
        elif (age < 18) and (money >= 5):
                return "Nice try, kid!"
        else: 
                return "You're too young to buy & drive a car."

print(license(18,5))
print(license(18,4))
print(license(17,5))
print(license(17,4))
 
nl()
#LISTS - HAVE brackets []
movies = ["Monty Pythons's Flying Circus", "And now for something Completly Different", "Monthy Python and the Holy Grail", "Monthy Pyhton's Life of Brian", "Monty Python Live at the Hollywood Bowl", "Monty Python's The Meaning of Life", "Monty Python Live (Mostly)," "Monty Python's Personal Best"]
print(movies[1]) #Returns the second item in the list
print(movies[0]) #Return the first item in the list.
print(movies[1:3]) #Return the first index number given right until the last number, but not include the last number. 
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(movies[-1]) #return last item in list. 

print(len(movies)) #count items in the list.  
movies.append("Back to the Future")
print(movies) #appends to the end of the list.
movies.insert(2, "Heat")
print(movies)

movies.pop(0) #removes the last item
print(movies)

rogers_movies = ['Scream', 'The Last Samurai', 'Dances with Wolves']
tiffanys_movies = ['An Officer and a Gentleman', 'Top Gun', 'Gone with the Wind']
our_favorite_movies = rogers_movies + tiffanys_movies + movies
print("our_favorite_movies")

grades = [["bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)

nl()
#TUPLES - Do not change. () 
grades = ("a", "b", "c", "d", "f")

print(grades[1])

nl()
#LOOPING

#For loops - start to finish of an iterate.
vegetables = ["cucumber", "spinach", "cabbage", "tomato", "olive", "pepper"]
for x in vegetables:
        print(x)

nl()
#example for looping through ip-adresses. 
#192.168.1.1-254

#ip = 1..254
#for x in ip: 
#       ping 192.168.1.x
        

#While loops - execute as long as True
i = 1

while i < 10:
        print(i)
        i += 1

nl()

#ADVANCED STRINGS

my_name = "Christoffer"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimiter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all of your money' "
print(quote)
quote = "He said, \"give me all your money\"" 
print(quote)
 
too_much_space =  "                                  hello                "
print(too_much_space.strip())

print("A" in "Apple") #True
print("a" in "APPLE") #False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

#Mississippi
#MiSSissIPPi 

movie = "Monty Pythons's Flying Circus"
print ("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")
 
nl()
#DICTIONARIES - Key/value pairs {}

drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8} #drink is the key price is the value
print(drinks)

employees = {"Finance":  ["Rob", "Linnea", "Alice", "Tina"], "IT": ["Gordon", "Louise", "Teddy"], 
             "HR": ["George", "Constanza", "Jerry S"]}
print(employees)

employees['Legal'] = ["Mr. Hackman"] #adding a new key:value pair
print(employees)

employees.update({"Sales": ["Andy", "Ollie"]}) #adds new key:value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))