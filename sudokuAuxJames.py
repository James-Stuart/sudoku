# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:08:39 2019

@author: Jamie
"""

#board style, numpy 3x3 matrix with values from 0-9, where 0 is a "blank space".

import copy
import numpy as np

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
    board = np.zeros([9,9])
    
    for i in range(9):
        for j in range(9):
            if sudokuboard[i][j] != '.':
                board[i,j] = int(sudokuboard[i][j])
                
                
    return board
boardEg = convertBoardNumpy(sudokuboard)
            
print(sudokucheck(boardEg))

def sudokucheck(board):
    removedZeros = np.zeros(9,dtype=object)
    i=0
    for row in board:
        removedZeros[i]=row[row!=0]
        i+=1
    
    return(removedZeros)











