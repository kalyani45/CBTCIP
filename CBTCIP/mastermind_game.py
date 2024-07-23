def get_valid_number(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return num
        else:
            print("Invalid input. Please enter a valid multi-digit number.")


def get_valid_guess(length):
    while True:
        guess = input(f"Enter your guess ({length} digits): ")
        if guess.isdigit() and len(guess) == length:
            return guess
        else:
            print(f"Invalid input. Please enter a {length}-digit number.")


def provide_hint(secret, guess):
    correct_digits = sum(s == g for s, g in zip(secret, guess))
    return correct_digits


def play_round(player_number, secret_length):
    secret = get_valid_number(f"Player {player_number}, enter your secret number: ")
    print("\n" * 50)  # Clear screen
    attempts = 0
    while True:
        attempts += 1
        guess = get_valid_guess(len(secret))
        if guess == secret:
            print(f"Correct! Player {player_number % 2 + 1} guessed the number in {attempts} attempts.\n")
            return attempts
        else:
            correct_digits = provide_hint(secret, guess)
            print(f"{correct_digits} digit(s) are correct.")


def main():
    print("Welcome to the Mastermind Game!\n")

    attempts_player1 = play_round(1, secret_length=None)
    attempts_player2 = play_round(2, secret_length=None)

    if attempts_player2 < attempts_player1:
        print("Player 2 wins the game and is crowned Mastermind!")
    elif attempts_player2 > attempts_player1:
        print("Player 1 wins the game and is crowned Mastermind!")
    else:
        print("It's a tie! Both players took the same number of attempts.")


if __name__ == "__main__":
    main()
