# - variable declaration /
# - Data Types
    # - Primitive
        # - Numbers
            # - integers
            num1 = 42
            # - floats
            num2 = 2.3
        # - Boolean
        boolean = True
        # - string
        string = 'Hello World'

# - type check
print(type(fruit))

# - log statement
print(person)

# - comment
    # - single line
    # - multiline*
    """
    Bonus section
    """

    # - Composite
        #     - List 
            #- initialize
            pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
            #- access value
            print(pizza_toppings[1])
            # - change value
            pizza_toppings[2] = "pineapple"
            #- add value
            pizza_toppings.append('Mushrooms')
            #- delete value
            pizza_toppings.pop()
            pizza_toppings.pop(1)

        # - Tuples
            #     - initialize
            fruit = ('blueberry', 'strawberry', 'banana')
            # - access value
            print(fruit[1])
            print(fruit[2])
        # - Dictionary
            # - initialize
            person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
            # - access value
            print(person['name'])
            print(person)
            # - change value
            person['name'] = 'George'
            # - add value
            person['eye_color'] = 'blue'
            # - delete value
            person.pop('eye_color')
# - conditional
#     - if
if num1 > 45:
    print("It's greater")
# - length check
if len(string) < 5:
    print("It's a short word!")
#     - else if
elif len(string) > 15:
    print("It's a long word!")
#     - else
else:
    print("It's lower")
else:
    print("Just right!")
# - for loop
#     - start (2 is the sart value)
    for x in range(2,5):
        print(x)
#     - stop
    for x in range(5):
        print(x)

#     - increment
for x in range(2,10,3):
    print(x)
#     - break
    print('After 1st if statement')
    if topping == 'Olives':
        break
#     - continue
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
#     - sequence
# - while loop
#     - start
x = 0
#     - stop
    while(x < 5):
        print(x)
#     - increment
        x += 1
# - function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#     - parameter
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#     - argument
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#     - return
print_hello_ten_times()
print_hello_x_times(4)
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

# * Bonus: Errors

# - NameError: name <variable name> is not defined
#   print(num3)


# - KeyError: 'favorite_team'
# print(person['favorite_team'])
# - IndexError: list index out of range
# print(pizza_toppings[7])
# - IndentationError: unexpected indent
#    num3 = 72
#   print(boolean)
# - Tuples
        #     - change value
        # - TypeError: 'tuple' object does not support item assignment
        # fruit[0] = 'cranberry'
#     - add value
        # - AttributeError: 'tuple' object has no attribute 'append'
        # fruit.append('raspberry')
#     - delete value
        # - AttributeError: 'tuple' object has no attribute 'pop'
        # fruit.pop(1)






