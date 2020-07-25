class piece():
    def __init__(self, color, char, r, c):
        self.color = color
        self.char = char
        self.row = r
        self.col = c
class pawn(piece):
    def __init__(self, color, char, r, c):
        self.piece = piece(color, char, r, c)
        self.value = 1
        self.moves = 3
        self.movesR = [-1,-2,0,0]
        self.movesC = [0,0,-1,1]
class Pawn(piece):
    def __init__(self, color, char, r, c):
        self.piece = piece(color, char, r, c)
        self.value = 1
        self.moves = 3
        self.movesR = [1,2,0,0]
        self.movesC = [0,0,-1,1]
class Rook(piece):
    def __init__(self, color, char, r, c):
        self.piece = piece(color, char, r, c)
        self.value = 10
        self.moves = 27
        self.movesR = [1,-1,0,0,2,-2,0,0,3,-3,0,0,4,-4,0,0,5,-5,0,0,6,-6,0,0,7,-7,0,0]
        self.movesC = [0,0,1,-1,0,0,2,-2,0,0,3,-3,0,0,4,-4,0,0,5,-5,0,0,6,-6,0,0,7,-7]
class Bishop(piece):
    def __init__(self, color, char, r, c):
        self.piece = piece(color, char, r, c)
        self.value = 6
        self.moves = 27
        self.movesR = [1,-1,1,-1,2,-2,2,-2,3,-3,3,-3,4,-4,4,-4,5,-5,5,-5,6,-6,6,-6,7,-7,7,-7]
        self.movesC = [1,-1,-1,1,2,-2,-2,2,3,-3,-3,3,4,-4,-4,4,5,-5,-5,5,6,-6,-6,6,7,-7,-7,7]

class Knight(piece):
    def __init__(self, color, char, r, c):
        self.piece = piece(color, char, r, c)
        self.value = 5
        self.moves = 7
        self.movesR = [1,2,2,1,-1,-2,-2,-1]
        self.movesC = [2,1,-1,-2,-2,-1,1,2]
class Queen(piece):
    def __init__(self, color, char, r, c):
        self.piece = piece(color, char, r, c)
        self.value = 18
        self.moves = 45
        self.movesR = [1,1,1,0,-1,-1,-1,0,2,2,2,0,-2,-2,-2,0,3,3,3,0,-3,-3,-3,0,4,4,4,0,-4,-4,-4,0,5,5,5,0,-5,-5,-5,0,6,6,6,0,-6,-6,-6,0,7,7,7,0,-7,-7,-7,0]
        self.movesC = [-1,0,1,1,1,0,-1,-1,-2,0,2,2,2,0,-2,-2,-3,0,3,3,3,0,-3,-3,-4,0,4,4,4,0,-4,-4,-5,0,5,5,5,0,-5,-5,-6,0,6,6,6,0,-6,-6,-7,0,7,7,7,0,-7,-7]
class King(piece):
    def __init__(self, color, char, r, c):
        self.value = 1
        self.piece = piece(color, char, r, c)
        self.moves = 3
        self.movesR = [1,-1,0,0]
        self.movesC = [0,0,1,-1]
class Empty(piece):
    def __init__(self, color, char, r, c):
        self.value = 0
        self.piece = piece(color, char, r, c)
        self.moves = 0
        self.movesR = []
        self.movesC = []
