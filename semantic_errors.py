num1 = input('Enter a number:')
num2 = input('Enter another number:')
sum = num1 + num2

print('The sum of', num1, 'and', num2, 'is', sum)

num1 = input('Enter a number:')
num2 = input('Enter another number:')
sum = int(num1) + int(num2)

print('The sum of', num1, 'and', num2, 'is', sum)

#  type error
a = input('wpisz godzine')
x = input('wpisz liczbe godzin')
a = int(a)
x = int(x)
h = x // 24
s = x % 24
print (h, s)
a = a + s
print ('godzina teraz', a)


# name error
str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wai_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
