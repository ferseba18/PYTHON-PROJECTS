import random

# Constants
MAX_SLOTS = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {
    'Cherry': 0,
    'Lemon': 0,
    'Orange': 1,
    'Plum': 1,
    'Bell': 2,
    'Drink': 2,
    'Coin': 3,
    'Seven': 4
}
symbol_value = {
    'Cherry': 2,
    'Lemon': 2,
    'Orange': 3,
    'Plum': 3,
    'Bell': 4,
    'Drink': 4,
    'Coin': 6,
    'Seven': 7
}

# Functions
def check_winnings(col, lines, bet, values):
    winning_pool = 0
    winning_lines = []
    for line in range(lines):
        symbol = col[0][line]
        for column in col:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winning_pool += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winning_pool, winning_lines


def get_slot_spin(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columnlist = []
    for _ in range(columns):
    # will loop 3 times
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            # will loop depending on how many rows the user wants to bet
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columnlist.append(column)

    return columnlist

def print_slots(columnlist):
    for row in range(len(columnlist[0])):
        for i,column in enumerate(columnlist):
            if i != len(columnlist) - 1:
                print(column[row], end='|' )
            else:
                print(column[row], end='' )

        print()
        #the usage of print and | in the above lines is for the sake of a clean display of the slot machine results

def deposit():
    while True:
        amount= input('Enter the amount you want to deposit: $')
        if amount.isdigit():
            amount = int(amount)
            if amount == 0:
                print('You must deposit at least $1')
            else:
             break
        else:
            print('Input must be a number and cannot be negative value')
    return amount
def get_number_of_slots():
    while True:
        lines = input("Enter the number of slots you want to play ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_SLOTS:
                break
            else:
                print(' The number of slots must be between 1 and ' + str(MAX_SLOTS))
        else:
            print('Input must be a number.')
    return lines
def get_bet():
    while True:
        amount = input('Enter the amount you want to bet on each line: $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print('The bet amount must be between ${MIN_BET} and ${MAX_BET}')
        else:
            print('Input must be a number.')
    return amount

def game_session(balance):
    lines = get_number_of_slots()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print('You do not have enough balance to play. Your current balance is ${balance}')
        else:
            break
        
    print(f'Bet: {balance}, lines: {lines}')
    slots = get_slot_spin(ROWS, COLUMNS, symbol_count)
    print_slots(slots)
    winning, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f'You won on lines {winning_lines}')
    
    print(f'congratulations! You won ${winning}')
    
    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Your Balance is: ${balance}')
        spin = input('Press Enter to spin or Q to quit: ').lower()
        if spin == 'q':
            break
        balance += game_session(balance)
    print(f'Game Over! Your balance left is ${balance}')

main()
