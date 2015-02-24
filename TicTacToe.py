from random import randint

grid = [0 for x in range(9)]
firstplayer = 1
count = 0
end = 0
player1win = 1
while count in range(0, 9) and end == 0:
    notOccupied = 1
    if firstplayer > 0:
        while notOccupied > 0:
            x=randint(0, 8)

            if grid[x] == 0:
                grid[x] = 1
                if (((grid[0] == grid[1] == grid[2]) and grid[0] != 0)or (grid[0] == grid[3] == grid[6] and grid[0] != 0) or (grid[0] == grid[4] == grid[8] and grid[0] !=0) or (grid[1] == grid[4] == grid[7] and grid [1] != 0)or (grid[2] == grid[5] == grid[8] and grid[2] != 0) or (grid[3] == grid[4] == grid[5] and grid[3] !=0) or (grid[6] == grid[7] == grid[8] and grid[6] != 0) or (grid[2] == grid[4] == grid[6] and grid[2] != 0)):
                    print("Player 1 Wins!")
                    end = 1
                    player1win = 1
                    break
                notOccupied *= -1

    else:
        while notOccupied > 0:
            x = randint(0, 8)

            if grid[x] == 0:
                grid[x] = 2
                if (((grid[0] == grid[1] == grid[2]) and grid[0] != 0)or (grid[0] == grid[3] == grid[6] and grid[0] != 0) or (grid[0] == grid[4] == grid[8] and grid[0] !=0) or (grid[1] == grid[4] == grid[7] and grid [1] != 0)or (grid[2] == grid[5] == grid[8] and grid[2] != 0) or (grid[3] == grid[4] == grid[5] and grid[3] !=0) or (grid[6] == grid[7] == grid[8] and grid[6] != 0) or (grid[2] == grid[4] == grid[6] and grid[2] != 0)):
                    print("Player 2 Wins!")
                    end = 1
                    player1win = 0
                    break
                notOccupied = notOccupied * -1

    firstplayer = firstplayer * -1
    count = count+1
grid.append(player1win)
f = open('data.txt', 'w')
print(grid, file=f)

f.close()





