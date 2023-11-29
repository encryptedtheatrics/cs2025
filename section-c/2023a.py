# Question 16(a)
# Examination Number: 123456
from random import randint

def guess_game(max_guesses_allowed, difficulty):
    if difficulty.lower() == "h":
        max_num = 100
    else:
        max_num = 5
        
    secret_number = randint(1,max_num)
    guess_count = 0
    user_guess = 0
    guessed_nums = []

    # While the user has not guessed the correct number
    while (user_guess != secret_number):
        user_guess = int(input("Enter your guess: "))
        guess_count += 1 # Increase guess_count by 1
        if guess_count == max_guesses_allowed:
            break
        
        elif user_guess in guessed_nums:
            print("You already guessed this number.")
        
        elif user_guess == secret_number:
            print("Congratulations! You win!")
            print("\033[1mYou took {} guesses. \033[0m".format(str(guess_count)))
        
        elif (user_guess > secret_number):
            print("Sorry! Your guess was too high")

        elif (user_guess < secret_number):
            print("Sorry! your guess was too low")

        guessed_nums.append(user_guess)

print("Welcome to the guessing game!")

max_guesses = int(input("Enter the maxiumum number of guesses allowed: "))
difficulty = input("Enter difficulty E(asy) or H(ard)")

guess_game(max_guesses, difficulty)