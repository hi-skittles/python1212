# print("Hello World!")
# print(5 + 5)
# print("Another string")

subTotal = input("What is the subtotal? ")
tax = 0.08 * float(subTotal)
total = tax + float(subTotal)
print("The tax is: " + str(tax))
print("The total is: " + str(total))