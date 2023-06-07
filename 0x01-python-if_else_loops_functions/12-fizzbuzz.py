#!/usr/bin/python3
def fizzbuzz():
    for fib in range(1, 101):
        if fib % 3 == 0 and fib % 5 != 0:
            print('Fizz', end=' ')
        elif fib % 5 == 0 and fib % 3 != 0:
            print('Buzz', end=' ')
        elif fib % 3 == 0 and fib % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print(fib, end=' ')
