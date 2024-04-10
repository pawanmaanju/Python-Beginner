import random

# Generate a random number
target_number = random.randint(1, 99)

# Loop until the user guesses the correct number
while True:
    # Take input from the user
    guess = int(input("Enter your guess (1-99): "))

    # Check if the guess is correct
    if guess == target_number:
        print("Congratulations! You guessed the right number.")
        print("You are the winner!")
        break
    elif guess < target_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
