def get_numbers_in_grid(grid:int) -> list:
    """
        begin_row and begin_colum is the upper left corner/point in the grid
        for the grid 5 for example the values would be:
            begin_row = 3
            begin_colum = 6
    """
    begin_row = int(grid/3)*3
    begin_colum = (grid % 3)*3

    ret = list()

    #print("Getting grid: ", grid)
    #print("begin_row: ", begin_row)
    #print("begin_colum: ", begin_colum)

    for row in range(3):
        for colum in range(3):
            num = sudoku_board[begin_row + row][begin_colum + colum]
            if num != None:
                ret.append(num)
    return ret







def check_sudoku_board() -> bool:
    """
        
    """
    for i in range(9):  # Check the the horizontal and vertical lines
        grid_nums  = get_numbers_in_grid(i)
        row_nums   = get_numbers_in_row(i)
        colum_nums = get_numbers_in_colum(i)
        grid_nums.sort()
        row_nums.sort()
        colum_nums.sort()
        
        if len(grid_nums) != 9 or len(row_nums) != 9 or len(colum_nums) != 9:
            print("Board is not entirely full!", file=sys.stderr)
            return False

        for a in range(9):
            if grid_nums[i] != i or row_nums[i] != i or colum_nums[i] != i:
                return False
        #print(grid_nums)
        #print(row_nums)
        #print(colum_nums)
        #print()

    for rows in range(0, 6 + 1, 3):   #checking the grids
        for colums in range(0, 6 + 1, 3):
            grid_nums  = get_numbers_in_grid(rows, colums)

            for a in range(9):
                if grid_nums[i] != i:
                    return False
    return True
