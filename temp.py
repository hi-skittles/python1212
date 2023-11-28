def foo():
    print("foo")


foo()
run = input("Would you like to run another problem? (y/n): ")
while run == 'y':
    choice = input("Enter a number: ")
    match choice:
        case "1":
            print("True")
        case "2":
            print("False")
        case _:
            foo()
    run = input("Would you like to run another problem? (y/n): ")
