import random

print("""
    QUESTION:  SELECT YOUR LANGUAGE:
    1. Python
    2. JavaScript/Node
    3. SQL
    4. HTML/CSS
    5. React
    6. General
    7. Soft Interview
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
    elif selection == '5':
        print(random.choice(react))
    elif selection == '6':
        print(random.choice(general))
    elif selection == '7':
        print(random.choice(soft))


python = ['explain the difference betwen a list and a tuple', 'What is a dictionary?', 'When is Python most commonly used?', 'Explain the differnce between a FOR loop and WHILE loop.', 'Explain how classes work in Python, and when you would use them.', 'When is __init__ used?', 'What is the difference between append() and extend()']

JavaScript = ['Explain what Middleware is, and why its used.', 'What is the difference between not defined and undefined?', 'What is the difference between =, ==, and ====?', 'Explain Closure', 'What is a promise?', 'What is a Protoype, and when would you use it?', 'When would you use async/await?', 'What is jQuery?', 'Describe an event loop.', 'what is call/bind/apply?', 'what does NPM stand for?', 'What is V8?', 'What is the difference of LET, VAR, and CONST?', 'Explain the following array methods: MAP, FILTER, FOREACH']

sql = ['What is a relational database?', 'is SQL case sensitive?', 'What does varchar mean?', 'What is the difference between a PRIMARY KEY and a FOREIGN KEY?', 'explain the difference between an inner join, outer join, and a left join', 'what is a constraint?', 'explain what CRUD means', 'what is the difference between these sequelize files: Model/Seed/Migration']

htmlcss = ['Name three different CSS libraries', 'what is the difference between a DIV and a SPAN tag?', 'when is it best to use class and style?', 'what does rgb stand for?', 'it is generally accepted practice for the home page of your html site to be named what?', 'whats the difference between margin and padding?', 'Explain the difference between session storage and local storage.']

react = ['What is REACT?, what are some of its features?','what is JSX?', 'explain State', 'Explain what a component is.', 'what is lifting up state?', 'What is a Reducer?', 'What is a store, and why do you use one?', 'Explain the difference between class based and functional based components.', 'What is Redux DevTools?', 'what is props?', 'Explain what HOOKS are.', '']

general = ['Explain the difference of global and local scope.', 'What is BIG O?', 'explain the process of pushing files to gitHub.', 'Why is it bad to push to main?', 'What are some examples of bad coding practice?', 'explain recursion', 'order these BIG O time from best to worst: Factorial, Linear, Quadratic, Constant', 'what does NPM stand for?', 'Define Object Oriented Programming', 'Explain the difference between cloning a github repository, and forking one.', ]

soft = ['Why do you want to work here?', 'What makes you different from any other applicant for this position?', 'What would you say is your biggest strength?', 'what would you say is your biggest weakness?', 'When you are given a project, what is the first thing you do?', 'tell us about a project you were particularly proud of', 'Describe a time where you overcame significant blockers to finish a project.']

print('************************')
choice()
print('************************')

