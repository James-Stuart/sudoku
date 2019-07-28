# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:08:39 2019

@author: Jamie
"""

#board style, numpy 3x3 matrix with values from 0-9, where 0 is a "blank space".

import copy
import numpy as np
import timeit

row1 = ['3', '2', '8',    '.', '7', '.',    '.', '1', '5']
row2 = ['.', '7', '6',    '.', '.', '.',    '8', '9', '3']
row3 = ['4', '.', '.',    '1', '.', '.',    '.', '6', '.']

row4 = ['5', '.', '.',    '3', '.', '.',    '.', '7', '.']
row5 = ['.', '.', '.',    '8', '1', '.',    '6', '3', '.']
row6 = ['6', '.', '.',    '.', '4', '.',    '9', '.', '.']

row7 = ['.', '6', '2',    '5', '9', '7',    '.', '.', '.']
row8 = ['9', '.', '.',    '.', '3', '.',    '7', '.', '.']
row9 = ['7', '4', '3',    '.', '2', '1',    '.', '8', '.']

sudokuboard = [row1,
               row2,
               row3,
               row4,
               row5,
               row6,
               row7,
               row8,
               row9
               ]


def convertBoardNumpy(board):
    boardConverted = np.zeros([9,9],dtype=int)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                boardConverted[i,j] = int(board[i][j])
                
                
    return boardConverted
boardEg = convertBoardNumpy(sudokuboard)
#print(boardEg)
#print(sudokucheck(boardEg))

def checkRow(row):
    ''' Given a 9x1 vector, counts how many times an value appears in the vector
        if any non-zero values appear more than once, returns false: if not: True
    '''
    rowUniques,counts = np.unique(row,return_counts=True)

    #Ignore 0's, since there can be multiple of these
    if rowUniques[0] == 0:
        counts = counts[1:]

    #If any of the remaining unique counts are > 1 then board is invalid, so if
    #where returns anything, the board is invalid
    return np.where(counts > 1)[0].size == 0




def sudokucheck(board):
    ''' For a give 9x9 sudoku board, uses checkRow to check the board for row,column
        and grid conflicts, returns False if there is any conflict, True if there 
        are none.
    '''
    for i in range(9):
        #Will return False if there are any non-zero duplicates
        if not checkRow(board[i]):
            return False


    #repeat for the columns
    col  = board.T
    for i in range(9):
        #Will return False if there are any non-zero duplicates
        if not checkRow(col[i]):
            return False


    #Repeat for the 3x3 grids
    grid = np.empty(board.shape)
    count = 0
    for i in [0,3,6]:
        for j in [0,3,6]:
            grid[count] = board[i:i+3,j:j+3].reshape(9)
            count+=1

    for i in range(9):
        if not checkRow(grid[i]):
            return False
    return True




def sudoku_complete(board):

    #If any entry in the board is 0, the board is not complete
    if np.where(board == 0)[0].size != 0:
        return False
    #Given we have the right values and the right amount of values, use sudokucheck
    #to make sure the board is a valid sudokuboard.
    return sudokucheck(board)




def sudoku_array_allowed(board):
    '''
    Given a sudoku board, this function will generate and return a 9x9 board
    where each entry is all of the possible values that the index on the sudoku
    board can be, if the entry for the sudoku board is already filled then the
    corresponding entry on the output will be an empty list.
    '''


    initial_entries = np.empty([9],dtype=object)
    initial_missing = np.empty([9],dtype=object)
    loop = 0

    for row in board:
        entries = np.unique(row)
        entries = np.delete(entries,0) #remove 0 from the initial entries
        initial_entries[loop] = entries
        initial_missing[loop] = np.setdiff1d(np.arange(1,10),entries)
        loop +=1




    #List of the indices of the board where the value is 0.
    indices = np.argwhere(board == 0)

    #Look at the empty spots in the sudoku
    array_allowed_entries=np.empty(board.shape,dtype=object)
    array_allowed_entries.fill([]) #This makes every element "[]"
    for index in indices:
        x = index[0]; y=index[1]
        local_allowed_entries = []

        #Try each missing number from that row and check if the board is valid
        for value in initial_missing[x]:
            board[x,y] = value


            start = timeit.default_timer()
            if sudokucheck(board):
                local_allowed_entries.append(value)
            stop = timeit.default_timer()
            print('Time: %.7f' % (stop - start))


            board[x,y] = 0

        array_allowed_entries[x,y] = local_allowed_entries


    return array_allowed_entries




def sudoku_oneoption(board):
    '''
    Given a sudoku board (and using sudoku_array_allowed) this function will search
    the sudoku board for any empty entires that only have 1 possible entry, and
    then fill that entry. It will then repeat this until there are no entries with
    only 1 possible entry.
    
    Once finished return the filled or partially filled sudoku board.
    '''
    one_option = True

    #while one_option:
    for i in range(1):
        array_allowed_entries = sudoku_array_allowed(board)
        #Length of each element in array_allowed_entries (1 dimensional)
        len_allowed_entries = [len(j) for i in array_allowed_entries for j in i]
        #Convert this back into a 9x9 array (2 dimensional)
        len_allowed_entries = np.asarray(len_allowed_entries).reshape(9,9)
    
        #list of the indices where the number of allowed entries is 1
        indices_are_1 = np.argwhere(len_allowed_entries==1)

        if indices_are_1.shape[0] == 0:
            #If there are no indices, then we are done
            one_option = False
            break

        #Go through the indices and place the values into the sudoku board
        for index in indices_are_1:
            x = index[0]; y=index[1]
            board[x,y] = array_allowed_entries[x,y][0]

        if sudoku_complete(board):
            one_option = False
            break

    return board




def sudoku_min_option(board):
    '''
    '''
    #Array of allowed entries

    allow = sudoku_array_allowed(board)


    len_allowed_entries = [len(j) for i in allow for j in i]
    len_allowed_entries = [10 if i == 0 else i for i in len_allowed_entries]
    len_allowed_entries = np.asarray(len_allowed_entries).reshape([9,9])
    #Unfortuneately I have to ignore the len = 0 entries, gonna put a hack answer in



    index = np.unravel_index(len_allowed_entries.argmin(),len_allowed_entries.shape)

    return len_allowed_entries.min(),index,allow






def sudoku_tree_solver(board):

    tree = [board]
    solved = False

    while not solved:
        for brd in tree:

            brd = sudoku_oneoption(brd)

            if sudoku_complete(brd):
                solved = True
                return brd

            tree.remove(brd)


            n,index,allow=sudoku_min_option(brd)


            next_entry = allow[index]

            for value in next_entry:
                new_board = copy.deepcopy(brd)
                new_board[index] = value
                tree.append(new_board)



































































