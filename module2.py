# print(type('This is a string.'))
# print(type("And so is this."))
# print(type("""and this."""))
# print(type('''and even this...'''))
#
# print(type("17"))
# print(type("3.2"))
#
# print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
# print("""This message will span
# several lines
# of the text.""")
#
# print(42500)
# print(42,500)

current_time_str = input("what is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int

final_answer = final_time_int % 24

print("The time after waiting is: ", final_answer)