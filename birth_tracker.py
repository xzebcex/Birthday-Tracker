# Birthday Tracker

import sys

birthdays = {'Aiden': 'Apr 1', 'Bella': 'Dec 12',
             'Owen': 'Mar 4', 'Harper': 'Dec 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')

print('Exiting program...')
sys.exit()
