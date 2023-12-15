import random

top_of_range = input("Type a number: ")

#making sure the user typed a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)#converting to and integer
    
    if top_of_range <= 0:
        print("PLease use a number larger than zero next time. ")
        quit()
    
else: 
        print("Please type a number next time.")
        quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)#converting to and integer
    
    else: 
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("Great job!")
        break
    elif user_guess > random_number:
            print("Not quite! Too high.")
    else: 
        print("Not quite! Too low.")
        
print("You got it in", guesses, "guesses.")