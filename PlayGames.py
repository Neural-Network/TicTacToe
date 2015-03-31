from random import randint


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
    while count in range(0, 9) and end == 0:
        notOccupied = 1
        if firstplayer > 0:
            while notOccupied > 0:
                x=randint(0, 8)
                   
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
                x = randint(0, 8)

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
    grid.append(win)

    f = open('data.txt', 'a')
    f.writelines("%s" % item for item in grid)
    f.writelines("\n")
    f.close()




