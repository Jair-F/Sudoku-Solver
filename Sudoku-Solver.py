import sys

"""
    Our Sudoku Board looks like this!
       0  1  2   3  4  5   6  7  8
    1 [1  2  3 | 4  5  6 | 7  8  9],
    2 [1  2  3 | 4  5  6 | 7  8  9],
    3 [1  2  3 | 4  5  6 | 7  8  9],
      ---------|---------|---------
    4 [1  2  3 | 4  5  6 | 7  8  9],
    5 [1  2  3 | 4  5  6 | 7  8  9],
    6 [1  2  3 | 4  5  6 | 7  8  9],
      ---------|---------|---------
    7 [1  2  3 | 4  5  6 | 7  8  9],
    8 [1  2  3 | 4  5  6 | 7  8  9],
    9 [1  2  3 | 4  5  6 | 7  8  9]

    Grids:
        colums -->    
rows   0  1  2   3  4  5   6  7  8
 |  0 [0       |         |        ],
 |  1 [   0    |    1    |    2   ],
    2 [        |         |        ],
      ---------|---------|----------
    3 [        |         |        ],
    4 [   3    |    4    |    5   ],
    5 [        |         |        ],
      ---------|---------|----------
    6 [        |         |        ],
    7 [   6    |    7    |    8   ],
    8 [        |         |        ]
"""

sudoku_board = [
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]

def get_numbers_in_row(sudoku_board:list[list], row:int) -> list:
    """
        return the numbers in the row
    """
    ret = list()
    for colum in sudoku_board[row]:
        if colum != None:
            ret.append(colum)
    return ret

def get_numbers_in_colum(sudoku_board:list[list], colum:int) -> list:
    """
        returns the number in the specified colum
    """
    ret = list()
    for row in sudoku_board:
        grid = row[colum]
        if grid != None:
            ret.append(grid)
    return ret

def get_numbers_in_grid(sudoku_board:list[list], begin_row:int, begin_colum:int) -> list:
    """
        specify one point in the sudoku_board and the function will return all the numbers in this grid
    """    
    while begin_row % 3 != 0:  # if the row is divideable by 3 we are at the first number of this grid
        begin_row -= 1
    
    while begin_colum % 3 != 0:  # if the colum is divideable by 3 we are at the first number of this grid
        begin_colum -= 1
    
    ret = list()
    for row in range(3):
        for colum in range(3):
            num = sudoku_board[begin_row + row][begin_colum + colum]
            if num != None:
                ret.append(num)
    return ret

def check_sudoku_board(sudoku_board:list[list], ) -> bool:
    """
        returns true if the board is fully solved!
    """
    for i in range(9):  # Check the the horizontal and vertical lines
        row_nums   = get_numbers_in_row(sudoku_board, i)
        colum_nums = get_numbers_in_colum(sudoku_board, i)
        row_nums.sort()
        colum_nums.sort()
        
        if len(row_nums) != 9 or len(colum_nums) != 9:
            print("Board is not entirely full!", file=sys.stderr)
            return False

        for a in range(9):
            if row_nums[i] != i+1 or colum_nums[i] != i+1:
                return False

    for rows in range(0, 6 + 1, 3):   #checking the grids
        for colums in range(0, 6 + 1, 3):
            grid_nums  = get_numbers_in_grid(sudoku_board, rows, colums)
            grid_nums.sort()

            for a in range(9):
                if grid_nums[i] != i+1:
                    return False
    return True

def check_duplicate_numbers(sudoku_board:list[list]) -> bool:
    """
        checks only if there is a duplicate numbers in one row-colum or grid! (if there are fore example 2 fives somewhere(in a row/colum/grid) - not solved correctly)
        Not if the board is full!!
        returns true if he doesnt found a duplicate number
    """
    row_nums   = list
    colum_nums = list
    grid_nums  = list
    for i in range(9):  # get the horizontal and vertical lines
        row_nums   = get_numbers_in_row(sudoku_board, i)
        colum_nums = get_numbers_in_colum(sudoku_board, i)

        row_nums.sort()
        colum_nums.sort()

        for a in range(1, len(row_nums)):
            if row_nums[a - 1] == row_nums[a]:
                return True
        for a in range(1, len(colum_nums)):
            if colum_nums[a - 1] == colum_nums[a]:
                return True
    
    for rows in range(0, 6 + 1, 3):   # get the grids
        for colums in range(0, 6 + 1, 3):
            grid_nums  = get_numbers_in_grid(sudoku_board, rows, colums)

            grid_nums.sort()
            for i in range(1, len(grid_nums)):
                if grid_nums[i - 1] == grid_nums[i]:
                    return True
    
    return False

