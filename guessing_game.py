import random

high_score = 1000

def display_welcome():
    print("""=================================
Welcome, Friends, to the Game
      That Never Ends!
    =================================
    """.center(40))
    
    if high_score < 1000:
        print("The record thus far is {} guesses.".format(high_score))

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
            print("\n'{}' is not valid. You must enter only whole numbers from {} to {}.\n\nTry again!".format(guess, low_number, high_number))
            continue

        total_guesses += 1
        
        if guess < low_number or guess > high_number:
            print("\nYour guess must be a number between {} and {}. Try again!".format(low_number, high_number))
            continue
        elif guess > target_number:
            print("\nThe number is lower than {}. Try again!".format(guess))
            continue
        elif guess < target_number:
            print("\nThe number is higher than {}. Try again!".format(guess))
            continue
        elif guess == target_number:
            print("\nYou guessed the number in {} tries!\nYou win!".format(total_guesses))
            break
    if total_guesses < high_score:
        print("You've set a new record of {} guesses!".format(total_guesses))
        high_score = total_guesses
        
    offer_retry()
    
start_game()
