#Tic Tac Toe by Zammy
print("Welcome to Tic Tac Toe!")
def printboard(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
'''list works best for X,O inputs'''
printboard(board)

#Printing board Done