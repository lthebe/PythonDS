from my2darray import Array2D
import random
class ReversiGameLogic:
    PLAYER_A = 1
    PLAYER_B = 2
    PLAYER_NONE = 0

    NUM_ROWS = 8
    NUM_COLS = 8

    GAME_OVER = 0
    GAME_IN = 1
    def __init__(self):
        """Creates a new instance of the Reversi game logic
        with the initial configuration."""
        self._grid = Array2D(self.NUM_ROWS, self.NUM_COLS)
        self._currentPlayer = self.PLAYER_A
        self._gameState = self.GAME_IN #game in in the beginning
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                self._grid[r,c] = self.PLAYER_NONE
        self._grid[4,3] = self.PLAYER_B
        self._grid[3,4] = self.PLAYER_B
        self._grid[3,3] = self.PLAYER_A
        self._grid[4,4] = self.PLAYER_A
        self._currentTruthList = list() #empty list to collect Truth Value to swipe color(player)value
        self._probing_range = list()
        self._openSquares = 60#after 4 covered position during initialization

    def whoseTurn(self):
        """Returns the player number (1 or 2) for the current player
        or 0 if no player can move"""
        if self._gameState == self.GAME_OVER:
            return self.PLAYER_NONE
        else:
            return self._currentPlayer

    def numChips(self,player):
        """Returns the number of chips on the board belonging
        to the indicated player. The value of player must be 1 or 2."""
        count = 0
        assert (player == self.PLAYER_A or player == self.PLAYER_B),\
            "Player should be %d or %d" %(self.PLAYER_A, self.PLAYER_B)
        for r in range(self.NUM_ROWS):
            for c in range(self.NUM_COLS):
                if self._grid[r,c] == player:
                    count += 1
        return count

    def numOpenSquares(self):
        """Returns the number of squares still open and avail-
        able for play."""
        return self._openSquares

    def getWinner(self):
        """Returns the player number (1 or 2) for the player who has
        won the game or 0 if the game is not finished."""
        if self._gameState == self.GAME_IN:
            return 0
        else:
            winner = self.PLAYER_A if self.numChips(self.PLAYER_A) > \
                self.numChips(self.PLAYER_B) else self.PLAYER_B
            return winner

    def _validateMove(self, row_list, column_list):
        count_current = 0
        count_opponent = 0
        if len(row_list) == 0 or len(column_list) == 0:
            self._currentTruthList.append(False)
            #print "False as row len or col len 0"
            return
        try:
            for r,c in zip(row_list, column_list):
                #print r, c, self._grid[r,c]
                if self._grid[r,c] == 0:#the next cell could not be empty
                    self._currentTruthList.append(False)
                    #print ("False as next cell contains 0")
                    return
                if self._grid[r,c] == self._currentPlayer:
                    count_current += 1
                else:
                    count_opponent += 1
                if count_current == 1:
                    if count_opponent == 0:
                        self._currentTruthList.append(False)
                        #print ("False as the next cell is occupied by same player")
                        return
                    else:
                        self._currentTruthList.append(True)
                        #print ("Last player is same player to form attack line, true")
                        return
            #loop completes, count current is still 0
            #print ("Loop completes, but no current player to complete attack")
            self._currentTruthList.append(False)
            return
        except AssertionError:#assertionerror to keep search within 0<=r,c<=7
            if count_opponent > 0 and current_count == 1:
                self._currentTruthList.append(True)
                return
            else:
                self._currentTruthList.append(False)
                return

    def isLegalMove(self,row, col):
        """Returns True or False to indicate if the cur-
        rent player can place their chip in the square at position (row, col).
        """
        if row == 8 and col == 8: # pass is 8,8
            self._currentPlayer = self.PLAYER_B if self._currentPlayer == \
                self.PLAYER_A else self.PLAYER_A
            return False
        if self.occupiedBy(row,col) is not 0:
            return False
        #first - search by moving from the cell towards the vertical lower side
        #second - search by moving from the cell towards the vertical upper side
        #third - search  by moving from the cell towards horizontal right side
        #fourth - search by moving from the cell towards horizontal left side
        #fifth - search by moving from the cell towards lower left corner
        #sixth - search by moving from the cell towards upper right corner
        #seventh - search by moving from the cell towards upper left corener
        #eighth - search by moving from the cell towards lower right corner
        self._probing_range = [(range(row+1,self.NUM_ROWS), [col]*len(range(row+1,self.NUM_ROWS))),\
                               (range(0,row)[::-1], [col]*len(range(0,row))),\
                               ([row]*len(range(col+1,self.NUM_COLS)),(range(col+1, self.NUM_COLS))),\
                               ([row]*len(range(0,col)), range(0,col)[::-1]),\
                               (range(row+1, self.NUM_ROWS), range(0,col)[::-1]),\
                               (range(0, row)[::-1], range(col+1, self.NUM_ROWS)),\
                               (range(0, row)[::-1], range(0, col)[::-1]),\
                               (range(row+1, self.NUM_ROWS), range(col+1, self.NUM_ROWS))]
        self._currentTruthList = list()
        for (row_list, col_list) in self._probing_range:
            self._validateMove(row_list, col_list)
        #print self._currentTruthList, "<- truth list in isLegalMove method"
        if True in self._currentTruthList:#at least a vailid move in one direction
            return True
        else:
            return False

    def occupiedBy(self,row, col):
        """Which player has a chip in the given square?
        Returns the player number (1 or 2) or 0 if the square is empty."""
        return self._grid[row, col] #0 is filled to denote empty, 1 to denote
        #player A, and 2 to denote player B

    def makeMove(self,row,col):
        """The current player places one of his chips in the
        square at position (row, col). All chips on the board that should be
        flipped based on the rules of Reversi are flipped."""

        if self.isLegalMove(row,col):
            self._grid[row,col] = self._currentPlayer
            probing_now = 0
            print self._currentTruthList, "<-truth list in makemove method"
            for truthValue in self._currentTruthList:
                if truthValue:
                    a, b = self._probing_range[probing_now]
                    for r,c in zip(a,b):
                        if self._grid[r,c] is not self._currentPlayer:
                            self._grid[r,c] = self._currentPlayer
                        else:
                            break
                probing_now += 1

            self._currentPlayer = self.PLAYER_A \
                if self._currentPlayer == self.PLAYER_B else self.PLAYER_B

            self._openSquares -= 1
        if self._openSquares == 0:
            self._gameState = self.GAME_OVER
            print ("Game is over and winner is: %d" %self.getWinner())
