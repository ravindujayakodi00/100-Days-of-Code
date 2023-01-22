import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
image = [rock, paper, scissors]

myChoice = int(input("Enter Your Choice (Rock : 1) (Paper : 2) (Scissors : 3) : "))
if myChoice > 3 or myChoice < 0:
    print("Invalid Number Try Again")
else:
    print(image[myChoice - 1])

    # Computer Choice
    print("Computer Choice: ")
    computerChoice = random.randint(1,3)
    print(image[computerChoice - 1])

    if myChoice == computerChoice:
        print("Draw")
    elif myChoice == 3 and computerChoice == 1:
        print("You Lose")
    elif myChoice == 1 and computerChoice == 3:
        print("You Win")
    elif myChoice < computerChoice:
        print("You Lose")
    elif myChoice > computerChoice:
        print("You Win")
