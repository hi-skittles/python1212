# going to try functions cuz there's a lot of problems today

# Problem 1
def one():
    print('Problem 1', end='\n\n----------\n')
    it = input('Enter a number: ')
    if it.isdigit():
        it = int(it)
        if it % 2 == 0:
            print('Even')
        else:
            print('Odd')
    else:
        print('Not a valid number.')
    print('----------', end='\n\n')


# Problem 2
def two():
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
def three():
    print('Problem 3', end='\n\n----------\n')
    age = input('Enter your age: ')
    if age.isdigit():
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
def four():
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
        print('Input not valid number.')
    print('----------', end='\n\n')


# Problem 5
def five():
    print('Problem 5', end='\n\n----------\n')
    pw1 = input('Enter a password: ')
    pw2 = input('Enter a password again: ')
    if pw1 == pw2:
        print('Passwords match. User logged in.')
    else:
        print('Passwords don’t match. Try again!')
    print('----------', end='\n\n')


# Problem 6
def six():
    print('Problem 6', end='\n\n----------\n')
    strin = input('Enter a string: ')
    strin = strin.lower()
    strin = strin[0]
    match strin:
        case 'a':
            print('Vowel')
        case 'e':
            print('Vowel')
        case 'i':
            print('Vowel')
        case 'o':
            print('Vowel')
        case 'u':
            print('Vowel')
        case _:  # default
            print('Consonant')
    print('----------', end='\n\n')


# Problem 7
def seven():
    print('Problem 7', end='\n\n----------\n')
    a = 6
    z = 26
    for _ in range(a, z + 1):
        if _ % 2 == 0:
            continue
        else:
            print(_)
    print('----------', end='\n\n')


# Problem 8
def eight():
    print('Problem 8', end='\n\n----------\n')
    work_hours = float(input("Enter the number of hours worked this week: "))
    hourly_wage = float(input("Enter your hourly rate: "))
    overtime = 0
    if work_hours > 40:
        overtime = work_hours - 40
        work_hours = 40
    pay = (work_hours * hourly_wage)
    pay += (overtime * (hourly_wage * 1.5))
    print(f"""You worked {work_hours} this week, with {overtime} hour(s) of overtime. This earned you ${pay}.""")
    print('----------', end='\n\n')


# Problem 9
def nine():
    print('Problem 9', end='\n\n----------\n')
    words = ["apple", "banana", "chocolate", "elephant", "giraffe", "hamburger", "kangaroo", "lemon", "octopus",
             "penguin",
             "panda", "strawberry", "tiger", "umbrella", "watermelon"]
    word = input("Enter a word to search for: ")
    if word in words:
        print(f"""Query "{word}" exists in the list.""")
    elif word not in words:
        print(f"""Query "{word}" does not exist in the list.""")
    print('----------', end='\n\n')


# Problem 10
def ten():
    print('Problem 10', end='\n\n----------\n')
    numbers = [39, 72, 16, 89, 4, 57, 61, 98, 27, 12, 33, 68, 6, 55, 91]
    for _ in range(len(numbers)):
        if _ % 2 == 0:
            print(numbers[_])
    print('----------', end='\n\n')


# Problem 11
def eleven():
    print('Problem 11', end='\n\n----------\n')
    numbers = [39, 72, 16, 89, 4, 57, 61, 98, 27, 12, 33, 68, 6, 55, 91, 50, 100]
    target_number = 50
    ans = 0
    for _ in range(len(numbers)):
        if numbers[_] % target_number == 0:
            ans += numbers[_]
    print(ans)
    print('----------', end='\n\n')

# Problem 12
def twelve():
    guest_names = ['Grace Hopper', 'Richard Tapia', 'Timnit Gebru', 'Radia Perlman', 'Ada Lovelace', 'Ruzena Bajcsy']
    number_of_guests = [2, 3, 1, 4, 2, 1]
    for p in range(len(guest_names)):
        if number_of_guests[p] > 1:
            print(guest_names[p])
    print('----------', end='\n\n')


question = input('Which problem would you like to run? ')
if question.isdigit():
    match question:
        case '1':
            one()
        case '2':
            two()
        case '3':
            three()
        case '4':
            four()
        case '5':
            five()
        case '6':
            six()
        case '7':
            seven()
        case '8':
            eight()
        case '9':
            nine()
        case '10':
            ten()
        case '11':
            eleven()
        case '12':
            twelve()
        case _:  # default
            print('Invalid problem number.')
else:
    print('Invalid problem number.')
