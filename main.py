import random

random_number = random.randint(1, 100)
guess_chances = 10
is_playing = True

while guess_chances > 0 and is_playing:
    print(f"Your guess count is : {guess_chances}")
    guess_number = int(input("Please guess the random number : "))
    guess_chances -= 1
    if guess_number == random_number:
        print(f"You win!!\nThe guess number is {guess_number}")
        is_playing = False
    elif guess_number > random_number:
        print("Too high!\nPlease try again\n")
    else:
        print("Too low\nPlease try again\n")

if guess_chances == 0:
    print("You lose!!!")
