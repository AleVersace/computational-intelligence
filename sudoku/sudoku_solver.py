''' 
Author: @AleVersace (Alessandro Versace)

Computational Intelligence Lab1 @ Polytechnic University of Turin (PoliTo)

- Write a program that solves a sudoku in an efficient way 

Approach: I decided to use a Depth-First Search starting solving the problem
selecting the "most interesting" empty cell (0s) to change at each step.
The "Most Interesting" is referred to the cell that has the lowest number 
of available values that are good (not against the rules) at a certain step. (As we humans usually proceed with the game)

So at each step the algorithm calculates the available values for each empty cell and selects
the cell with the lowest number of values. Then it expands the frontier using DF and proceeding
with the next step.

'''


from collections import deque
import numpy as np
from sudoku_validitycheck import solved

# This is your sudoku. 0s are empty cells.
sudoku1 = np.array([[5, 3, 0,      0, 7, 0,       0, 0, 0],
                    [6, 0, 0,      1, 9, 5,       0, 0, 0],
                    [0, 9, 8,      0, 0, 0,       0, 6, 0],
                    [8, 0, 0,      0, 6, 0,       0, 0, 3],
                    [4, 0, 0,      8, 0, 3,       0, 0, 1],
                    [7, 0, 0,      0, 2, 0,       0, 0, 6],
                    [0, 6, 0,      0, 0, 0,       2, 8, 0],
                    [0, 0, 0,      4, 1, 9,       0, 0, 5],
                    [0, 0, 0,      0, 8, 0,       0, 7, 9]], dtype=np.int8)

frontier = deque()
frontier.append(sudoku1)

n = 0
while frontier:
    n += 1
    sudoku1 = frontier.popleft()
    
    ## DEBUG
    #print(sudoku1)
    #print(len(frontier))
    ## END

    if solved(sudoku1):
        print(f"Whoa! Look how good I am, you can't beat me!\nSolved in {n} steps:\n {sudoku1}\n")
        break

    b_i = -1;
    b_j = -1;
    best_available_values = None

    # Check for next interesting position to go on with
    for i, j in np.ndindex(sudoku1.shape):
        if sudoku1[i, j] == 0:
            # Computes available values that follows game rules for the empty cells
            available_values = np.linspace(1, 9, 9, dtype=np.int8)
            already_used = np.unique(np.concatenate((sudoku1[i, :], sudoku1[:, j], sudoku1[ (i//3*3) : (i//3*3+3) , (j//3*3) : (j//3*3+3)].flatten())))
            available_values = set(available_values.flatten())
            already_used = set(already_used.flatten())
            available_values = np.array(list(available_values.difference(already_used)), dtype=np.int8)
            
            # Save position and values if is the lowest number of available values seen for this configuration
            if best_available_values is None or (available_values.shape[0] < best_available_values.shape[0]):
                best_available_values = available_values
                b_i = i
                b_j = j

    if best_available_values is None:
        continue

    # Expand Frontier
    for v in best_available_values:

        ## DEBUG
        #print(f"{best_available_values} in {b_i},{b_j}\n")
        #print(f"[v] = {v}")
        ## END

        sudoku1[b_i, b_j] = v
        new_config = np.copy(sudoku1)
        frontier.appendleft(new_config)