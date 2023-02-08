number = int(input("Enter Number: "))
is_prime = True

for x in range(2,number):
    if number % x == 0:
        is_prime = False

if is_prime == True:
    print("This is a Prime Number")
else:
    print("Not a prime number")