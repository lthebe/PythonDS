from __future__ import print_function
from reversigamelogic import ReversiGameLogic

def main():
    game = ReversiGameLogic()
    draw(game)
    print("First move: ", game.whoseTurn())
    while(game.getWinner() == 0):
        canInput = True
        while canInput:
            #plays until someone wins
            move_coordinate = raw_input("Input (row,col) for %d or 'pass'   >"\
                                        %game.whoseTurn())
            #IF no legal move at all for a player, the optiion should be pass
            #but it is not implemented as ReversiGameLogic ADT needs some change
            r_string,c_string = move_coordinate.split(',')
            r, c = int(r_string), int(c_string)
            if game.isLegalMove(r,c):
                canInput = False
                game.makeMove(r,c)
        draw(game)


def draw(game):
    for r in range(8):
        for c in range(8):
            print(game.occupiedBy(r,c), sep = '   ', end = '   ')
        print('\n---------------------------------')

main()
