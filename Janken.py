import random

user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    
    # This line is asking for user input and changes the input to ll lowercase letters in case the user enters uppercase
    user_input = input("Type Rock, Paper, Scissors or Q to quit: ").lower()
    if user_input== "q": # This exits the while loop if the user wants to quit
        break
    
    if user_input not in options:
        print("Not Valid")
        continue # continues to ask for an input until correct
    
    random_num = random.randint(0, 2) # rock: 0, paper: 1, scissors: 2
    
    comp_pick = options[random_num] # sets computers pick to a random option
    print("The computer picked", comp_pick + ".")
    
    if user_input == "rock" and comp_pick == "scissors":
        print("Winner Winner Chicken Dinner")
        user_wins += 1 #increases user score
        
    elif user_input == "paper" and comp_pick == "rock":
        print("Winner Winner Chicken Dinner")
        user_wins += 1 #increases user score
        
    elif user_input == "scissors" and comp_pick == "rock":
        print("Winner Winner Chicken Dinner")
        user_wins += 1 #increases user score
    
    elif user_input == "scissors" and comp_pick == "scissors":
        print("Tie!")
    
    elif user_input == "rock" and comp_pick == "rock":
        print("Tie!")
    
    elif user_input == "paper" and comp_pick == "paper":
        print("Tie!")
    
    else:
        print("Loser!")
        comp_wins += 1

print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
print("Goodbye!")