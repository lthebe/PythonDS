from __future__ import print_function
import ast
from ProjectSparseLifeGrid import SparseLifeGrid

def main():
    grid = SparseLifeGrid()
    string_config = raw_input("Give tuples of r and c like: (1,2),(2,1),(2,2),(2,3)  -> ")
    INIT_CONFIG = ast.literal_eval(string_config)
    #INIT_CONFIG = [(1,2), (2,1), (2,2), (2,3)]
    grid.configure(INIT_CONFIG)   #play the game
    draw(grid)
    play = True
    while play:
        evolve(grid)
        user_desire = raw_input("Do you still go ahead? Yes for going othewise ends!  -> ")
        if(user_desire.lower() == 'yes'):
            play = True
        else:
            play = False
        draw(grid)

def evolve(grid):
    gridList = list()
    row_min, col_min = grid.minRange()
    row_max, col_max = grid.maxRange()
    for r in range(row_min - 1, row_max + 2):#row_max is increemented by 2 due to range function
        for c in range(col_min -  1, col_max + 2):
            neighbors = grid.numLiveNeighbors(r,c)
            if (r == row_min - 1) or (c == col_min -1) \
                    or (r == row_max + 1) or (c == col_max +1):
                if neighbors == 3:
                    #grid.setCell(r,c)
                    gridList.append((r,c))
                # neighbors 3 and outside the grid
            #inside the grid
            else:
                if (neighbors == 2 and grid.isLiveCell(r,c)) or \
                    (neighbors == 3 and grid.isLiveCell(r,c)):
                    #grid.setCell(r,c) #set the cell
                    gridList.append((r,c))
                if (neighbors == 3 and not grid.isLiveCell(r,c)):
                    gridList.append((r,c))
                #else:
                    #grid.clearCell(r,c)
                    #Grid clearCell and setCell is not used here because of loop
                    #I have to think how to make it yet
    grid.configure(gridList)

def draw(grid):
    row_min, col_min = grid.minRange()
    row_max, col_max = grid.maxRange()
    for r in range(row_min, row_max+1):
        for c in range(col_min, col_max+1):
            if grid.isLiveCell(r,c):
                print('x', sep = ' ', end= ' ')
            else:
                print('o', sep= ' ', end= ' ')
        print ('\n')
    print("----next gen-----")
main()
