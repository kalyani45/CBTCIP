import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_user_choice():
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        user_input = input("Enter rock, paper, or scissors: ").lower()
    return user_input


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print("\n" + "AESTHETIC BLOB " * 3 + "ROCK PAPER SCISSOR GAME" + " AESTHETIC BLOB" * 3 + "\n")
    print("Winning Rules:\n")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
