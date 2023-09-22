# Problem 1
# you could use a while loop here. oh well todo while loop i guess
print('Problem 1', end='\n\n----------\n')
st = input('Enter a string: ')
if len(st) < 5:
    print('Your string is too short.')
elif len(st) > 5:
    len = len(st)
    third = st[2]
    scLs = st[-2]
    first5 = st[:5]
    allTwo = st[:-2]
    print(f'Length of string: {len}\nThird character: {third}\nSecond to last character: {scLs}\nFirst five characters: {first5}\nAll but last two characters: {allTwo}')
print('----------', end='\n\n')

# Problem 2
print('Problem 2', end='\n\n----------\n')
items = "pencils, pens, paper, erasers, staples, binders"
itemsList = items.split(', ')
print(f'Original list: {itemsList}')
print(f'First item: {itemsList[0]}\nLast item: {itemsList[-1]}\nFirst three items: {itemsList[:3]}\nLast item: {itemsList[-1]}\nLast three items: {itemsList[-3:]}\nEvery second item: {itemsList[::2]}\nEvery second item, starting with the second: {itemsList[1::2]}\nReverse the list: {itemsList[::-1]}')
print('----------', end='\n\n')

# Problem 3
print('Problem 3', end='\n\n----------\n')
fruits_str = "apple - banana - orange - lemon - mango"
fruits = fruits_str.split(' - ')
print(f'Original list: {fruits}')
print(f'First item: {fruits[0]}\nLast item: {fruits[-1]}\nFirst three items: {fruits[:3]}\nLast item: {fruits[-1]}\nLast three items: {fruits[-3:]}\nEvery second item: {fruits[::2]}\nEvery second item, starting with the second: {fruits[1::2]}\nReverse the list: {fruits[::-1]}')
print('----------', end='\n\n')

# Problem 4
print('Problem 4', end='\n\n----------\n')
items = ["raindrops", "roses", "whiskers", "kittens", "kettles", "mittens"]
favourite_things = ", ".join(items)
print(f'To string: {favourite_things}\nType: {type(favourite_things)}')
print('----------', end='\n\n')

# Problem 5
print('Problem 5', end='\n\n----------\n')
names = ['Emma Watson', 'Geraldine Somerville', 'Rupert Grint', 'Devon Murray', 'Tom Felton', 'Daniel Radcliffe', 'Warwick Davis', 'Stan Lee', 'Mark Williams', 'Adrian Rawlins', 'Kenny Baker', 'David Bradley', 'Ian McDiarmid', 'Hugo Weaving', 'David Schofield', 'Orlando Bloom', 'Mike Myers', 'Tyrese Gibson', 'Greg Ellis', 'Kellan Lutz', 'Julie Walters', 'Karl Urban', 'Will Smith', 'Bernard Hill', 'Anna Kendrick', 'John Ratzenberger', 'Mackenzie Crook', 'Josh Duhamel', 'Bryce Dallas Howard', 'Mickie McGowan', 'Bill Farmer', 'Robert Hardy', 'Martin Klebba', 'Jack Angel', 'Shia LaBeouf', 'Ken Jeong', 'Debi Derryberry', 'CCH Pounder', 'Wes Studi', 'Peter Cullen', 'Michelle Rodriguez', 'Billy Burke', 'Bob Bergen', 'Phil Proctor', 'Elizabeth Reaser', 'Alan Rickman', 'Frank Oz', 'Sherry Lynn', 'Kevin McNally', 'Bonnie Hunt', 'Seth Rogen', 'Verne Troyer', 'Andy Serkis', 'Eddie Murphy', 'Marton Csokas', 'Clark Gregg', 'Tom Cruise', 'Tom Hanks', 'Robbie Coltrane', 'Julie Andrews', 'Geraldine James', 'Alan Tudyk', 'Steve Carell', 'Keira Knightley', 'Leonard Nimoy', 'Gary Oldman', 'Mark Hamill', 'Harrison Ford', 'Cillian Murphy', 'Tim Allen', 'Zoe Saldana', 'Cameron Diaz', 'Tobey Maguire', 'Jason Isaacs', 'Wayne Knight', 'Hugh Jackman', 'Sam Worthington', 'Temuera Morrison', 'Jim Cummings', 'Peter Facinelli', 'Julian Glover', 'Brad Garrett', 'Cameron Bright', 'Christopher Lee', 'Eric Bana', 'Oliver Ford Davies', 'Laz Alonso', 'Maggie Smith', 'Sayed Badreya', 'Michael Papajohn', 'Richard Griffiths', 'Haley Joel Osment', 'Naomie Harris', 'Bradley Cooper', 'Jon Favreau', 'Elizabeth Banks', 'Cheri Oteri', 'Gemma Jones', 'Alec Guinness', 'Dwayne Johnson']
last = names[-1]#.split(' ')[-1] # okay if you interpret it as get EVERY LAST NAME, this would suffice.
second_last = names[-2]#.split(' ')[-2] # and this would get their first name. that's not what it's asking for, but it's here anyways because it piqued my interest :)
print(f'Last name: {last}\nSecond last name: {second_last}')
print('----------', end='\n\n')

# Problem 6
print('Problem 6', end='\n\n----------\n')
ids = [1231, 1423, 1212, 1331, 1532, 1207, 1145, 1012]
makes = ['Maserati', 'Honda', 'Subaru', 'Fiat', 'Ford', 'Porsche', 'Ford', 'Lotus']
years = ['2004', '1989', '2002', '2016', '2008', '1970', '1926', '2011']
entry = int(input('Enter an ID: '))
# todo loop this? could. should? maybe.
if ids.index(entry):
    index = ids.index(entry)
    print(f'ID: {entry}\nMake: {makes[index]}\nYear: {years[index]}')
else:
    print('ID not found.')
print('----------', end='\n\n')