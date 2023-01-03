#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is less than 6 and not 0"
str5 = "and is 0"
if number < 0:
    digit = ((-1) * number) % 10
    digit = (-1) * digit
    if digit > 5:
        print(str1, number, str2, digit, str3)
    elif digit != 0 and digit < 6:
        print(str1, number, str2, digit, str4)
elif number > 0:
    digit = number % 10
    if digit > 5:
        print(str1, number, str2, digit, str3)
    elif digit != 0 and digit < 6:
        print(str1, number, str2, digit, str4)
else:
    digit = 0
    print(str1, number, str2, digit, str5)
