# conditional statement

print("Welcome to the Roller coaster")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the Roller coaster!")
    age = int(input("What is your age? "))
    if age > 18:
        bill = 12
    elif 18 > age > 12:
        bill = 7
    else:
        bill = 5

    photo = input("Do you need a photo? (Y/N)")
    if photo == 'Y':
        bill += 6
        print(f"Your total bill is {bill}$")
    else:
        print(f"Your total bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
