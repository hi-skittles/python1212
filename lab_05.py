# Problem 1
print('Problem 1', end='\n\n----------\n')
numbers = [1, 2, 3, 4]  # ??? edit: ohhhhhhhhhh i see aaahaha
mult = 1
for n in numbers:  # previous commit to this file uses range(1, 5) which is what the hard coded version
    mult *= n
print(mult)
print('----------', end='\n\n')

# Problem 2
print('Problem 2', end='\n\n----------\n')
a = 7
z = 15
i = 0
for n in range(a, z):
    print(f'{n}')
    i += n
    # if n == (z - 1):
    #     print(i)  # different way of printing the sum! more roundabout way though...
print(i)
print('----------', end='\n\n')

# Problem 3
print('Problem 3', end='\n\n----------\n')
n = int(input('Enter a number: '))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f'Factorial of {n} is {fact}')
print('----------', end='\n\n')

# Problem 4
print('Problem 4', end='\n\n----------\n')
names = ['Grace Hopper', 'Richard Tapia', 'Timnit Gebru', 'Radia Perlman', 'Ada Lovelace', 'Ruzena Bajcsy', 'four']
f = 0
for name in names:
    f += len(name)
print(f)
print('----------', end='\n\n')

# Problem 5
print('Problem 5', end='\n\n----------\n')
guest_names = ['Grace Hopper', 'Richard Tapia', 'Timnit Gebru', 'Radia Perlman', 'Ada Lovelace', 'Ruzena Bajcsy']
number_of_guests = [2, 3, 1, 2, 2, 1]
for p in range(len(guest_names)):
    print(f'{guest_names[p]}: {number_of_guests[p]}')
print('----------', end='\n\n')

# Problem 6 - Explore More 1
print('Problem 6 - Explore More 1', end='\n\n----------\n')
phrase = input("Enter a phrase to reverse: ")
print(phrase[::-1])
print('----------', end='\n\n')

# Problem 7 - Explore More 2
print('Problem 7 - Explore More 2', end='\n\n----------\n')
prices = [2.99, 240, 100, 31.98, 1099.99]
print(prices[::-1])
print('----------', end='\n\n')
