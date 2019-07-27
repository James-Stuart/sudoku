# This script contains functions I have defined to help make my Su Doku solver
# scripts.

# Aim: clock sudoku.

# When Sudoku-mania swept the globe in the mid-2000s, many mathematicians, programmers
# and computer scientists  amateur and professional  started to
# investigate Sudoku itself. They were less interested in solving individual puzzles,
# and more focused on asking and answering mathematical and/or computational questions
# about the entire universe of Sudoku puzzles and solutions.
#                     Gordon Royle, University of Western Australia.



# This is a module used in one of the steps of the tree solver.
import copy

# This function checks if the board is valid.
def sudokucheck(board): # board is a list of lists each with nine entries

    """
        This function checks whether a board is valid. Not necessarily
        complete, but that the rules have not yet been broken.

        Output: Boolean

    """

    # First we have the function check whether the rows are valid.
    for row in board:

        for i in range(len(row)):

                if row[i] != '.':
                    for j in range(len(row)):
                        if i == j:
                            pass
                        elif row[i] == row[j]:
                            #print "Sudoku board not valid"
                            #print "Entries %d and %d in Row %s are equal" % (i+1,j+1,row)
                            #valid = False
                            #print i,j, 'row'
                            return False
                        else:
                            pass

        # Define columns of board

        col1 =[]
        for row in board:
            col1.append(row[0])

        col2 =[]
        for row in board:
            col2.append(row[1])

        col3 =[]
        for row in board:
            col3.append(row[2])

        col4 =[]
        for row in board:
            col4.append(row[3])

        col5 =[]
        for row in board:
            col5.append(row[4])

        col6 =[]
        for row in board:
            col6.append(row[5])

        col7 =[]
        for row in board:
            col7.append(row[6])

        col8 =[]
        for row in board:
            col8.append(row[7])

        col9 =[]
        for row in board:
            col9.append(row[8])

        columns = [col1,
                   col2,
                   col3,
                   col4,
                   col5,
                   col6,
                   col7,
                   col8,
                   col9
                   ]

        # Check columns are valid
        for col in columns:

            for i in range(len(col)):

                    if col[i] != '.':
                        for j in range(0,len(col)):
                            if i == j:
                                pass
                            elif col[i] == col[j]:
                                #print "Sudoku board not valid"
                                #print "Entries %d and %d in Column %s are equal" % (i+1,j+1,col)
                                #print i,j, 'col'
                                return False
                            else:
                                pass



        #Define the 9 squares. Index row-column i.e. sq23 is square in second row
        # and third column of squares.
        # First column of 3x3 squares
        sq11 = [board[0][0],board[0][1],board[0][2],
                board[1][0],board[1][1],board[1][2],
                board[2][0],board[2][1],board[2][2]
               ]

        sq12 = [board[3][0],board[3][1],board[3][2],
                board[4][0],board[4][1],board[4][2],
                board[5][0],board[5][1],board[5][2]
               ]

        sq13 = [board[6][0],board[6][1],board[6][2],
                board[7][0],board[7][1],board[7][2],
                board[8][0],board[8][1],board[8][2]
               ]
        # Second column of 3x3 squares

        sq21 = [board[0][3],board[0][4],board[0][5],
                board[1][3],board[1][4],board[1][5],
                board[2][3],board[2][4],board[2][5]
               ]

        sq22 = [board[3][3],board[3][4],board[3][5],
                board[4][3],board[4][4],board[4][5],
                board[5][3],board[5][4],board[5][5]
               ]

        sq23 = [board[6][3],board[6][4],board[6][5],
                board[7][3],board[7][4],board[7][5],
                board[8][3],board[8][4],board[8][5]
               ]
        # Third column of 3x3 squares

        sq31 = [board[0][6],board[0][7],board[0][8],
                board[1][6],board[1][7],board[1][8],
                board[2][6],board[2][7],board[2][8]
               ]

        sq32 = [board[3][6],board[3][7],board[3][8],
                board[4][6],board[4][7],board[4][8],
                board[5][6],board[5][7],board[5][8]
               ]

        sq33 = [board[6][6],board[6][7],board[6][8],
                board[7][6],board[7][7],board[7][8],
                board[8][6],board[8][7],board[8][8]
               ]

        squares = [sq11,
                   sq12,
                   sq13,
                   sq21,
                   sq22,
                   sq23,
                   sq31,
                   sq32,
                   sq33
                   ]

        for sq in squares:

            for i in range(0,len(sq)):

                    if sq[i] == '.':
                        pass

                    else:
                        for j in range(0,len(sq)):
                            if i == j:
                                pass
                            elif sq[i] == sq[j]:
                                #print "Sudoku board not valid"
                                #print "Square %s has entries that are equal." % sq
                                #print sq
                                return False
                            else:
                                pass

        #print "True"
        return True

