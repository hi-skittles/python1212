# Problem 1
def one():
    


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
        case _:  # default
            print('Invalid problem number.')
else:
    print('Invalid problem number.')