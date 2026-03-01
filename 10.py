import random

def get_user_choice():
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()


    def multiplication_table():
        for i in range(1, 11):
            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")
            print()

    multiplication_table()

    def find_smallest_number(numbers):
        if not numbers:
            return None  # Return None if the list is empty
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
        return smallest

    # Example usage
    numbers = [34, 15, 88, 2, 0, -5, 42]
    print(f"The smallest number in the list is: {find_smallest_number(numbers)}")