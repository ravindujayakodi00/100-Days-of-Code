#Write your code below this row 👇

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        number = str(number)
        number = "FizzBuzz"
    elif number % 3 == 0:
        number = str(number)
        number = "Fizz"
    elif number % 5 == 0:
        number = str(number)
        number = "Buzz"
    print(number)