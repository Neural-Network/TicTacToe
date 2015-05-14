# -*- coding: utf-8 -*-
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
import random


ds = SupervisedDataSet(9, 9)

#get training set: combo + result 
targetFile = open('data2.txt','r')
for line in targetFile.readlines():
   data = [int(x) for x in line.strip()if x!='']
   move = (data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17])
   ds.addSample((data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]), (move))
   print ds
TrainDS, TestDS = ds.splitWithProportion(0.8)
net = buildNetwork( TrainDS.indim, 5, TrainDS.outdim, outclass=SoftmaxLayer )
trainer = BackpropTrainer(net, ds,verbose = True)
trainer.trainEpochs(100)
#trainer.trainUntilConvergence()
#, momentum = 0.1, verbose = True, weightdecay = 0.01
#===============GAME===================
def OandX(i):
   if grid[i] == 1:
       return "X"
   if grid[i] == 0:
       return " "
   if grid[i] == 2:
       return "O"

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
     (bo[8] == le and bo[4] == le and bo[0] == le)) 
                   
def printBoard():
   print OandX(0),"|",OandX(1),"|",OandX(2)
   print " ------- "
   print OandX(3),"|",OandX(4),"|",OandX(5)
   print " -------"
   print OandX(6),"|",OandX(7),"|",OandX(8)
   print "=================================="
   
       
def chooseRandomMoveFromList(grid, movesList):
     # Returns a valid move from the passed list on the passed board.
     # Returns None if there is no valid move.
     possibleMoves = []
     for i in range (0,9):
         if grid[i]==0:
             possibleMoves.append(i)

     if len(possibleMoves) != 0:
         return random.choice(possibleMoves)
     else:
         return None
         
grid = [0]*9
board = [0] * 9
def TestGame():
   turn =0;
   while turn<6: 
       userMove = input("User's turn: ")
       grid[userMove] = 1
       printBoard()
       if (((grid[0] == grid[1] == grid[2]) and grid[0] != 0)or (grid[0] == grid[3] == grid[6] and grid[0] != 0) or (grid[0] == grid[4] == grid[8] and grid[0] !=0) or (grid[1] == grid[4] == grid[7] and grid [1] != 0)or (grid[2] == grid[5] == grid[8] and grid[2] != 0) or (grid[3] == grid[4] == grid[5] and grid[3] !=0) or (grid[6] == grid[7] == grid[8] and grid[6] != 0) or (grid[2] == grid[4] == grid[6] and grid[2] != 0)):

           print("User Wins!")
           break
       for i in range (0,9):
            board[i] = grid[i]
       compMove = net.activate((board))
       final = max(compMove[0], compMove[1], compMove[2], compMove[3], compMove[4], compMove[5], compMove[6], compMove[7], compMove[8])
       for j in range(0,9):
           if final == compMove[j]:
               realMove = j
       if grid[realMove] == 0:
           grid[realMove] = 2
           print realMove
       else:
           free = chooseRandomMoveFromList(grid, [0,1,2,3,4,5,6,7,8])
           grid[free] = 2
       
       print ("")
       print ("")
       print ("")
       print ("")
       print ("")
       print ("")
       print ("Computer's Move:")
       printBoard()
       if(((grid[0] == grid[1] == grid[2]) and grid[0] != 0)or (grid[0] == grid[3] == grid[6] and grid[0] != 0) or (grid[0] == grid[4] == grid[8] and grid[0] !=0) or (grid[1] == grid[4] == grid[7] and grid [1] != 0)or (grid[2] == grid[5] == grid[8] and grid[2] != 0) or (grid[3] == grid[4] == grid[5] and grid[3] !=0) or (grid[6] == grid[7] == grid[8] and grid[6] != 0) or (grid[2] == grid[4] == grid[6] and grid[2] != 0)):

           print("Computer Wins! Game Over")
           break

       turn+=1

TestGame()     
