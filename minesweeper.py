import random
import numpy as np
import sys

class MineSweeper(object):

    def __init__(self, *args, **kwargs):
        self.board = None
        self.unknown = 0
        self.mine = 1
        self.clear = 2
        self.adjacentToClear = 3
        self.adjacentToClearAndMine = 4
        self.flag = 5
        self.flaggedMine = 6   
        self.finished = False  
        self.correctFlags = 0  
        self.numMines = 10
        pass

    def createBoard(self, length, width,numBombs = 10):
        if(numBombs > length * width):
            print("Error!  numBombs exceeds the number of available squares")
            return False
        self.numMines = numBombs
        #Create the board as a 2D array
        self.board = [[self.unknown for x in range(length)] for y in range(width)]
        #Scatter bombs around
        i = 0
        
        while i < numBombs:
            x = random.randint(0,length-1)
            y = random.randint(0,width-1)
            if(self.board[x][y] == self.unknown):
                self.board[x][y] = self.mine
                i+= 1
        pass

    def findNumAdjacentBombs(self, x, y):
        bombs = 0
        adjacentSquares = self.getAdjacentSquares(x,y)
        for tup in adjacentSquares:
               if(self.board[tup[0]][tup[1]] == self.mine or 
                  self.board[tup[0]][tup[1]] == self.flaggedMine or 
                  self.board[tup[0]][tup[1]] == self.adjacentToClearAndMine):
                   bombs += 1               
        return bombs
        
    def getAdjacentSquares(self,x,y):
        adjacentSquares = [(x+1, y), (x-1,y), (x,y+1), (x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y-1),(x-1,y+1)]
        ret = []
        for tup in adjacentSquares:
            test = np.array(tup)
            A = test >= 0 
            B = test < 10
            if (np.all([A,B])):#See if we're out of bounds
                ret.append(tup)
        return ret

    def selectSquare(self,x,y):
        adjacentSquares = self.getAdjacentSquares(x,y)
        if(self.board[x][y] == self.flag or self.board[x][y] == self.flaggedMine):
            print("You have a flag here.  Ignoring.")
        elif(self.board[x][y] == self.mine):
            print("You hit a bomb!  Endgame.")
            self.finished = True
        elif(self.board[x][y] == self.unknown):
            self.board[x][y] = self.clear
            for tup in self.getAdjacentSquares(x,y):
                if(self.board[tup[0]][tup[1]] == self.unknown and self.findNumAdjacentBombs(tup[0],tup[1]) == 0):
                    self.selectSquare(tup[0],tup[1])
                elif(self.board[tup[0]][tup[1]] == self.unknown):
                     self.board[tup[0]][tup[1]] = self.adjacentToClear
                elif(self.board[tup[0]][tup[1]] == self.mine):
                    self.board[tup[0]][tup[1]] = self.adjacentToClearAndMine

    def plantFlag(self,x,y):
        if(self.board[x][y] == self.mine or self.board[x][y] == self.adjacentToClearAndMine):
            self.board[x][y] = self.flaggedMine
            self.correctFlags += 1
            if(self.correctFlags >= self.numMines):
                self.finished = True
                print("All bombs successfully flagged!")
        elif(self.board[x][y] == self.unknown):
            self.board[x][y] = self.flag
        pass

    def displayBoard(self):
        sys.stdout.flush()
        sys.stdout.write("  ")
        for y in range(len(self.board[0])):
            sys.stdout.write(repr(y) + " " )
        print("\n")
        for x in range(len(self.board)):
            sys.stdout.write(repr(x) + " " )
            for y in range(len(self.board[0])):
                item = self.board[x][y]
                if(item == self.unknown or item == self.mine):
                    sys.stdout.write ("#")
                elif(item == self.clear):
                    sys.stdout.write(" ")
                elif(item == self.adjacentToClear or item == self.adjacentToClearAndMine):
                    sys.stdout.write(repr(self.findNumAdjacentBombs(x,y)))
                elif(item == self.flag or item == self.flaggedMine):
                    sys.stdout.write("&")
                sys.stdout.write("|")
            print("\n")
    def getPublicState(self):
        result = self.board
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                item = self.board[x][y]
                if(item == self.adjacentToClear or item == self.adjacentToClearAndMine):
                    result[x][y] = self.findNumAdjacentBombs(x,y)
        result = np.where(self.board == self.mine, self.board, self.unknown)

def main():
    game = MineSweeper()
    game.createBoard(10,10,20)
    while not game.finished:
        game.displayBoard()
        try:
            var = raw_input("Enter move.  S == select square, F == plant flag:\n")
            if(var.lower() == "s"):
                xy = raw_input("Enter x y coordinates:\n")
                coords = xy.split(" ")
                game.selectSquare(int(coords[0]),int(coords[1]))
            elif(var.lower() == "f"):
                xy = raw_input("Enter x y coordinates:\n")
                coords = xy.split(" ")
                game.plantFlag(int(coords[0]),int(coords[1]))
        except:
            print("unrecognized input, try again")



if __name__ == "__main__":
    main()