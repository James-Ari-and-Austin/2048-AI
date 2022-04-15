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
#Edits the grid value
def editVal(normCords, val):
    grid[toListCords(normCords)[0]][toListCords(normCords)[1]] = val

#Creates a class for each tile, stores cords as a tuple and val as an int. 
class tile:
    def __init__(self, x, y, val):
        global id
        self.normCords = (x, y)
        self.val = val
        self.id = id
        id = id + 1
        tiles.update({self.id: self})
    def canMove(self, dxn):
        if dxn == "right":
            if self.normCords[0] + 1 > 4:
                return False
            elif grid[toListCords((self.normCords[0] + 1, self.normCords[1]))[0]][toListCords(self.normCords)[1]] == 0:
                return True
            elif grid[toListCords((self.normCords[0] + 1, self.normCords[1]))[0]][toListCords(self.normCords)[1]] == self.val:
                return "Merge"
        if dxn == "left":
            if self.normCords[0] - 1 < 1:
                return False
            elif grid[toListCords((self.normCords[0] - 1, self.normCords[1]))[0]][toListCords(self.normCords)[1]] == 0:
                return True
            elif grid[toListCords((self.normCords[0] - 1, self.normCords[1]))[0]][toListCords(self.normCords)[1]] == self.val:
                return "Merge"
        if dxn == "up":
            if self.normCords[1] + 1 > 4:
                return False
            elif grid[toListCords(self.normCords)[0]][toListCords((self.normCords[0], self.normCords[1] + 1))[1]] == 0:
                return True
            elif grid[toListCords(self.normCords)[0]][toListCords((self.normCords[0], self.normCords[1] + 1))[1]] == self.val:
                return "Merge"
        if dxn == "down":
            if self.normCords[1] - 1 < 1:
                return False
            elif grid[toListCords(self.normCords)[0]][toListCords((self.normCords[0], self.normCords[1] - 1))[1]] == 0:
                return True
            elif grid[toListCords(self.normCords)[0]][toListCords((self.normCords[0], self.normCords[1] - 1))[1]] == self.val:
                return "Merge"
    def move():
        print()

firstTile = tile(1, 2, 2)
secondTile = tile(1, 3, 2)

#Add tiles to grid
for key in tiles:
    editVal(tiles[key].normCords, tiles[key].val)

print(firstTile.canMove("up"))

#Display the 2D lists
for i in range(len(grid)):
    print(grid[i])