def check_fully_filled(sudoku_board:list[list]) -> bool:
    """
        checks if every field in the sudoku_board is filled up - if the board is entirely filled
    """
    for row in sudoku_board:
        for colum in row:
            if colum == None:
                return False
    return True

def solve_sudoku(sudoku_board:list[list]) -> bool:
    """
        Returns true if there is a solution for this board - if it could solve it.
        Otherwise false
    """

    if check_duplicate_numbers(sudoku_board) == True:
        return False
    if check_fully_filled(sudoku_board) == True:
        return check_sudoku_board(sudoku_board) # if the board is right, it will return true else false


    options_to_fill_in = list() # options of numbers we can fill in(for the coordinate with the lowest most less options)
    all_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # all the options which can be in one row/colum/grid

    """
        we change in this function call only one number(the number with the most less options of numbers
        to fill in). The position(row and colum) of this number is stored in this two variables:
            change_number_position_row    - the row
            change_number_position_colum  - the colum
    """
    change_number_position_row   = 0
    change_number_position_colum = 0

    lowest_num_of_options = 10    # lowest num of options on the whole board - this number we will change afterwards/set it


    for row in range(len(sudoku_board)):    # parsing for numbers, we can fill in
        for colum in range(len(sudoku_board[row])):
            if sudoku_board[row][colum] != None:    # if at this position there is already a number - continue - we dont can put in there a number
                continue

            used_numbers = get_numbers_in_colum(sudoku_board, colum) + get_numbers_in_row(sudoku_board, row) + get_numbers_in_grid(sudoku_board, row, colum)
            used_numbers = list(set(used_numbers)) # remove duplicates - we added the numbers from row,colum and grid - there are maybe duplicates
            
            num_of_options = len(all_options) - len(used_numbers)
            if num_of_options < lowest_num_of_options:
                change_number_position_colum = colum
                change_number_position_row   = row

                for item in all_options:
                    if item not in used_numbers:     # add the numbers, which are not in used_numbers, but in all_options
                        options_to_fill_in.append(item)

                lowest_num_of_options = num_of_options

    
    for option in options_to_fill_in:
        sudoku_board[change_number_position_row][change_number_position_colum] = option
        if solve_sudoku(sudoku_board) == True:
            return True
    

    # we dont found a solution on this position - restore the actual position by setting it to None(because the board-function-paramter is given as reference)
    sudoku_board[change_number_position_row][change_number_position_colum] = None
    return False


def print_board(sudoku_board:list[list]):
    print("-------------------------")
    for row in range(len(sudoku_board)):
        print(f"|{sudoku_board[row][0]}  {sudoku_board[row][1]}  {sudoku_board[row][2]}|{sudoku_board[row][3]}  {sudoku_board[row][4]}  {sudoku_board[row][5]}|{sudoku_board[row][6]}  {sudoku_board[row][7]}  {sudoku_board[row][8]}|".replace("None", ' '))
        if (row+1) % 3 == 0:
            print("-------------------------")


if __name__ == "__main__":
    input_board = input("File with sudoku_board: ")
    with open(input_board, "r") as file:
        row = 0
        for line in file:
            line = line.strip()
            line = line.replace(' ', '')
            nums = line.split(',')
            for i in range(len(nums)):
                sudoku_board[row][i] = int(nums[i]) if nums[i] != '' else None
            row += 1
    
    print_board(sudoku_board)
    print()

    if solve_sudoku(sudoku_board) == True:
        print("solved board!!")
    else:
        print("doesnt solved board!!")
    
    print_board(sudoku_board)
