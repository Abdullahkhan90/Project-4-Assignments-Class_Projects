import random


NUM_ROUNDS = 5  

def main():
  
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    
    score = 0

    # Loop through the rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers for the user and the computer
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Show the user's number (but not the computer's)
        print(f"Your number is {user_number}")
        
        # Get user's guess for higher or lower
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Ensure input is valid (either "higher" or "lower")
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Check if the guess is correct and update the score
        if guess == "higher" and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif guess == "lower" and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            if user_number == computer_number:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Print the score after each round
        print(f"Your score is now {score}")
        print()  # Blank line between rounds

    # End of the game
    print("Thanks for playing!")

    # Display the final score with conditional ending messages
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
