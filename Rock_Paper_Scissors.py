import random

def get_computer_choice():
    """Randomly select between 'rock', 'paper', and 'scissors'."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Prompt the user to enter their choice and validate it."""
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "tie"
    
    # Define the winning scenarios
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def play_game():
    """Play until the user or computer gets 5 points."""
    user_score = 0
    computer_score = 0
    rounds = 0
    print("Welcome to Rock, Paper, Scissors! First to 5 points wins.")
    
    while user_score < 5 and computer_score < 5:
        rounds += 1
        print(f"\nRound {rounds}:")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")
    
    # Final result
    if user_score == 5:
        print("\nCongratulations! You won the game!")
    else:
        print("\nComputer wins the game! Better luck next time!")

if __name__ == "__main__":
    play_game()
