from art import logo
import random

numbers = list(range(1, 101))
random_number = int(random.choice(numbers))
# print(random_number)
keep_playing = True
lives = 10

print(logo)
if input("Pick a difficulty: Type 'Easy' or 'Hard': ").lower() == 'easy':
    lives = 10
else:
    lives = 5

guess = int(input("Guess a number between 1 and 100: "))

while keep_playing == True:

    def play_game():
        global lives
        global guess
        global keep_playing

        if lives > 0 and guess == random_number:
            keep_playing = False
            print(f"Correct! The answer was {random_number}! You had {lives} attempts remaining.")

        elif lives > 0 and guess < random_number:
            lives -= 1
            print(f"Too low. You have {lives} attempts remaining.")
            if lives == 0:
                print("You lose. You are out of attempts.")
                return keep_playing == False
            guess = int(input("Guess again: "))
        elif lives > 0 and guess > random_number:
            lives -= 1
            print(f"Too high. You have {lives} attempts remaining.")
            if lives == 0:
                print("You lose. You are out of attempts.")
                return keep_playing == False
            guess = int(input("Guess again: "))
        # elif lives == 0:
        #   keep_playing = False
        #   print("You lose. You are out of attempts.")


    play_game()