# The following function will be determine whether or not the board
# is complete.
def sudoku_complete(board):
    """
        This function returns a Boolean based on whether or not the
        board is finished.

    """

    # Search through rows
    for i in range(0,9):
        for j in range(0,9):

            if board[i][j] == '.':
                return False

    return sudokucheck(board)

# This code prints the board in a terminal-friendly fashion
def print_sudoku(board):

    """
        Print a sudoku board in a manner that looks nice in the terminal

    """
    print(' \n ')
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[0][0],board[0][1],board[0][2],board[0][3],board[0][4],board[0][5],board[0][6],board[0][7],board[0][8]))
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[1][0],board[1][1],board[1][2],board[1][3],board[1][4],board[1][5],board[1][6],board[1][7],board[1][8]))
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[2][0],board[2][1],board[2][2],board[2][3],board[2][4],board[2][5],board[2][6],board[2][7],board[2][8]))
    print('------------------------------------')
    print('------------------------------------')
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[3][0],board[3][1],board[3][2],board[3][3],board[3][4],board[3][5],board[3][6],board[3][7],board[3][8]))
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[4][0],board[4][1],board[4][2],board[4][3],board[4][4],board[4][5],board[4][6],board[4][7],board[4][8]))
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[5][0],board[5][1],board[5][2],board[5][3],board[5][4],board[5][5],board[5][6],board[5][7],board[5][8]))
    print('------------------------------------')
    print('------------------------------------')
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[6][0],board[6][1],board[6][2],board[6][3],board[6][4],board[6][5],board[6][6],board[6][7],board[6][8]))
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[7][0],board[7][1],board[7][2],board[7][3],board[7][4],board[7][5],board[7][6],board[7][7],board[7][8]))
    print(' %s | %s | %s || %s | %s | %s || %s | %s | %s ' % (board[8][0],board[8][1],board[8][2],board[8][3],board[8][4],board[8][5],board[8][6],board[8][7],board[8][8]))

    return ' \n '

# This function will allow us to find the possible entries for each point
# of the sudokuboard.
def sudoku_array_allowed(board):

    """
        Given a sudoku board --- in the form of a list of 9 element lists --- this
        function will return an array indexed by row (i) and column(j) of allowed
        numbers at each entry of the sudoku board.

        To be precise; the output is a list of nine lists --- the list of rows.
        Each element in a row is a list of allowed entries at the point of the
        board.

        Empty spots are to be entered as the string '.'

        If the board already has an entry, then the allowed entries will be
        an empty list at that index.

    """

    # This is a list of elements initially in each row.
    initial_row_entries = []

    for row in board:

        initial = []

        for i in range(len(row)):

            if row[i] != '.':
                initial.append(row[i])

        initial_row_entries.append(initial)



    # This creates a list of elements initially missing in each row.
    initial_row_missing = []

    for list in initial_row_entries:
        missing = []
        for i in range(1,10):
            if not(str(i) in list):
                missing.append(str(i))
        initial_row_missing.append(missing)

    array_allowed_entries = []

    # Index over the rows of the board:
    for i in range(9):

        row_allowed_entries = []

        # Index over the elements of the row.
        for j in range(9):

            # Create list of entries allowed at i,j.
            local_allowed_entries = []

            # If i,j is empty, then try elements missing from row.
            if board[i][j] == '.':

                for x in initial_row_missing[i]:
                    board[i][j] = x
                    if sudokucheck(board):
                        # Append the elements if they are allowed.
                        local_allowed_entries.append(x)
                    board[i][j] = '.'

            row_allowed_entries.append(local_allowed_entries)

        array_allowed_entries.append(row_allowed_entries)

    return array_allowed_entries

