#Create grid
grid = [0, 0, 0, 0]
for i in range(4):
    grid[i] = [0, 0, 0, 0]
#Create tile variables
tiles = {}
id = 0

#There are two systems of cords, normCords and listCords. normCords start index 1, go (x,y), and have origin in bottom left.
#listCords are different. Do operations on normCords to keep things simple, and then convert the resulting cords with toListCords().

#Each tile is going to be an object. Cords will be properties of that object, as will the value

#When user inputs a dxn, I am going to:
#1: Identify tile that needs to be moved
    #I will need to do this in a different order depending on direction, so that tiles furthest from direction move last
    #Will need to be able to iterate through the grid to identify tiles in multiple different directions
    #When moving horizontally, y cord does not matter to the order. Vice-versa for moving vertically.
#2: Move that tile
    #This will be done one move at a time, checking adjacency after every single move


#Move each tile with a method, and update the grid after each tile is moved so that the next tile to move will have up to date information
#about the locations of other tiles.
#Store each tile object in a dictionary in order to name them. Add a new object to the dictionary whenever a new tile is created.
#Give each tile a tileID. When a tile is merged, create a new tile with a new tileID.

#Switches normalCords to ListCords
def toListCords(normCords):
    row = 4 - normCords[1]
    col = normCords[0] - 1
    listCords = (row, col)
    return listCords
#Returns grid value
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
    cordsList = []
    keysList = []
    objList = []
    sortedDict = {}
    for i in range(len(tiles)):
        print(list(tiles.values()))
        print(type(list(tiles.values())[i]))
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



#Creates a class for each tile, stores cords as a tuple and val as an int.
class tile:
    def __init__(self, x, y, val):
        global id
        self.normCords = (x, y)
        self.val = val
        self.id = id
        self.oldNormCords = (x, y)
        id += 1
        tiles.update({self.id: self})
    #Adds the tile to the grid
    def editGrid(self):
        print("value @editGrid:", self.val)
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
        if dxn == "left":
            if self.normCords[0] - 1 < 1:
                return False
            elif gridVal((self.normCords[0] - 1, self.normCords[1])) == 0:
                return True
            elif gridVal((self.normCords[0] - 1, self.normCords[1])) == self.val:
                return "Merge"
        if dxn == "up":
            if self.normCords[1] + 1 > 4:
                return False
            elif gridVal((self.normCords[0], self.normCords[1] + 1)) == 0:
                return True
            elif gridVal((self.normCords[0], self.normCords[1] + 1)) == self.val:
                return "Merge"
        if dxn == "down":
            if self.normCords[1] - 1 < 1:
                return False
            elif gridVal((self.normCords[0], self.normCords[1] - 1)) == 0:
                return True
            elif gridVal((self.normCords[0], self.normCords[1] - 1)) == self.val:
                return "Merge"
            else: return False
#Given direction, shifts a tile 1 space in that direction
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
                print("old: ", self.oldNormCords)
                print("new: ", self.normCords)
                if self.oldNormCords is not self.normCords:
                    self.editGrid()
                    pass
                break
#Searches for and selects tile overwritten by merge. Deleted after iteration.
    def delTile(self):
        for key in tiles:
            if tiles[key].normCords == self.normCords and tiles[key].val == self.val / 2:
                deadTiles.append(key)

firstTile = tile(1, 3, 2)
secondTile = tile(1, 2, 2)
for key in tiles:
    tiles[key].editGrid()

#Game loop
while True:
    for i in range(len(grid)):
        print(grid[i])
    dxn = input("Direction:")
    deadTiles = []
    tiles = sortList(dxn)
    for key in tiles:
        tiles[key].moveLoop(dxn)
    for tile in deadTiles:
        tiles.pop(deadTiles[tile])
    print("# Remaining Tiles:", len(tiles))
    for key in tiles:
        print("Remaining Tile Cords and value:", tiles[key].normCords, tiles[key].val)
