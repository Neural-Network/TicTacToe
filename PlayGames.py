# -*- coding: utf-8 -*-
from random import randint, choice

#-------------------------------------------------------------------------
def isWinner(bo, le):
     # Given a board and a player’s letter, this function returns True if that player has won.
     # We use bo instead of board and le instead of letter so we don’t have to type as much.
     return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
     (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
     (bo[0] == le and bo[1] == le and bo[2] == le) or # across the bottom
     (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
     (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
     (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
     (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
     (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal

def getBoardCopy(board):
     # Make a duplicate of the board list and return it the duplicate.
     dupeBoard = []

     for i in board:
         dupeBoard.append(i)

     return dupeBoard

def isSpaceFree(board, move):
     # Return true if the passed move is free on the passed board.
     return board[move] == 0
     
def chooseRandomMoveFromList(board, movesList):
     # Returns a valid move from the passed list on the passed board.
     # Returns None if there is no valid move.
     possibleMoves = []
     for i in movesList:
         if isSpaceFree(board, i):
             possibleMoves.append(i)

     if len(possibleMoves) != 0:
         return choice(possibleMoves)
     else:
         return None 
         
computerLetter = 1
playerLetter = 2    
     
def getComputerMove(board, computerLetter):
     # Given a board and the computer's letter, determine where to move and return that move.


     # Here is our algorithm for our Tic Tac Toe AI:
     # First, check if we can win in the next move
     for i in range(0, 9):
         copy = getBoardCopy(board)
         if isSpaceFree(copy, i):
             makeMove(copy, computerLetter, i)
             if isWinner(copy, computerLetter):
                 return i

     # Check if the player could win on their next move, and block them.
     for i in range(0, 9):
         copy = getBoardCopy(board)
         if isSpaceFree(copy, i):
             makeMove(copy, playerLetter, i)
             if isWinner(copy, playerLetter):
                 return i

    
     # Try to take the center, if it is free.
     if isSpaceFree(board, 4):
         return 4

     # Try to take one of the corners, if they are free.
     move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
     if move != None:
         return move


     # Move on one of the sides.
     return chooseRandomMoveFromList(board, [1, 3, 5, 7])

def isBoardFull(board):
     # Return True if every space on the board has been taken. Otherwise return False.
     for i in range(0, 9):
         if isSpaceFree(board, i):
             return False
     return True
     
def makeMove(board, letter, move):
     board[move] = letter
#----------------------------------------------------------------------------------

def OandX(i):
    if grid[i] == 1:
        return "X"
    if grid[i] == 0:
        return " "
    if grid[i] == 2:
        return "O"

for game in range(1000):
    grid = [0 for x in range(9)]
    print OandX(0),"|",OandX(1),"|",OandX(2)
    print " ------- "
    print OandX(3),"|",OandX(4),"|",OandX(5)
    print " -------"
    print OandX(6),"|",OandX(7),"|",OandX(8)
    print " "
    print "Player1's turn"
   
    firstplayer = 1
    occupyNum = 0
    count = 0
    end = 0
    win = 0
    grid.append(0)
    while count in range(0, 9) and end == 0:
        notOccupied = 1
        if firstplayer > 0:
            while notOccupied > 0:
                x= randint(0,8)
                grid[9] = x
                
                   
                if grid[x] == 0:
                    grid[x] = 1
                    notOccupied *= -1
                    occupyNum+=1
                    print OandX(0),"|",OandX(1),"|",OandX(2)
                    print "-----------"
                    print OandX(3),"|",OandX(4),"|",OandX(5)
                    print "-----------"
                    print OandX(6),"|",OandX(7),"|",OandX(8)
                
                    if (((grid[0] == grid[1] == grid[2]) and grid[0] != 0)or (grid[0] == grid[3] == grid[6] and grid[0] != 0) or (grid[0] == grid[4] == grid[8] and grid[0] !=0) or (grid[1] == grid[4] == grid[7] and grid [1] != 0)or (grid[2] == grid[5] == grid[8] and grid[2] != 0) or (grid[3] == grid[4] == grid[5] and grid[3] !=0) or (grid[6] == grid[7] == grid[8] and grid[6] != 0) or (grid[2] == grid[4] == grid[6] and grid[2] != 0)):
                        print " "
                        print("Player 1 Wins!")
                        print "=============================="
                        print " "
                        end = 1
                        win = 1
                        break
                    elif occupyNum==9 and win!=1 and win !=2:
                        win = 0
                        print" "
                        print"Draw!"
                        print("==============================")
                        print(" ")
                    else: 
                        print " "
                        print "Player2's turn"
                    
        else:
            while notOccupied > 0:
                x = getComputerMove(grid, 'X')
                grid[9] = x
                f = open('data.txt', 'a')
                f.writelines("%s" % item for item in grid)
                f.writelines("\n")
                f.close()
                if grid[x] == 0:
                    grid[x] = 2
                    notOccupied = notOccupied * -1
                    occupyNum+=1
                    print OandX(0),"|",OandX(1),"|",OandX(2)
                    print "-----------"
                    print OandX(3),"|",OandX(4),"|",OandX(5)
                    print "-----------"
                    print OandX(6),"|",OandX(7),"|",OandX(8)
                    if (((grid[0] == grid[1] == grid[2]) and grid[0] != 0)or (grid[0] == grid[3] == grid[6] and grid[0] != 0) or (grid[0] == grid[4] == grid[8] and grid[0] !=0) or (grid[1] == grid[4] == grid[7] and grid [1] != 0)or (grid[2] == grid[5] == grid[8] and grid[2] != 0) or (grid[3] == grid[4] == grid[5] and grid[3] !=0) or (grid[6] == grid[7] == grid[8] and grid[6] != 0) or (grid[2] == grid[4] == grid[6] and grid[2] != 0)):
                        print " "
                        print("Player 2 Wins!")
                        print("==============================")
                        print(" ")
                        end = 1
                        win = 2
                        break
                    elif occupyNum==9 and win !=1 and win !=2:
                        win = 0
                        print" "
                        print"Draw!"
                        print("==============================")
                        print(" ")
                    else:
                        print " "
                        print "Player1's turn"
        
        firstplayer = firstplayer * -1
        count = count+1
    

    

