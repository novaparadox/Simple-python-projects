#This is a REALLY basic calculator so don't expect a lot
def add(x,y):
    a = x + y
    return a

def subtract(x,y):
    a = x - y
    return a

def multiply(x,y):
    a = x * y
    return a

def divide(x,y):
    a = x / y
    return a


user_response = input("Would you like to add, subtract, multiply or divide: ")

if user_response == 'add':
    first_number = int(input('First number: '))
    second_number = int(input('Second number: '))
    print(add(first_number,second_number))
elif user_response == 'subtract':
    first_number = int(input('First number: '))
    second_number = int(input('Second number: '))
    print(subtract(first_number,second_number))
elif user_response == 'multiply':
    first_number = int(input('First number: '))
    second_number = int(input('Second number: '))
    print(multiply(first_number,second_number))
elif user_response == 'divide':
    first_number = int(input('First number: '))
    second_number = int(input('Second number: '))
    print(divide(first_number,second_number))

input("Press Enter to close...")