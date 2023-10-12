# Problem 1
def one():
    print('Problem 1', end='\n\n----------\n')
    awards = ['Emmy', 'Tony', 'Academy', 'Grammy', 'Oscar']
    if 'Tony' in awards:
        print(f"Tony is in the list, at position {awards.index("Tony")}")
    else:
        print("Tony is not in the list.")
    print('----------', end='\n\n')


# alternate to problem one
def one_alt():
    print('Problem 1', end='\n\n----------\n')
    awards = ['Emmy', 'Tony', 'Academy', 'Grammy', 'Oscar']
    word = input("Enter a word to search for: ")
    (lambda word: print(f"""Query "{word}" exists in the list.""") if word in awards else print(
        f"""Query "{word}" does not exist in the list."""))(word)
    print('----------', end='\n\n')


# Problem 2
def two():
    print('Problem 2', end='\n\n----------\n')
    # override list literal
    my_friends = []
    my_friends.append("friend1")
    my_friends.append("friend2")
    my_friends.append("friend3")
    my_people = []
    my_people = my_friends.copy()
    my_people.append("person1")
    my_people.append("person2")
    print(f"my_friends: {my_friends}")
    print(f"my_people: {my_people}")
    print('----------', end='\n\n')


# Problem 3
def three():
    print('Problem 3', end='\n\n----------\n')
    words = ["read", "work", "walk", "watch", "drink", "surf"]
    wordings = []
    for word in words:
        wordings.append(word + "ing")
    print(f"words: {words}")
    print(f"wordings: {wordings}")
    print('----------', end='\n\n')


# Problem 4
def four():
    print('Problem 4', end='\n\n----------\n')
    numbers = [71, 96, 88, 76, 39, 34, 17, 88, 40, 69, 51, 23, 84, 74, 14, 84, 20, 63, 37]
    sqrts = []
    s = lambda x: x ** 0.5
    for _ in numbers:
        sqrts.append(s(_))
    print(f"numbers: {numbers}")
    print(f"roots: {sqrts}")
    print('----------', end='\n\n')


# Problem 5
def five():
    print('Problem 5', end='\n\n----------\n')
    words = ['Work', 'had', 'been', 'piling', 'up', 'lately', '.', 'Work,', 'work,', 'and', 'more', 'work', 'seemed',
             'to', 'be', 'the', 'theme', 'of', 'the', 'day', '.', 'Day', 'turned', 'into', 'night', ',', 'and', 'work',
             'is', 'still', 'piling', 'up', '.']
    stri = ""
    for _ in words:
        stri += " " + _
    print(stri)
    print('----------', end='\n\n')


# Problem 6
def six():
    print('Problem 6', end='\n\n----------\n')
    star_wars = ["Leia", "Han Solo", "Yoda", "Luke", "C3PO", "R2D2"]
    del star_wars[2]
    print(star_wars)
    print('----------', end='\n\n')


# Problem 7
def seven():
    print('Problem 7', end='\n\n----------\n')
    cats = [8, 6, 8, 4, 9, 34, 7]
    dogs = [5, 23, 14, 30, 10, 15, 7]
    cats.sort(reverse=True)
    cats.insert(1, int(input("Enter the number of cats a new shelter has: ")))
    dogs.insert(0, int(input("Enter the number of dogs a new shelter has: ")))
    pets = []
    for _ in range(len(cats)):
        pets.append(cats[_] + dogs[_])
    print(f"cats: {cats}")
    print(f"dogs: {dogs}")
    print(f"pets: {pets}")
    i = 0
    for _ in range(len(pets)):
        i += pets[_]
    print(i)
    print('----------', end='\n\n')


# Problem 8
def eight():
    print('Problem 8', end='\n\n----------\n')
    my_str = "The daisies are prettier in the early spring"
    my_list = [3, 9, -32, 53, 54, 17, 63, 63, 95, -16, 38, -15]
    e_count = my_str.count('e')
    pos_average = [number for number in my_list if number > 0]
    pos_average = sum(pos_average) / len(pos_average)
    print(f"Number of e's: {e_count}")
    print(f"Average of positive numbers: {pos_average}")
    name = input("Enter your name: ")
    print("\n".join(name[::-1]))
    print('----------', end='\n\n')


# Problem 9
def nine():
    print('Problem 9', end='\n\n----------\n')
    presidents = ["Washington, George, 2/22/1732, 12/14/1799", "Adams, John, 10/30/1735, 7/4/1826",
                  "Jefferson, Thomas, 4/13/1743, 7/4/1826", "Madison, James, 3/16/1751, 6/28/1836",
                  "Monroe, James, 4/28/1758, 7/4/1831"]
    for _ in presidents:
        _ = _.split(', ')
        print(f"{_[1]} {_[0]} ({_[2]} - {_[3]})")
    print('----------', end='\n\n')


question = input('Which problem would you like to run?: ')
# if question.isdigit():
match question:
    case '1':
        one()
    case '1a':
        one_alt()
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
    case _:  # default
        print('Invalid problem number.')
# else:
#     print('Invalid problem number.')
