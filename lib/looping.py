#!/usr/bin/env python3

def happy_new_year():
    i=10 
    while i>=1:
     if(i ==1):
       print(i)
       print("Happy New Year!")
     else:
       print(i)
     i-=1

def square_integers(int_list):
    numbers = []
    for num in int_list:
        number = num ** 2
        numbers.append(number)
    return numbers  

 

def fizzbuzz():
    i = 1  
    while i <= 100:
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
        i += 1


