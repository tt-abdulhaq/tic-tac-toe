import random 




board_list = [
        ['|',  ' ', '|', ' ', '|', ' ', '|'],
        ['|',  ' ', '|', ' ', '|', ' ', '|'],
        ['|',  ' ', '|', ' ', '|', ' ', '|']
    ]


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

#TODO: write a function to check the end of game and specifie the wener.
for _ in range(3):
    print_board()
    row, column, value = get_user_input()
    while board_list[row][column] in ['X', 'O']:
        row, column, value = get_user_input()
    board_list = get_board_list(board_list=board_list, row=row, column=column, value=value)
    row, column, value = get_computer_input(board_list)
    board_list = get_board_list(board_list=board_list, row=row, column=column, value=value)
print_board()
print("Finished the game")
    

    

