from itertools import product

# function to solve a sudoku puzzle using backtracking
def solve_sudoku(puzzle):
    if (len(puzzle) < 9):
        return []
    for line in puzzle:
        if len(line) < 9:
            return []

    for (row, col) in product(range(0,9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1, 10):
                allowed = True
                for i in range(0,9):
                    if num in (puzzle[i][col], puzzle[row][i]):
                        allowed = False
                        break
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + 1][col - col % 3 + j] == num:
                        allowed = False
                        break
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    puzzle[row][col] = 0
            return False

    return puzzle

if __name__ == '__main__':
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
    solve_sudoku(puzzle)
    for line in puzzle:
        print(line)

    """ [[5,3,4,6,7,8,9,1,2]
         [6,7,2,1,9,5,3,4,8]
         [1,9,8,3,4,2,5,6,7]
         [8,5,9,7,6,1,4,2,3]
         [4,2,6,8,5,3,7,9,1]
         [7,1,3,9,2,4,8,5,6]
         [9,6,1,5,3,7,2,8,4]
         [2,8,7,4,1,9,6,3,5]
         [3,4,5,2,8,6,1,7,9]] """