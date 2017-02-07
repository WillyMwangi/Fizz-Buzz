# FIZZ BUZZ

# Create a function fizz_buzz
def fizz_buzz(number):
    if number % 15 == 0:
        return "FizzBuzz"

    elif number % 3 == 0:
        return "Fizz"

    elif number % 5 == 0:
        return "Buzz"

    else:
        return number  # When the number is not divisible by 3 or 5, the number itself should be returned