# This function finds all entries with one option, fills them in. Checks new
# board for entries with one option, fills them in. Repeats until no such entry
# exists. May, or may not, be enough to solve the board.
def sudoku_oneoption(board):

    """
        This function takes in a sudokuboard. Finds the possible entries
        at each point in the board. Fills in those points with only one
        possibility. Repeats the check and fill until the board is full or
        the solver must fork into branches of choices.

    """

    # This Boolean is true while there are points with precisely one option.
    one_option = True

    # This is the array of allowed entries at each point of the board.
    array_allowed_entries = sudoku_array_allowed(board)

    # This while loop does the checking and filling.
    while one_option == True:

        # Index over rows
        for i in range(0,9):

            # Index over columns
            for j in range(0,9):

                # This if statement fills the points with one possible entry.
                if len(array_allowed_entries[i][j]) == 1:
                    board[i][j] = array_allowed_entries[i][j][0]
                else:
                    pass

        # Is it still true that there is only one option?
        # Recalculate the allowed entries on the new board.
        array_allowed_entries = sudoku_array_allowed(board)

        # After rechecking the board, we look for points with one possible
        # entry.
        length_one = 0
        for i in range(0,9):
            for j in range(0,9):
                if len(array_allowed_entries[i][j]) == 1:
                    length_one = 1
                else:
                    pass

        # If there are none, then we use the Boolean to exit the while loop.
        # Else, we go through the loop again.
        if length_one == 1:
            pass
        else:
            one_option = False

    return None

# Find entry with minimum number of options to make.
def sudoku_min_option(board):

    """
        This function returns the minimum number of options among all
        the squares of the sudoku board.

        For instance if a board has a square with only two options, while all
        other squares have more than two options, then this function
        will return 2.

    """
    #Array of allowed entries
    allow = sudoku_array_allowed(board)

    all_zero = True
    for x in allow:
        if not (len(x) == 0):
            all_zero = False
        else:
            pass

    if all_zero == True:
        return 0

    # Local variable to find the entries with smallest options.
    min_length = 9

    # Row index
    for i in range(0,9):
        # Column index
        for j in range(0,9):

            # Update minimum length and the index of the entry with
            # the minimun length.
            if 0 < len(allow[i][j]) < min_length:
                min_length = len(allow[i][j])

    return min_length

# This is the function which will solve all suoku puzzles. This takes, at most, about 15minutes to solve a puzzle.
def sudoku_tree_solver(board):

    """
        Given a board, this function creates a list containing that board.

        For each board (seed) in the list, this function updates the list by adjoining
        new boards. These are obtained by taking the smallest options and making
        all of them seperately. The seed is removed each time.

        Each step updates the list with boards with valid entries.

    """
    # This is the tree of possible solutions updated throughout the loop.
    tree = [board]
    #max_len = 1

    # Boolean to tell the loop to stop.
    solved = False

    # The completed board.
    solution = []

    while not solved:

        for brd in tree:

                # For each board in the tree. Find entry with smallest number
                # of options. Append each of those options to the tree.
                # Remove the board from the tree.

                if sudoku_complete(brd):
                    solved = True
                    solution = brd

                # Remove brd
                tree.remove(brd)

                # Array of allowed entries
                allow = sudoku_array_allowed(brd)

                # Local variables to find the entries with smallest options.
                min_index_row = 0
                min_index_col = 0
                min_length = 9

                # Now we find the (an) entry with the smallest number of options.
                # Row index
                for i in range(9):
                    # Column index
                    for j in range(9):

                        # Update minimum length and the index of the entry with
                        # the minimun length.
                        #TODO: 
                        if 0 < len(allow[i][j]) < min_length:
                            min_length = len(allow[i][j])
                            min_index_row = i
                            min_index_col = j
                            # Entry with lowest number of options.
                next_entry = allow[min_index_row][min_index_col]

                # Feng Discussion: Feng thinks deep-copy might fix code.
                for x in next_entry:
                    # Append a new board for each option in next_entry.
                    new_board = copy.deepcopy(brd)
                    new_board[min_index_row][min_index_col] = x
                    tree.append(new_board)

    return solution
