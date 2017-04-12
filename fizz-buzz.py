# given a number return "Fizz Buzz" if its divisable by 3 and 5
# "fizz" if divisible by 3
# "buzz" if divisible by 5
# the number as a string otherwise

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)