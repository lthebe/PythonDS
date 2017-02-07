from __future__ import print_function
from life import LifeGrid

INIT_CONFIG = [(1,2), (2,1), (2,2), (2,3)]

GRID_WIDTH = 5
GRID_HEIGHT = 5

NUM_GENS = 8
def main():
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)
    #play the game
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

def evolve(grid):
    #livecells of the next generation
    liveCells = list()
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbors = grid.numLiveNeighbors(i,j)

            if (neighbors == 2 and grid.isLiveCell(i,j)) or \
                    (neighbors == 3 and grid.isLiveCell(i,j)) or\
                    (not grid.isLiveCell(i,j) and neighbors == 3):
                liveCells.append((i,j)) #appends the tuple
    grid.configure(liveCells)#configures the grid using liveCells coord list

def draw(grid):
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            if grid.isLiveCell(i,j):
                print('x', sep = ' ', end= ' ')
            else:
                print('o', sep= ' ', end= ' ')
        print ('\n')
    print("----next gen-----")

main()
