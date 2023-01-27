def greet(name):
    print(f"Hello {name}")

# greet("Ravindu")

# Key word arguments

def greetWith(location, name):
    print(f"Hello {name} How is it going in {location}")

# greetWith(location="Kandy" , name="Ravindu")

# prime number checker
def prime_checker(number):
    is_prime = True
    for x in range (2,number):
        if number % x == 0:
            is_prime = False
    if is_prime == True:
        print("This is a Prime Number")
    else:
        print("This is not a prime number")

number = int(input("Enter a Number: "))
prime_checker(number)
