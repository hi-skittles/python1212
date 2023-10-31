RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"

# Problem 1
def one():
    print('Problem 1', end='\n\n----------\n')
    eng2sp = dict({'one': 'uno'})
    eng2sp['two'] = 'dos'
    print(eng2sp)
    print('----------', end='\n\n')


# Problem 2
def two():
    """
    Returns each guest's name that is bringing more than one guest.

    :return: list
    """
    print('Problem 2', end='\n\n----------\n')
    guests = {'Grace Hopper': 2, 'Richard Tapia': 3, 'Timnit Gebru': 1, 'Radia Perlman': 4, 'Ada Lovelace': 2,
              'Ruzena Bajcsy': 1}
    more_than_1 = [guest for guest in guests if guests[guest] > 1]
    # more_than_1 = [guest for guest, count in guests.items() if count > 1]  # alternate response
    print(more_than_1)
    print('----------', end='\n\n')


# Problem 3
def three():
    print('Problem 3', end='\n\n----------\n')
    words = input("Enter text to analyze: ").lower()
    stored = dict()
    stored = {letter: words.count(letter) for letter in words if letter.isalpha()}  # concise
    print(f'stored: {stored}')
    print('----------', end='\n\n')


# Problem 4
def four():
    print('Problem 4', end='\n\n----------\n')
    word_synonyms = {
        'travel': ['journey', 'go', 'jaunt', 'move_around', 'move', 'locomote', 'change_of_location', 'traveling',
                   'locomotion', 'trip'],
        'computer': ['data_processor', 'computing_machine', 'information_processing_system', 'calculator',
                     'electronic_computer', 'estimator', 'figurer', 'computing_device', 'reckoner'],
        'learn': ['hear', 'acquire', 'pick_up', 'teach', 'take', 'check', 'instruct', 'discover', 'read', 'get_a_line',
                  'study', 'find_out', 'determine', 'ascertain', 'memorize', 'watch', 'see'],
        'excited': ['shake_up', 'emotional', 'activated', 'frantic', 'energize', 'mad', 'charge_up', 'stimulate',
                    'worked_up', 'stir', 'charge', 'delirious', 'shake', 'agitate', 'wind_up', 'unrestrained']}
    query = input("Enter a word to search for: ")
    if query in word_synonyms:
        callback = ', '.join(word_synonyms[query])
        print(f'Synonyms for {GREEN}{query}{RESET}: {callback}')
    else:
        print(f'"{RED}{query}{RESET}" does not exist in the list.')
    print('----------', end='\n\n')


# Problem 5
def five():
    print('Problem 5', end='\n\n----------\n')
    message_count = {}


question = input('Which problem would you like to run?: ')
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
        case _:  # default
            print('Invalid problem number.')