import random


print("""
    CHALLENGE:  SELECT YOUR LANGUAGE:
    1. Python
    2. JavaScript/Node
    3. SQL
    4. HTML/CSS
    5. React
    6. General
""")

def choice():
    selection = input()
    if selection == '1':
        print(random.choice(python))
    elif selection == '2':
        print(random.choice(JavaScript))
    elif selection == '3':
        print(random.choice(sql))
    elif selection == '4':
        print(random.choice(htmlcss))

python = ['perform the fibonacci sequence algorithm up to 7 terms', 'reverse the given list of [6,7,8,9,10]', 'order this list from smallest to largest [14, 67, 3, 99, 32]', 'add up all the times each character occcurs in this string: We are Learning Algorithms today', 'MADLIB: write a program that randomly selects from two lists, then print a string using random choices from both of those lists']

JavaScript = ['reverse the given an array of [1, 2, 3, 4, 5,]', 'reverse the string HELLO WORLD using recursion', 'Sort the array from largest to smallest[45, 6, 13, 87, 99, 21', ]

sql = ['write a query that would select all columns from a table named CITIES']

htmlcss = ['using flexbox, place four orange squares in the center of a html page, numbered 1 to 4']

choice()
