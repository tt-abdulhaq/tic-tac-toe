import random 
import sys





board_list = [
        ['|',  ' ', '|', ' ', '|', ' ', '|'],
        ['|',  ' ', '|', ' ', '|', ' ', '|'],
        ['|',  ' ', '|', ' ', '|', ' ', '|']
    ]

winner_list = sorted([
    [(0,1), (0,3), (0,5)],
    [(1,1), (1,3), (1,5)],
    [(2,1), (2,3), (2,5)],
    [(0,1), (1,1), (2,1)],
    [(0,3), (1,3), (2,3)],
    [(0,5), (1,5), (2,5)],
    [(0,1), (1,3), (2,5)]
])


user_fill_cell = []
computer_fill_cell = []



def print_board(board_list = board_list):
    for board_cell in board_list:
        for c_board in board_cell:
            print(c_board, end='')
        print()


def get_user_input():
    row = input("please choice a row: ")
    while row not in ['1', '2', '3']:
        print("Please enter a number between 1-3")
        row = input("please choice a row: ")

    column = input("Please choice a column: ")
    while column not in ['1', '2', '3']:
        print("please enter a number between 1-3")
        column = input("Please choice a column: ")
    row = int(row)
    column = int(column)
    row = row-1
    column_index_map = {1:1, 2:3, 3:5}
    column = column_index_map[column]

    return (row, column, 'X')


def get_computer_input(board_list):
    row_indexes  = [0,1,2]
    column_index = [1,3,5]
    row = random.choice(row_indexes)
    column = random.choice(column_index)
    while board_list[row][column] in ['X', 'O']:
        row = random.choice(row_indexes)
        column = random.choice(column_index)
    return (row, column, 'O')



def get_board_list(board_list, row, column, value):
    board_list[row][column] = value
    return board_list

def check_winner(filled_cells, player, winner_list = winner_list):
    if sorted(filled_cells) in winner_list:
        if player == 'user':
            return (1, 'user')
        else:
            return (1, "computer")
    else:
        return (0, None)

for _ in range(3):
    print_board()
    row, column, value = get_user_input()
    while board_list[row][column] in ['X', 'O']:
        row, column, value = get_user_input()
    user_fill_cell.append((row, column))
    board_list = get_board_list(board_list=board_list, row=row, column=column, value=value)
    row, column, value = get_computer_input(board_list)
    computer_fill_cell.append((row, column))
    winner_status, winner = check_winner(computer_fill_cell, 'computer')
    board_list = get_board_list(board_list=board_list, row=row, column=column, value=value)


print_board()
winner_status, winner = check_winner(user_fill_cell, 'user')
if winner_status:
    print(f"Your are win Congertulation. ):")
    sys.exit()
    

winner_status, winner = check_winner(computer_fill_cell, 'computer')
if winner_status:
    print("computer is the winner. sorry! :(")
    sys.exit()

print("Finished the game, no one is winner do want play again!")
sys.exit()
    

    

