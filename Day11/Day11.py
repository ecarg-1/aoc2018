import numpy as np
from typing import Tuple
serial_num = 2568
def calc_pwr(x:int, y:int) -> int: return (((x + 1 + 10) * (y +1) + serial_num) * (x + 1 + 10))//100%10 - 5 #usees formaula to calcualte power based on x and y coord, accounts for the coord being 1 less than actual due to indexing at 0
def largest_square_pwr(square:int) -> Tuple[int, int, int]: #takes in a square size and finds the top left coordinate of the largest power and the max power
    max_pwr = -10000000000000
    for x in range(300-square): #goes through each x and y as long as making a square would not be out of range of the 300x300 grid
        for y in range(300-square):
            total_pwr = int(np.sum(pwr_grid[x:x+square,y:y+square])) #sums the section of the grid to get the total pwr
            if total_pwr > max_pwr: max_pwr, coord = total_pwr, (x,y) #finds the max total pwr and also records the coord
    return (coord[0]+1, coord[1]+1, max_pwr) #returns the coords and the max pwr

pwr_grid = np.fromfunction(calc_pwr, (300,300)) #calc pwr for each coord and puts it in that spot 

print(largest_square_pwr(3)) #pt1

#observed that it starts getting more negative after square size of 25 so I only check up to 24
max_pwr = -1000000000
for square in range(1,25): #pt2
    x, y, square_max = largest_square_pwr(square) #gets the max pwr for each square size and the coord
    if square_max > max_pwr: max_pwr, coord, square_size = square_max, (x,y), square #finds which is the max of the maxes
print(coord[0],coord[1], square_size)
