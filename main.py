"""
    About:
    This program finds an unique solution to any unsolved sudoku entered. 
    I have done this in a 2 step process. First, I search for the blank spaces which are straightforward ie, the correct number can be found very easily.
    Lastly, I have used backtracking via recursion to find the rest of the numbers. Backtracking is very fast, and efficient making it ideal for solving sudokus. 

    References:
    1. https://codereview.stackexchange.com/questions/242327/simple-sudoku-solver-in-python
    2. https://youtu.be/JzONv5kaPJM

    Author:
    Rishab Maheshwari
"""
#sample sudoku
sudokuBoard = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
]

#solve(board:list):bool
def solve(board:list) -> bool:
    find = empty_spaces(board)
    
    #this is the base base. If find is empty, the board has been solved
    if not find:
        return True
    else:
        row = find[0]
        col = find[1]

    for i in range(1,10):
        if valid_turn(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

#valid_turn(board:list, number: int, position: int):bool
def valid_turn(board:list, number:int, position:int) -> bool:
    #check row
    for i in range(len(board)):
        if board[position[0]][i] == number:
            return False

    #check column
    for j in range(len(board)):
        if board[j][position[1]] == number:
            return False

    #check square
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number: 
                return False
    
    return True

#print_board(board:list):
def print_board(board:list):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        
        for j in range(len(board)):
            if j%3 == 0 and j != 0:
                print(" | ", end ="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

#empty_spaces(board:list):tuple
def empty_spaces(board:list) -> tuple:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    
    return None

#fill_single_values(board:list)
def fill_single_values(board:list):
    for i in range(len(board)):
        for j in range(len(board)):
            row_numbers = get_row_numbers(board, i)
            col_numbers = get_column_numbers(board, j)
            box_numbers = get_box_numbers(board, i, j)

            if board[i][j] == 0:
                if len(row_numbers) == 1:
                    board[i][j] = row_numbers[0]
                    break
                if len(col_numbers) == 1:
                    board[i][j] = col_numbers[0]
                    break
                if len(box_numbers) == 1:
                    board[i][j] = box_numbers[0]
    
#get_row_numbers(board:list, row:int):list
def get_row_numbers(board:list, row:int) -> list:
    numbers_present = []
    allowed_numbers = [1,2,3,4,5,6,7,8,9]

    for j in range(len(board)):
        if board[row][j] != 0:
            if board[row][j] in allowed_numbers:
                numbers_present.append(board[row][j])

    return list(set(allowed_numbers) - set(numbers_present))

#get_column_numbers(board:list, column:int):list
def get_column_numbers(board:list, column:int) -> list:
    numbers_present = []
    allowed_numbers = [1,2,3,4,5,6,7,8,9]

    for i in range(len(board)):
        if board[i][column] != 0:
            if board[i][column] in allowed_numbers:
                numbers_present.append(board[i][column])

    return list(set(allowed_numbers) - set(numbers_present))

#get_box_numbers(board:list, row:int, column:int):list
def get_box_numbers(board:list, row:int, column:int) -> list:
    numbers_present = []
    allowed_numbers = [1,2,3,4,5,6,7,8,9]
    row = row // 3
    column = column // 3
    for i in range(row * 3, row * 3 + 3):
        for j in range(column * 3, column * 3 + 3):
            if board[i][j] != 0:
                if board[i][j] in allowed_numbers:
                    numbers_present.append(board[i][j])
    
    return list(set(allowed_numbers) - set(numbers_present))

#MAIN
print_board(sudokuBoard)
fill_single_values(sudokuBoard)
solve(sudokuBoard)
print()
print_board(sudokuBoard)