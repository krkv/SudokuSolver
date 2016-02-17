# Sudoku Solver
# By Rodion Kryuchkov

import sys

# Next function takes a sudoku file path
# and returns an array of numbers that represent
# a sudoku field.

def makeField(path):
    field = []
    file = open(path, 'r')
    for i in range(9):
        line = file.readline().strip('\n')
        chars = line.split(' ')
        for c in chars:
            if c in ['1','2','3','4','5','6','7','8','9']:
                field.append(int(c))
            else:
                field.append(0)
    file.close()
    return field

# Next functions are used to find
# row number, column number, square number
# for any given sudoku table index.

def getRowNum(index):
    return index//9

def getColNum(index):
    return index%9

def getSquareNum(index):
    return (index%9)//3 + 3*(index//27)

# Takes a field and row/column/square number.
# Returns an array of integers present in given row/column/square.

def getRowUsed(field, number):
    result = []
    for i in range(number*9, number*9+9):
        if field[i] > 0:
            result.append(field[i])
    return result

def getColUsed(field, number):
    result = []
    for i in range(number, 73+number, 9):
        if field[i] > 0:
            result.append(field[i])
    return result

def getSquareUsed(field, number):
    result = []
    for i in [0,1,2,9,10,11,18,19,20]:
        if field[i+3*number+(number//3)*18] > 0:
            result.append(field[i+3*number+(number//3)*18])
    return result

# Takes a filed and an index of empty cell.
# Returns an array of possible integers that
# can be put into the cell.

def getMoves(field, index):
    moves = [1,2,3,4,5,6,7,8,9]
    r = getRowNum(index)
    c = getColNum(index)
    s = getSquareNum(index)
    ru = getRowUsed(field, r)
    cu = getColUsed(field, c)
    su = getSquareUsed(field, s)
    for a in [ru,cu,su]:
        for i in a:
            if i in moves:
                moves.remove(i)
    return moves

# Returns the solution of the given field.

def solve(field):
    if field.count(0) == 0:
        # found the solution
        return field
    else:
        i = field.index(0)
        moves = getMoves(field, i)
        if len(moves) == 0:
            # this branch has failed
            return []
        else:
            # new branch for every possible move
            solution = []
            for m in moves:
                newField = field.copy()
                newField[i] = m
                solution += solve(newField)
            return solution

# Prints given sudoku field.

def printSudoku(field):
    counter = 0
    for i in range(81):
        if field[i] == 0:
            print("-", end=" ")
        else:
            print(field[i], end=" ")
        counter += 1
        if counter%9 == 0:
            print()

# Program starts here.

if(len(sys.argv)==2):
    try:
        f = makeField(sys.argv[1])
    except:
        print("Argument",sys.argv[1],"is not a valid sudoku file path!")
        print("Running the program with default input.")
        f = makeField("default.txt")
else:
    f = makeField("default.txt")
print("\nSudoku:")
printSudoku(f)
s = solve(f)
if(len(s)>0):
    print("\nSolution:")
    printSudoku(s)
else:
    print("\nFailed to find a solution.")
