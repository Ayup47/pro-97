import random

print("Number Guessing Game")

number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")

while chances < 5:
    guess=int(input("Enter Your Guess:"))
    
    if guess == number:
       print("Congratulations YOU WON!!!")
       break
    elif guess < number:
        print("Your Guess was too low: Guess a higher number than", guess)
    else:
        print("Your Guess was too high: Guess a lower number than", guess)
    chances+=1
    
if not chances < 5:
    print("YOU LOSE!! The number is",number)

