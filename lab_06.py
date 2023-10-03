# gonna try functions cuz theres a lot of problems today

# Problem 1
print('Problem 1', end='\n\n----------\n')
it = input('Enter a number: ')
if isinstance(it, int):
    it = int(it)
    if it % 2 == 0:
        print('Even')
    else:
        print('Odd')
else:
    print('Not a valid number.')
print('----------', end='\n\n')

# Problem 2
print('Problem 2', end='\n\n----------\n')
it = input('Enter a number: ')
it = int(it)
if it > 0:
    print(1)
elif it < 0:
    print(-1)
else:
    print(0)
print('----------', end='\n\n')

# Problem 3
print('Problem 3', end='\n\n----------\n')
age = input('Enter your age: ')
if isinstance(age, int):
    age = int(age)
    if age >= 18:
        print('You can vote.')
    elif age in range(1, 18):
        print('Too young to vote.')
    else:
        print('You are a time traveler!')
else:
    print('Input not valid number.')
print('----------', end='\n\n')

# Problem 4
print('Problem 4', end='\n\n----------\n')
messages = ['eleven', 'twelve', 'thirteen', 'fourteen']
num = input('Enter a number between 1-4: ')
if num.isdigit():
    num = int(num)
    if num in range(1, 5):
        print(messages[num - 1])
    else:
        print('Number not in range.')
else:
    print('Input not number.')
print('----------', end='\n\n')

# Problem 5