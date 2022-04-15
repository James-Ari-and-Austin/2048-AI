#There are two systems of cords, normCords and listCords. normCords start index 1, go (x,y), and have origin in bottom left.
#listCords are different. Do operations on normCords to keep things simple, and then convert the resulting cords with toListCords().

#Each tile is going to be an object. Cords will be properties of that object, as will the value

#When user inputs a dxn:
#1: Sort the list of tile objects into the order they need to be moved based on cords relative to dxn
#2: Iterate through the list of tile objects using methods to move each tiles
#3: The tile moves one square at a time, checking adjacency after each movement, and keeps moving until it merges or is unable to move more.
#4: The updated position of the tile is added to the grid so that other objects can accurately reference that tile's position
#5: The spot where the tile used to be is set to an empty space
#6: The process repeats with the next tile object in the list until the list is completely iterated through.

#Tiles are created unnamed, but stored in a dictionary with a self.id value as their key. To reference an object, use the dictionary.

#Dependencies
from random import randrange

#Converts normalCords to listCords
def toListCords(normCords):
    row = 4 - normCords[1]
    col = normCords[0] - 1
    listCords = (row, col)
    return listCords

#Returns grid value at given cords
def gridVal(normCords):
    return grid[toListCords(normCords)[0]][toListCords(normCords)[1]]

#Returns value of a tile based on cords
def getValue(normCords):
    for key in tiles:
        if tiles[key].normCords == normCords:
            return tiles[key]

#Returns key of a tile based on cords
def getKey(normCords):
    for key in tiles:
        if tiles[key].normCords == normCords:
            return key

#Returns object of a tile based on cords
def getObj(normCords):
    for key in tiles:
        if tiles[key].normCords == normCords:
            return tiles[key]

#Sorts list based on directions
def sortList(dxn):
    #Uses the cords of a tile to identify each object, so that the objects can be sorted based on position.
    #Gets the cords of each tile and stores it into a list.
    #The list is sorted in different ways based on the direction, and then the get____() functions are used to get that tile's object,
    #or key, or value, etc in the order that the cords are in in the list, so that they can be read into a new dictionary in order.
    cordsList = []
    keysList = []
    objList = []
    sortedDict = {}
    for i in range(len(tiles)):
        cordsList.append(list(tiles.values())[i].normCords)
    if dxn == "right":
        cordsList = sorted(cordsList, key = lambda x: x[0], reverse = True)
    if dxn == "left":
        cordsList = sorted(cordsList, key = lambda x: x[0])
    if dxn == "up":
        cordsList = sorted(cordsList, key = lambda x: x[1], reverse = True)
    if dxn == "down":
        cordsList = sorted(cordsList, key = lambda x: x[1])
    for i in range(len(cordsList)):
        keysList.append(getKey(cordsList[i]))
        objList.append(getObj(cordsList[i]))
        sortedDict.update({keysList[i]: objList[i]})
    return sortedDict


#Finds an open spot on the grid and returns the cords in normCords form.
def openSpot():
    i = True
    while i == True:
        x = randrange(1, 4)
        y = randrange(1, 4)
        if gridVal((x, y)) == 0:
            return (x, y)

#Translates direction inputs from wsad to up, down, left, right
def getDxn():
    i = True
    while i == True:
        dxn = input("Direction:").lower()
        if dxn == "w":
            dxn = "up"
        if dxn == "s":
            dxn = "down"
        if dxn == "d":
            dxn = "right"
        if dxn == "a":
            dxn = "left"
        if dxn != "up" and dxn != "down" and dxn != "left" and dxn != "right":
            pass
        else: i = False
    return dxn

#Creates a class for each tile, stores cords as a tuple and val as an int.
class tile:

    #Creates relevant variables, adds new object to tiles dict, and updates global id variable.
    def __init__(self):
        global id
        self.normCords = openSpot()
        self.oldNormCords = self.normCords
        self.val = randrange(2, 4, 2)
        self.id = id
        id += 1
        tiles.update({self.id: self})

    #Adds the tile to the grid
    def editGrid(self):
        grid[toListCords(self.oldNormCords)[0]][toListCords(self.oldNormCords)[1]] = 0
        grid[toListCords(self.normCords)[0]][toListCords(self.normCords)[1]] = self.val

    #Checks to see if a tile can move in a given direction
    def canMove(self, dxn):
        if dxn == "right":
            if self.normCords[0] + 1 > 4:
                return False
            elif gridVal((self.normCords[0] + 1, self.normCords[1])) == 0:
                return True
            elif gridVal((self.normCords[0] + 1, self.normCords[1])) == self.val:
                return "Merge"
            else:
                return False
        elif dxn == "left":
            if self.normCords[0] - 1 < 1:
                return False
            elif gridVal((self.normCords[0] - 1, self.normCords[1])) == 0:
                return True
            elif gridVal((self.normCords[0] - 1, self.normCords[1])) == self.val:
                return "Merge"
            else:
                return False
        elif dxn == "up":
            if self.normCords[1] + 1 > 4:
                return False
            elif gridVal((self.normCords[0], self.normCords[1] + 1)) == 0:
                return True
            elif gridVal((self.normCords[0], self.normCords[1] + 1)) == self.val:
                return "Merge"
            else:
                return False
        elif dxn == "down":
            if self.normCords[1] - 1 < 1:
                return False
            elif gridVal((self.normCords[0], self.normCords[1] - 1)) == 0:
                return True
            elif gridVal((self.normCords[0], self.normCords[1] - 1)) == self.val:
                return "Merge"
            else:
                return False

#Given direction, shifts a tile 1 space in that direction
#Breaks cord tuple into a list so it can be modified, and then changes it back to a tuple.
    def moveCords(self, dxn):
        self.cordsArr = list(self.normCords)
        if dxn == "right":
            self.cordsArr[0] += 1
        elif dxn == "left":
            self.cordsArr[0] -= 1
        elif dxn == "up":
            self.cordsArr[1] += 1
        elif dxn == "down":
            self.cordsArr[1] -= 1
        self.normCords = tuple(self.cordsArr)

#Moves a tile in given direction as many times as is possible
    def moveLoop(self, dxn):
        self.oldNormCords = self.normCords
        while True:
            if self.canMove(dxn) == True:
                self.moveCords(dxn)
            elif self.canMove(dxn) == "Merge":
                self.val *= 2
                self.moveCords(dxn)
                self.delTile()
                self.editGrid()
                break
            elif self.canMove(dxn) == False:
                if self.oldNormCords is not self.normCords:
                    self.editGrid()
                break

#Searches for and selects tile overwritten by merge. Tile not deleted in this function because the dict is currently being iterated on.
    def delTile(self):
        for key in tiles:
            if tiles[key].normCords == self.normCords and tiles[key].val == self.val / 2:
                deadTiles.append(key)

def main():
    #Game loop
    while True:
        for i in range(len(grid)):
            print(grid[i])
        dxn = getDxn()
        deadTiles = []
        tiles = sortList(dxn)
        global tile

        for key in tiles:
            tiles[key].moveLoop(dxn)
            #KNOWN BUG: Merges frequently don't occur when there are a lot of blocks concentrated. 
        if len(deadTiles) > 0:
            for tile in deadTiles:
                tiles.pop(deadTiles[tile])
        tile().editGrid()

if __name__ == "__main__":
    #First Time Setup
    grid = [0, 0, 0, 0]
    for i in range(4):
        grid[i] = [0, 0, 0, 0]
    tiles = {}
    deadTiles = []
    id = 0
    #Create first tiles
    tile().editGrid()
    tile().editGrid()

    main()
