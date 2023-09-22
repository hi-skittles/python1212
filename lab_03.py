# Problem 1
print('Problem 1', end='\n\n----------\n')
print('''Welcome to ITSC 1212!''')
print('----------', end='\n\n')


# Problem 2
print('Problem 2', end='\n\n----------\n')
dog_year = input("Please provide your dog's age: ")
to_human = int(dog_year) * 7
print("""Your dog's age is equivalent to {0} human years""".format(to_human))
print('----------', end='\n\n')


# Problem 3
print('Problem 3', end='\n\n----------\n')
from statistics import fmean as mean
x = float(input('Enter a number: '))
y = float(input('Enter a second number: '))
z = mean([x, y])
print('The average of the two numbers you have entered is:', z)
print('----------', end='\n\n')


# Problem 4
print('Problem 4', end='\n\n----------\n')
num = float(input('Enter a number: '))
num2 = float(input('Enter a second number: '))
num += num2
print(f'The sum of the two numbers you have entered is: {num}')
print('----------', end='\n\n')


# Problem 5
print('Problem 5', end='\n\n----------\n')
import random as ps_random
from secrets import SystemRandom

random = SystemRandom().randrange(0, 1000)
print(f'SystemRandom: {random}')
ps_random = ps_random.randrange(0, 1000)
print(f'Pseudo-random: {ps_random}')
print('----------', end='\n\n')


# Problem 6
print('Problem 6', end='\n\n----------\n')
import math as m

# cube, root, ceil
# cube me then root me then ceil me
x = float(input('Enter a number: '))
x = pow(x, 3)
x = m.sqrt(x)
x = m.ceil(x)
print(f'The cubed, rooted, rounded result of the number you have entered is: {x}')
print('----------', end='\n\n')
