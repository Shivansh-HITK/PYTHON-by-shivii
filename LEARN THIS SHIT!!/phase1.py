Topic 1 : Variable & Data Types
think like "dabbe" also called containers to contain data
syntax = variable_name = Value

MAIN DATA TYPES
1. String (str) : A sequence of characters enclosed in quotes ""
example = name = "Shivansh"
2. Integer (int) : Whole numbers without a decimal point
example = age = 18
3. Float (float) : Numbers with a decimal point
example = height = 5.9
4. Boolean (bool) : Represents True or False values
example = is_student = True
5. List (list) : An ordered collection of items enclosed in square brackets []
example = fruits = ["apple", "banana", "cherry"]
6. Tuple (tuple) : An ordered collection of items enclosed in parentheses ()
example = coordinates = (10, 20)
7. Dictionary (dict) : A collection of key-value pairs enclosed in curly braces {}
example = person = {"name": "Shivansh", "age": 18, "height": 5.9}
8. Set (set) : An unordered collection of unique items enclosed in curly braces {}
example = unique_numbers = {1, 2, 3, 4, 5}
9. NoneType (None) : Represents the absence of a value
example = result = None

Example : 
# Variable ban rahe hain
user_name = "Rahul"
user_age = 22
is_logged_in = False

print(user_name)  # Output: Rahul

TOPIC 2 : Input / Output (I/O)
while doing backend dev, we need to take the input and we need to show the output to the user, 
so we need to learn how to take input and show output in python

Output: print() function use hota hai.
Input: input() function user se data leta hai (hamesha String deta hai).

name =  input("Enter your name: ")
print("Entered name is:", name)

Agar number lenge to int ya float lena parega
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

TOPIC 3 : Conditional Statements (If/Else)
It is the brain of the program, it helps us to make decisions based on conditions.
Syntax:
if condition:
    # code to execute if condition is true
elif another_condition:
    # code to execute if another_condition is true
else:
    # code to execute if all conditions are false   
Example:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.") 


TOPIC 4 : Loops
When we have to repeat block of codes 
ando many times,
we use loops to avoid writing the same code again and again.  

1.For Loop : when we know how many times we have to repeat the block of code
Syntax:
for variable in iterable:
    # code to execute for each item in the iterable 
Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
2. While Loop : when we don't know how many times we have to repeat the block of code
Syntax:
while condition:
    # code to execute as long as the condition is true
    # update the condition to avoid infinite loop
Example:
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # update the condition to avoid infinite loop


TOPIC 5: Data Structures (The King of Backend)
Data structures are a way of organizing and storing data in a computer so that it can be accessed and modified efficiently.
1. List : An ordered collection of items that can be changed (mutable) and allows duplicate values.
example = fruits = ["apple", "banana", "cherry"]
syntax = list_name = [item1, item2, item3, ...]
indexing starts from 0
2. Dictionaries : in backend we need to send data in the JSON format,
and JSON format is similar to dictionary in python,
it is a collection of key-value pairs that can be changed (mutable) and does not allow duplicate keys.

Syntax: dict_name = {"key1": value1, "key2": value2, "key3": value3}

user = {
    "name": "Shivansh",
    "age": 18,
    "height": 5.9
}
 DATA ACCCES KARNA
print(user["name"])  # Output: Shivansh
print(user["age"])   # Output: 18
print(user["height"]) # Output: 5.9

IF Want to add new key-value pair
user["city"] = "gaya"

TOPIC 6: Functions
Functions are reusable blocks of code that perform a specific task.
They help in breaking down a program into smaller,
manageable pieces and promote code reusability.
Syntax:
def function_name(parameters):
    # code to execute
    return value  # optional
keywords: def - to define a function
return - to return a value from the function (optional)
Example:
def greet(name):
    return f"Hello, {name}!"
print(greet("Shivansh"))  # Output: Hello, Shivansh!

Bonus Topic: OOP (Classes & Objects - Basic Level)
Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and programs.
It allows for the creation of classes, which are blueprints for objects,
   and objects are instances of classes.

Class: Ek blueprint (jaise ek ki recipe).
Object: Us blueprint se banaya hua actual cheez (jaise bani hui roti).
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    OBJECT bana rahein hein toh : 
    my_car = Car("Tesla")
my_car.drive()  # Output: Tesla gaadi chal rahi hai!

        