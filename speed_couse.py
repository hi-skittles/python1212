def test(i):
    try:
        i = int(i)
        pass
    except ValueError:
        raise TypeError("Input must be an integer")
    if 0 < i < 10:
        print(i)
        return True
    else:
        print("Number is not in range")
        return False


inp = input("Enter a number: ")
result = test(inp)
while not result:
    inp = int(input("Enter a number: "))
    result = test(inp)
else:
    print("Number is in range")
