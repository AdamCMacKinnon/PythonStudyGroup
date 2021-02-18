import random

names = ['Adam', 'Ally', 'Andrea', 'Layne', 'Claude']

dare = ['Question', 'Challenge']

language = ['JavaScript/Node', 'SQL', 'Python', 'React', 'Choose!', 'General', 'HTML/CSS', 'Soft Interview']

print('----------------------------------------------')
print('Next up, ' + random.choice(names) + ' with a ' + random.choice(dare) + ' about: ' + random.choice(language))
print('----------------------------------------------')

