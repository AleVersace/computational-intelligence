'''
Write a program that checks if a sudoku configuration is valid and if a certain solution is valid.
'''

import numpy as np

# print(sudoku)

def dups(x):
    '''
    Checks if the sum of an array elements is not equal to the sum of its unique elements
    '''
    return np.sum(x) != np.sum(np.unique(x))

def not_valid(sudoku):
    '''
    Checks if rows and columns are valid
    '''
    # This is not a generator because I'm not passing a list
    # So this is going to check them all
    return any(dups(sudoku[r,:]) for r in range(1, sudoku.shape[0])) or \
        any(dups(sudoku[:,c]) for c in range(1, sudoku.shape[1])) or \
        any(dups(sudoku[i:i+3,j:j+3]) for i in range(0, 9, 3) for j in range(0, 9, 3))

def solved(sudoku):
    '''
    Check if this is a valid solution
    '''
    return not not_valid(sudoku) and sudoku.sum() == (1+2+3+4+5+6+7+8+9)*9

# print(solved(sudoku))
