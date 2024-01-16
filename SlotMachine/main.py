import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { 
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

        return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items() gives you both the key and the value associated with a dictionary
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice (all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: #if i is not equal to the maximum index... if we have a list of 3 items, the maximum index is 2.
                print(column[row], end=" | ") #end tells the print statement what to end the line with, by default it's \n
            else:
                print(column[row], end="")

        print() #print new line



def deposit():
    while True:
        amount = input("What would you like to deposit? $") 
        if amount.isdigit(): #check if enetered a valid number
            amount = int(amount) #input comes as string, so we need to convert it to int
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
                print("Please enter a number.")
        
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") #convert MAX-LINES into a string, concatenate
        if lines.isdigit(): 
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
        
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $") 
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}") #f string to embed values in your string using {}
        else:
            print("Please enter a number.")
        
    return amount
    

    
     

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won! ${winnings}" )
    print(f"You won on lines:", *winning_lines)

main()

