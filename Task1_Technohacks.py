import random

# List of valid options
options = ["rock", "paper", "scissors"]

# Function to get user choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in options:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")


while True:
    # Randomly select computer's choice
    computer_choice = random.choice(options)

    # Allows you to get the users choice
    user_choice = get_user_choice()

    # Print user and computer choices
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
