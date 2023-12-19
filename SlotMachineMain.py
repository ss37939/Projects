#This project will be building a text based slot machine. The user will be able deposit a certain amount 
#of money, and we will allow them to bet on four lines on the slot machine. If they win any lines, we'll 
#multiply their bet by the value of the lines and add that to their value. They may keep playing until
#they want to cash out, or they run out of money.
import random

MAX_LINES = 4 #change this when wanting to change the max number of lines
MAX_BET = 200
MIN_BET = 1

ROWS = 4
COLS = 4

symbol_count = {
    "Star": 2,
    "Triangle": 4,
    "Circle": 6, 
    "Square": 8
}

symbol_value = {
    "Star": 5,
    "Triangle": 4,
    "Circle": 3, 
    "Square": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #every line in the lines
    for line in range(lines):
        #whatever symbol we want to check  is in the first column of the current row
        symbol = columns[0][line]
        #go to each column and check for that symbol
        for column in columns:
            symbol_to_check = column[line]
            #check if the symbols are the same 
            if symbol != symbol_to_check:
                break
            #if they are the same the player wins
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    #defining colums list
    columns = []
    
    #generating colums for every single column we have
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy of all symbols
        for _ in range(rows):
            value = random.choice(current_symbols)#picks a random value from the list
            current_symbols.remove(value)#removes the value so it cannot be picked again
            column.append(value)#adds the value to column
            
        columns.append(column) #adds column to the columns list
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end = " | ")
            else:
                print(column[row], end = "")
                
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        
        #make sure the amount is actually a number
        if amount.isdigit():
            #if the number is valid, we will convert the string to an integer
            amount = int(amount)
            if amount > 0:
                break #breaks the while loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        
        #make sure the amount is actually a number
        if lines.isdigit():
            #if the number is valid, we will convert the string to an integer
            lines = int(lines)
            
            #if lines is greater than or equal to one and less than or equal to the max, break the while loop
            if 1 <= lines <= MAX_LINES:
                break #breaks the while loop
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
            
    return lines

def get_bet():
    while True:
        betAmount = input("How much would you like to bet on each line? $")
        
        #make sure the amount is actually a number
        if betAmount.isdigit():
            #if the number is valid, we will convert the string to an integer
            betAmount = int(betAmount)
            if MIN_BET <= betAmount <= MAX_BET:
                break #breaks the while loop
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
            
    return betAmount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet this amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        enter = input("Press enter to play (q to quit). ")
        if enter == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")
    
main()