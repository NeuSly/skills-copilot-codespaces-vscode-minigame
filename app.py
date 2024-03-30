import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ["rock", "r", "paper", "p", "scissors", "s"]:
            return choice if len(choice) > 1 else {"r": "rock", "p": "paper", "s": "scissors"}[choice]
        else:
            print("Invalid choice. Please try again.")

def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "tie"
    elif (user_choice == "rock" and ai_choice == "scissors") or \
         (user_choice == "paper" and ai_choice == "rock") or \
         (user_choice == "scissors" and ai_choice == "paper"):
        return "user"
    else:
        return "ai"

def play_game():
    user_score = 0
    ai_score = 0

    while True:
        user_choice = get_user_choice()
        ai_choice = get_ai_choice()

        print(f"You chose {user_choice}. AI chose {ai_choice}.")

        winner = determine_winner(user_choice, ai_choice)

        if winner == "user":
            print("You won!")
            user_score += 1
        elif winner == "ai":
            print("You lost!")
            ai_score += 1
        else:
            print("It's a tie!")

        print(f"Score: You {user_score} - {ai_score} AI")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            break

    print(f"Final score: You {user_score} - {ai_score} AI")

play_game()