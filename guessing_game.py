import random

high_score = 1000


def display_welcome():
    print("""=================================
Welcome, Friends, to the Game
      That Never Ends!
    =================================
    """.center(40))
    
    if high_score < 1000:
        print(f"The record thus far is {high_score} guesses.")


def create_target_number(low, high):
    return random.randint(low, high)


def offer_retry():
    keep_playing = input("Would you like to play again?")
    
    if keep_playing.upper() == "Y":
        print("Restarting...")
        start_game()
    elif keep_playing.upper() == "N":
        print("No problem. Have a great day!")
        exit()
    else:
        print("I can only understand 'Y' or 'N'.")
        offer_retry()


def start_game():
    global high_score
        
    low_number = 1
    high_number = 10
    target_number = 0
    total_guesses = 0
    target_number = create_target_number(low_number, high_number)

    display_welcome()

    while True:
        guess = input("Guess a number from 1 - 10:  ")

        try:
            guess = int(guess)
        except ValueError:
            print(
                f"\n'{guess}' is not valid. "
                f"You must guess whole numbers from {low_number} to "
                f"{high_number}.\n\nTry again!"
                )
            continue

        total_guesses += 1
        
        if guess < low_number or guess > high_number:
            print(
                f"\nYour guess must be a number between {low_number} "
                f"and {high_number}. Try again!"
                )
            continue
        elif guess > target_number:
            print(f"\nThe number is lower than {guess}. Try again!")
            continue
        elif guess < target_number:
            print(f"\nThe number is higher than {guess}. Try again!")
            continue
        elif guess == target_number:
            print(
                f"\nYou guessed the number in {total_guesses} tries!\n"
                "You win!"
                )
            break
    if total_guesses < high_score:
        print(f"You've set a new record of {total_guesses} guesses!")
        high_score = total_guesses
        
    offer_retry()

print(__name__)
if __name__ == "__main__":
    try:
        start_game()
    except KeyboardInterrupt:
        print(
            "Oops, your game was interrupted."
            "Please type 'python guessing_game.py to retry.'"
        )
