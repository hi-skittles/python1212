# functions
import os


# Problem 1
def one():
    print('Problem 1', end='\n\n----------\n')
    x_coordinate = []
    y_coordinate = []
    appendxy = lambda x, y: (x_coordinate.append(x), y_coordinate.append(y))
    with open('./lab_08/xy.txt', 'r') as f:
        for line in f:
            x, y = line.split(',')
            appendxy(float(x), float(y))
    print(f'x_coordinate: {x_coordinate}\nlength: {len(x_coordinate)}\ntype: {type(x_coordinate[0])}')
    print(f'y_coordinate: {y_coordinate}\nlength: {len(y_coordinate)}\ntype: {type(y_coordinate[0])}')
    print('----------', end='\n\n')


# Problem 2
def two():
    print('Problem 2', end='\n\n----------\n')
    file = './lab_08/scarlet.txt'
    with open(file, 'r') as f:
        text = f.read()
        lines = text.split('\n')
        occurrences = lambda word: text.lower().count(word)
        red = occurrences(' red ')
        scarlet = occurrences('scarlet')
        red_lines = [line for line in lines if 'red' in line.lower()]
        scarlet_lines = [line for line in lines if 'scarlet' in line.lower()]
        reds_list = [lines.index(index) for index in red_lines]
        scarlets_list = [lines.index(index) for index in scarlet_lines]
        print(f'{reds_list[:2]}...{reds_list[-2:]}\n{scarlets_list[:2]}...{scarlets_list[-2:]}')
        print(f'Number of times "red" appears: {red}\nNumber of times "scarlet" appears: {scarlet}')
    print('----------', end='\n\n')


# Problem 3
def three():
    print('Problem 3', end='\n\n----------\n')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    # store the contents of the list months to a new text file called months.txt
    with open('./lab_08/months.txt', 'w') as f:
        for month in months:
            if month == months[-1]: f.write(month)
            else: f.write(month + '\n')
    # read the contents of the file months.txt and store it in a list called months_list
    with open('./lab_08/months.txt', 'r') as f:
        months_list = f.read().split('\n')
    # print the contents of the list months_list
    print(months_list)
    # test if file was created?
    if os.path.exists('./lab_08/months.txt'):
        print('program success')
    print('----------', end='\n\n')


# Problem 4
def four():
    print('Problem 4', end='\n\n----------\n')
    # ./lab_08/words5000.csv
    file = input('Enter file name: ')
    if os.path.exists(file):
        try:
            file = open(file, 'r')
        except FileNotFoundError:
            print('File not found.')
            print('----------', end='\n\n')
            return
        file = file.read()
        query = input('Enter a word to search for: ')
        is_invalid_query = any(_.isdigit() for _ in query)
        if not is_invalid_query and query.lower() in file:
            print(f'"{query}" exists in the list.')
        else:
            print(f'"{query}" does not exist in the list, or the query is invalid.')
    else:
        print('File not found.')
    print('----------', end='\n\n')


question = input('Which problem would you like to run?: ')
# if question.isdigit():
match question:
    case '1':
        one()
    case '2':
        two()
    case '3':
        three()
    case '4':
        four()
    case _:  # default
        print('Invalid problem number.')