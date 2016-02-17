# Sudoku Solver
by Rodion Kryuchkov

## About

The purpose of this program is to find a solution of a Sudoku game field provided by the user.

The program is implemented in Python 3.5.0. The program does not have a UI and utilizes console output for human-computer interaction.

## Program input
 
The input for the program is provided through a text file containing the game field to be solved. The text file should provide description of the game field using following rules:

* there should be 9 lines in the given text file
* each line represents a line of given Sudoku field
* each line should contain 17 characters: 9 cell values separated with spaces
* cell value should be given as a number in range 1-9 or as an unknown value
* unknown value should be represented with dash (-) symbol

Example input:

```
5 3 - - 7 - - - -
6 - - 1 9 5 - - -
- 9 8 - - - - 6 -
8 - - - 6 - - - 3
4 - - 8 - 3 - - 1
7 - - - 2 - - - 6
- 6 - - - - 2 8 -
- - - 4 1 9 - - 5
- - - - 8 - - 7 9
```

## Starting the program

There are two ways to start the program with desired input.

One way is to start the program through the command line providing **only one argument** that contains path to the desired input file. For example,
```sudoku.py "C:/input.txt"```.

If program fails to open the path provided, or if it fails to read the text file and create a Sudoku field out of it, it will use default input from the file default.txt that is located in the program folder.

An alternative way to start the program with desired input is to modify the contents of the default.txt and to run the program with no arguments provided.

Please note that **Python 3.5.0** has to be used to run this program. Older versions of Python are not supported.

## Program output

If program finds a solution of the given field, the solution is sent as a console output in the same format as the program input.

Example solution:

```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

If program fails to find a solution, it is supposed to display a message "Failed to find a solution".

## Algorithm

When Sudoku field is generated, it is represented as a list of 81 integers. Each integer represents a value of a Sudoku field cell. Empty cell value is 0.

Integer index in the list equals to the corresponding Sudoku field cell index. For the purpose of this program Sudoku field cells are indexed as follows:

```
00 01 02   03 04 05   06 07 08
09 10 11   12 13 14   15 16 17
18 19 20   21 22 23   24 25 26

27 28 29   30 31 32   33 34 35
36 37 38   39 40 41   42 43 44
45 46 47   48 49 50   51 52 53

54 55 56   57 58 59   60 61 62
63 64 65   66 67 68   69 70 71
72 73 74   75 76 77   78 79 80
```

Each index location is defined with help of rows, column and squares. There are nine rows, nine columns and nine squares. Each of them has a number from 0 to 8. For example, field cell with index 64 location is: row 7, column 1, square 6.

There are three helper functions ```getRowNum```, ```getColNum```, ```getSqareNum``` that are used to determine the location of a given index.

There are three helper functions ```getRowUsed```, ```getColUsed```, ```getSqareUsed``` that are used to determine what values are already present in a given row, column or square.

The function ```getMoves``` utilizes all the helper functions to determine what values can be assigned to the given Sudoku field cell according to the Sudoku game rules.

The function ```solve``` takes a Sudoku field and starts to iterate through empty cells of this field, checking for possible values to put into each cell and creating a new solution branch for every such opportunity. If there are no values available, the branch is considered failed and it does not return anything. If there are no more empty cells available, the branch is considered successful and it returns the present cell combination as the solution of the given field.

Function ```solve``` essentially creates a search tree and iterates through this search tree to find a solution. It uses **constraint satisfaction** method with help of ```getMoves``` function as it determines what values can be assigned to the empty cell and creates new branches only for such possible values. It helps to optimize the algorithm performance.


