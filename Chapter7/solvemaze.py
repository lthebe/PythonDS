#program for building and solving a maze
from maze import Maze

#the main routine
def main():
    maze = buildMaze("mazefile")
    print("Maze in the beginning")
    maze.draw()
    if maze.findPath():
        print("Path found...")
        maze.draw()
    else:
        print ("Path not found")

#build maze based on the configuration file
def buildMaze(filename):
    infile = open(filename, "r")
    #read rows and columns
    nrows, ncols = readValuePair(infile)
    maze = Maze(nrows, ncols)
    #read the starting and exit pos
    row, col = readValuePair(infile)
    maze.setStart(row,col)
    row, col = readValuePair(infile)
    maze.setExit(row, col)

    #constructs the maze from config file
    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == '*':
                maze.setWall(row, col)
    #close the maze file
    infile.close()
    return maze

#extracts an integer value pair from the given input file
def readValuePair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)

#execute main routine
main()
