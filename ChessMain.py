class Tile:
    def __init__(self, PIECE, COLOR):
        self.piece = PIECE
        self.color = COLOR
        
class Board(Tile): 
    def __init__(self):
        self.tile1a = Tile("R","B")
        self.tile1b = Tile("N","B")
        self.tile1c = Tile("B","B")
        self.tile1d = Tile("Q","B")
        self.tile1e = Tile("K","B")
        self.tile1f = Tile("B","B")
        self.tile1g = Tile("N","B")
        self.tile1h = Tile("R","B")
        self.tile2a = Tile("P","B")
        self.tile2b = Tile("P","B")
        self.tile2c = Tile("P","B")
        self.tile2d = Tile("P","B")
        self.tile2e = Tile("P","B")
        self.tile2f = Tile("P","B")
        self.tile2g = Tile("P","B")
        self.tile2h = Tile("P","B")
        self.tile3a = Tile(" ","")
        self.tile3b = Tile(" ","")
        self.tile3c = Tile(" ","")
        self.tile3d = Tile(" ","")
        self.tile3e = Tile(" ","")
        self.tile3f = Tile(" ","")
        self.tile3g = Tile(" ","")
        self.tile3h = Tile(" ","")
        self.tile4a = Tile(" ","")
        self.tile4b = Tile(" ","")
        self.tile4c = Tile(" ","")
        self.tile4d = Tile(" ","")
        self.tile4e = Tile(" ","")
        self.tile4f = Tile(" ","")
        self.tile4g = Tile(" ","")
        self.tile4h = Tile(" ","")
        self.tile5a = Tile(" ","")
        self.tile5b = Tile(" ","")
        self.tile5c = Tile(" ","")
        self.tile5d = Tile(" ","")
        self.tile5e = Tile(" ","")
        self.tile5f = Tile(" ","")
        self.tile5g = Tile(" ","")
        self.tile5h = Tile(" ","")
        self.tile6a = Tile(" ","")
        self.tile6b = Tile(" ","")
        self.tile6c = Tile(" ","")
        self.tile6d = Tile(" ","")
        self.tile6e = Tile(" ","")
        self.tile6f = Tile(" ","")
        self.tile6g = Tile(" ","")
        self.tile6h = Tile(" ","")
        self.tile7a = Tile("p","W")
        self.tile7b = Tile("p","W")
        self.tile7c = Tile("p","W")
        self.tile7d = Tile("p","W")
        self.tile7e = Tile("p","W")
        self.tile7f = Tile("p","W")
        self.tile7g = Tile("p","W")
        self.tile7h = Tile("p","W")
        self.tile8a = Tile("r","W")
        self.tile8b = Tile("n","W")
        self.tile8c = Tile("b","W")
        self.tile8d = Tile("k","W")
        self.tile8e = Tile("q","W")
        self.tile8f = Tile("B","W")
        self.tile8g = Tile("n","W")
        self.tile8h = Tile("r","W")        
        
        
class ChessMain(Board):
    def __init__(self,Player1,Player2):
        game_won = False
        """create starting board"""
        self.chessBoard = Board()
        """input players"""
        self.pl1_name = Player1
        self.pl1_sym = "W"
        self.pl2 = Player2
        self.pl2_sym = "B"
    def check(self, row, col):
        if col == "a":
            if row == 1:
                return self.chessBoard.tile1a.color
            elif row == 2:
                return self.chessBoard.tile2a.color
            elif row == 3:
                return self.chessBoard.tile3a.color
            elif row == 4:
                return self.chessBoard.tile4a.color
            elif row == 5:
                return self.chessBoard.tile5a.color
            elif row == 6:
                return self.chessBoard.tile6a.color
            elif row == 7:
                return self.chessBoard.tile7a.color
            elif row == 8:
                return self.chessBoard.tile8a.color
        elif col == "b":
            if row == 1:
                return self.chessBoard.tile1b.color
            elif row == 2:
                return self.chessBoard.tile2b.color
            elif row == 3:
                return self.chessBoard.tile3b.color
            elif row == 4:
                return self.chessBoard.tile4b.color
            elif row == 5:
                return self.chessBoard.tile5b.color
            elif row == 6:
                return self.chessBoard.tile6b.color
            elif row == 7:
                return self.chessBoard.tile7b.color
            elif row == 8:
                return self.chessBoard.tile8b.color
        elif col == "c":
            if row == 1:
                return self.chessBoard.tile1c.color
            elif row == 2:
                return self.chessBoard.tile2c.color
            elif row == 3:
                return self.chessBoard.tile3c.color
            elif row == 4:
                return self.chessBoard.tile4c.color
            elif row == 5:
                return self.chessBoard.tile5c.color
            elif row == 6:
                return self.chessBoard.tile6c.color
            elif row == 7:
                return self.chessBoard.tile7c.color
            elif row == 8:
                return self.chessBoard.tile8c.color
        elif col == "d":
            if row == 1:
                return self.chessBoard.tile1d.color
            elif row == 2:
                return self.chessBoard.tile2d.color
            elif row == 3:
                return self.chessBoard.tile3d.color
            elif row == 4:
                return self.chessBoard.tile4d.color
            elif row == 5:
                return self.chessBoard.tile5d.color
            elif row == 6:
                return self.chessBoard.tile6d.color
            elif row == 7:
                return self.chessBoard.tile7d.color
            elif row == 8:
                return self.chessBoard.tile8d.color
        elif col == "e":
            if row == 1:
                return self.chessBoard.tile1e.color
            elif row == 2:
                return self.chessBoard.tile2e.color
            elif row == 3:
                return self.chessBoard.tile3e.color
            elif row == 4:
                return self.chessBoard.tile4e.color
            elif row == 5:
                return self.chessBoard.tile5e.color
            elif row == 6:
                return self.chessBoard.tile6e.color
            elif row == 7:
                return self.chessBoard.tile7e.color
            elif row == 8:
                return self.chessBoard.tile8e.color
        elif col == "f":
            if row == 1:
                return self.chessBoard.tile1f.color
            elif row == 2:
                return self.chessBoard.tile2f.color
            elif row == 3:
                return self.chessBoard.tile3f.color
            elif row == 4:
                return self.chessBoard.tile4f.color
            elif row == 5:
                return self.chessBoard.tile5f.color
            elif row == 6:
                return self.chessBoard.tile6f.color
            elif row == 7:
                return self.chessBoard.tile7f.color
            elif row == 8:
                return self.chessBoard.tile8f.color
        elif col == "g":
            if row == 1:
                return self.chessBoard.tile1g.color
            elif row == 2:
                return self.chessBoard.tile2g.color
            elif row == 3:
                return self.chessBoard.tile3g.color
            elif row == 4:
                return self.chessBoard.tile4g.color
            elif row == 5:
                return self.chessBoard.tile5g.color
            elif row == 6:
                return self.chessBoard.tile6g.color
            elif row == 7:
                return self.chessBoard.tile7g.color
            elif row == 8:
                return self.chessBoard.tile8g.color
        elif col == "h":
            if row == 1:
                return self.chessBoard.tile1h.color
            elif row == 2:
                return self.chessBoard.tile2h.color
            elif row == 3:
                return self.chessBoard.tile3h.color
            elif row == 4:
                return self.chessBoard.tile4h.color
            elif row == 5:
                return self.chessBoard.tile5h.color
            elif row == 6:
                return self.chessBoard.tile6h.color
            elif row == 7:
                return self.chessBoard.tile7h.color
            elif row == 8:
                return self.chessBoard.tile8h.color
    def get_piece(self, row, col):
        if col == "a":
            if row == 1:
                temp = self.chessBoard.tile1a.piece
                self.chessBoard.tile1a.piece = " "
                self.chessBoard.tile1a.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2a.piece
                self.chessBoard.tile2a.piece = " "
                self.chessBoard.tile2a.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3a.piece
                self.chessBoard.tile3a.piece = " "
                self.chessBoard.tile3a.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4a.piece
                self.chessBoard.tile4a.piece = " "
                self.chessBoard.tile4a.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5a.piece
                self.chessBoard.tile5a.piece = " "
                self.chessBoard.tile5a.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6a.piece
                self.chessBoard.tile6a.piece = " "
                self.chessBoard.tile6a.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7a.piece
                self.chessBoard.tile7a.piece = " "
                self.chessBoard.tile7a.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8a.piece
                self.chessBoard.tile8a.piece = " "
                self.chessBoard.tile8a.color = ""
                return temp
        elif col == "b":
            if row == 1:
                temp = self.chessBoard.tile1b.piece
                self.chessBoard.tile1b.piece = " "
                self.chessBoard.tile1b.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2b.piece
                self.chessBoard.tile2b.piece = " "
                self.chessBoard.tile2b.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3b.piece
                self.chessBoard.tile3b.piece = " "
                self.chessBoard.tile3b.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4b.piece
                self.chessBoard.tile4b.piece = " "
                self.chessBoard.tile4b.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5b.piece
                self.chessBoard.tile5b.piece = " "
                self.chessBoard.tile5b.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6b.piece
                self.chessBoard.tile6b.piece = " "
                self.chessBoard.tile6b.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7b.piece
                self.chessBoard.tile7b.piece = " "
                self.chessBoard.tile7b.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8b.piece
                self.chessBoard.tile8b.piece = " "
                self.chessBoard.tile8b.color = ""
                return temp
        elif col == "c":
            if row == 1:
                temp = self.chessBoard.tile1c.piece
                self.chessBoard.tile1c.piece = " "
                self.chessBoard.tile1c.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2c.piece
                self.chessBoard.tile2c.piece = " "
                self.chessBoard.tile2c.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3c.piece
                self.chessBoard.tile3c.piece = " "
                self.chessBoard.tile3c.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tilec.piece
                self.chessBoard.tile4c.piece = " "
                self.chessBoard.tile4c.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5c.piece
                self.chessBoard.tile5c.piece = " "
                self.chessBoard.tile5c.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6c.piece
                self.chessBoard.tile6c.piece = " "
                self.chessBoard.tile6c.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7c.piece
                self.chessBoard.tile7c.piece = " "
                self.chessBoard.tile7c.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8c.piece
                self.chessBoard.tile8c.piece = " "
                self.chessBoard.tile8c.color = ""
                return temp
        elif col == "d":
            if row == 1:
                temp = self.chessBoard.tile1d.piece
                self.chessBoard.tile1d.piece = " "
                self.chessBoard.tile1d.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2d.piece
                self.chessBoard.tile2d.piece = " "
                self.chessBoard.tile2d.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3d.piece
                self.chessBoard.tile3d.piece = " "
                self.chessBoard.tile3d.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4d.piece
                self.chessBoard.tile4d.piece = " "
                self.chessBoard.tile4d.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5d.piece
                self.chessBoard.tile5d.piece = " "
                self.chessBoard.tile5d.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6d.piece
                self.chessBoard.tile6d.piece = " "
                self.chessBoard.tile6d.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7d.piece
                self.chessBoard.tile7d.piece = " "
                self.chessBoard.tile7d.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8d.piece
                self.chessBoard.tile8d.piece = " "
                self.chessBoard.tile8d.color = ""
                return temp
        elif col == "e":
            if row == 1:
                temp = self.chessBoard.tile1e.piece
                self.chessBoard.tile1e.piece = " "
                self.chessBoard.tile1e.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2e.piece
                self.chessBoard.tile2e.piece = " "
                self.chessBoard.tile2e.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3e.piece
                self.chessBoard.tile3e.piece = " "
                self.chessBoard.tile3e.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4e.piece
                self.chessBoard.tile4e.piece = " "
                self.chessBoard.tile4e.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5e.piece
                self.chessBoard.tile5e.piece = " "
                self.chessBoard.tile5e.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6e.piece
                self.chessBoard.tile6e.piece = " "
                self.chessBoard.tile6e.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7e.piece
                self.chessBoard.tile7e.piece = " "
                self.chessBoard.tile7e.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8e.piece
                self.chessBoard.tile8e.piece = " "
                self.chessBoard.tile8e.color = ""
                return temp
        elif col == "f":
            if row == 1:
                temp = self.chessBoard.tile1f.piece
                self.chessBoard.tile1f.piece = " "
                self.chessBoard.tile1f.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2f.piece
                self.chessBoard.tile2f.piece = " "
                self.chessBoard.tile2f.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3f.piece
                self.chessBoard.tile3f.piece = " "
                self.chessBoard.tile3f.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4f.piece
                self.chessBoard.tile4f.piece = " "
                self.chessBoard.tile4f.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5f.piece
                self.chessBoard.tile5f.piece = " "
                self.chessBoard.tile5f.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6f.piece
                self.chessBoard.tile6f.piece = " "
                self.chessBoard.tile6f.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7f.piece
                self.chessBoard.tile7f.piece = " "
                self.chessBoard.tile7f.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8f.piece
                self.chessBoard.tile8f.piece = " "
                self.chessBoard.tile8f.color = ""
                return temp
        elif col == "g":
            if row == 1:
                temp = self.chessBoard.tile1g.piece
                self.chessBoard.tile1g.piece = " "
                self.chessBoard.tile1g.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2g.piece
                self.chessBoard.tile2g.piece = " "
                self.chessBoard.tile2g.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3g.piece
                self.chessBoard.tile3g.piece = " "
                self.chessBoard.tile3g.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4g.piece
                self.chessBoard.tile4g.piece = " "
                self.chessBoard.tile4g.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5g.piece
                self.chessBoard.tile5g.piece = " "
                self.chessBoard.tile5g.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6g.piece
                self.chessBoard.tile6g.piece = " "
                self.chessBoard.tile6g.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7g.piece
                self.chessBoard.tile7g.piece = " "
                self.chessBoard.tile7g.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8g.piece
                self.chessBoard.tile8g.piece = " "
                self.chessBoard.tile8g.color = ""
                return temp
        elif col == "h":
            if row == 1:
                temp = self.chessBoard.tile1h.piece
                self.chessBoard.tile1h.piece = " "
                self.chessBoard.tile1h.color = ""
                return temp
            elif row == 2:
                temp = self.chessBoard.tile2h.piece
                self.chessBoard.tile2h.piece = " "
                self.chessBoard.tile2h.color = ""
                return temp
            elif row == 3:
                temp = self.chessBoard.tile3h.piece
                self.chessBoard.tile3h.piece = " "
                self.chessBoard.tile3h.color = ""
                return temp
            elif row == 4:
                temp = self.chessBoard.tile4h.piece
                self.chessBoard.tile4h.piece = " "
                self.chessBoard.tile4h.color = ""
                return temp
            elif row == 5:
                temp = self.chessBoard.tile5h.piece
                self.chessBoard.tile5h.piece = " "
                self.chessBoard.tile5h.color = ""
                return temp
            elif row == 6:
                temp = self.chessBoard.tile6h.piece
                self.chessBoard.tile6h.piece = " "
                self.chessBoard.tile6h.color = ""
                return temp
            elif row == 7:
                temp = self.chessBoard.tile7h.piece
                self.chessBoard.tile7h.piece = " "
                self.chessBoard.tile7h.color = ""
                return temp
            elif row == 8:
                temp = self.chessBoard.tile8h.piece
                self.chessBoard.tile8h.piece = " "
                self.chessBoard.tile8h.color = ""
                return temp
    def make_move(self, row, col, sym, piece):
        if col == "a":
            if row == 1:
                self.chessBoard.tile1a.color = sym
                self.chessBoard.tile1a.piece = piece
            elif row == 2:
                self.chessBoard.tile2a.color = sym
                self.chessBoard.tile2a.piece = piece
            elif row == 3:
                self.chessBoard.tile3a.color = sym
                self.chessBoard.tile3a.piece = piece
            elif row == 4:
                self.chessBoard.tile4a.color = sym
                self.chessBoard.tile4a.piece = piece
            elif row == 5:
                self.chessBoard.tile5a.color = sym
                self.chessBoard.tile5a.piece = piece
            elif row == 6:
                self.chessBoard.tile6a.color = sym
                self.chessBoard.tile6a.piece = piece
            elif row == 7:
                self.chessBoard.tile7a.color = sym
                self.chessBoard.tile7a.piece = piece
            elif row == 8:
                self.chessBoard.tile8a.color = sym
                self.chessBoard.tile8a.piece = piece
        elif col == "b":
            if row == 1:
                self.chessBoard.tile1b.color = sym
                self.chessBoard.tile1b.piece = piece
            elif row == 2:
                self.chessBoard.tile2b.color = sym
                self.chessBoard.tile2b.piece = piece
            elif row == 3:
                self.chessBoard.tile3b.color = sym
                self.chessBoard.tile3b.piece = piece
            elif row == 4:
                self.chessBoard.tile4b.color = sym
                self.chessBoard.tile4b.piece = piece
            elif row == 5:
                self.chessBoard.tile5b.color = sym
                self.chessBoard.tile5b.piece = piece
            elif row == 6:
                self.chessBoard.tile6b.color = sym
                self.chessBoard.tile6b.piece = piece
            elif row == 7:
                self.chessBoard.tile7b.color = sym
                self.chessBoard.tile7b.piece = piece
            elif row == 8:
                self.chessBoard.tile8b.color = sym
                self.chessBoard.tile8b.piece = piece
        elif col == "c":
            if row == 1:
                self.chessBoard.tile1c.color = sym
                self.chessBoard.tile1c.piece = piece
            elif row == 2:
                self.chessBoard.tile2c.color = sym
                self.chessBoard.tile2c.piece = piece
            elif row == 3:
                self.chessBoard.tile3c.color = sym
                self.chessBoard.tile3c.piece = piece
            elif row == 4:
                self.chessBoard.tile4c.color = sym
                self.chessBoard.tile4c.piece = piece
            elif row == 5:
                self.chessBoard.tile5c.color = sym
                self.chessBoard.tile5c.piece = piece
            elif row == 6:
                self.chessBoard.tile6c.color = sym
                self.chessBoard.tile6c.piece = piece
            elif row == 7:
                self.chessBoard.tile7c.color = sym
                self.chessBoard.tile7c.piece = piece
            elif row == 8:
                self.chessBoard.tile8c.color = sym
                self.chessBoard.tile8c.piece = piece
        elif col == "d":
            if row == 1:
                self.chessBoard.tile1d.color = sym
                self.chessBoard.tile1d.piece = piece
            elif row == 2:
                self.chessBoard.tile2d.color = sym
                self.chessBoard.tile2d.piece = piece
            elif row == 3:
                self.chessBoard.tile3d.color = sym
                self.chessBoard.tile3d.piece = piece
            elif row == 4:
                self.chessBoard.tile4d.color = sym
                self.chessBoard.tile4d.piece = piece
            elif row == 5:
                self.chessBoard.tile5d.color = sym
                self.chessBoard.tile5d.piece = piece
            elif row == 6:
                self.chessBoard.tile6d.color = sym
                self.chessBoard.tile6d.piece = piece
            elif row == 7:
                self.chessBoard.tile7d.color = sym
                self.chessBoard.tile7d.piece = piece
            elif row == 8:
                self.chessBoard.tile8d.color = sym
                self.chessBoard.tile8d.piece = piece
        elif col == "e":
            if row == 1:
                self.chessBoard.tile1e.color = sym
                self.chessBoard.tile1e.piece = piece
            elif row == 2:
                self.chessBoard.tile2e.color = sym
                self.chessBoard.tile2e.piece = piece
            elif row == 3:
                self.chessBoard.tile3e.color = sym
                self.chessBoard.tile3e.piece = piece
            elif row == 4:
                self.chessBoard.tile4e.color = sym
                self.chessBoard.tile4e.piece = piece
            elif row == 5:
                self.chessBoard.tile5e.color = sym
                self.chessBoard.tile5e.piece = piece
            elif row == 6:
                self.chessBoard.tile6e.color = sym
                self.chessBoard.tile6e.piece = piece
            elif row == 7:
                self.chessBoard.tile7e.color = sym
                self.chessBoard.tile7e.piece = piece
            elif row == 8:
                self.chessBoard.tile8e.color = sym
                self.chessBoard.tile8e.piece = piece
        elif col == "f":
            if row == 1:
                self.chessBoard.tile1f.color = sym
                self.chessBoard.tile1f.piece = piece
            elif row == 2:
                self.chessBoard.tile2f.color = sym
                self.chessBoard.tile2f.piece = piece
            elif row == 3:
                self.chessBoard.tile3f.color = sym
                self.chessBoard.tile3f.piece = piece
            elif row == 4:
                self.chessBoard.tile4f.color = sym
                self.chessBoard.tile4f.piece = piece
            elif row == 5:
                self.chessBoard.tile5f.color = sym
                self.chessBoard.tile5f.piece = piece
            elif row == 6:
                self.chessBoard.tile6f.color = sym
                self.chessBoard.tile6f.piece = piece
            elif row == 7:
                self.chessBoard.tile7f.color = sym
                self.chessBoard.tile7f.piece = piece
            elif row == 8:
                self.chessBoard.tile8f.color = sym
                self.chessBoard.tile8f.piece = piece
        elif col == "g":
            if row == 1:
                self.chessBoard.tile1g.color = sym
                self.chessBoard.tile1g.piece = piece
            elif row == 2:
                self.chessBoard.tile2g.color = sym
                self.chessBoard.tile2g.piece = piece
            elif row == 3:
                self.chessBoard.tile3g.color = sym
                self.chessBoard.tile3g.piece = piece
            elif row == 4:
                self.chessBoard.tile4g.color = sym
                self.chessBoard.tile4g.piece = piece
            elif row == 5:
                self.chessBoard.tile5g.color = sym
                self.chessBoard.tile5g.piece = piece
            elif row == 6:
                self.chessBoard.tile6g.color = sym
                self.chessBoard.tile6g.piece = piece
            elif row == 7:
                self.chessBoard.tile7g.color = sym
                self.chessBoard.tile7g.piece = piece
            elif row == 8:
                self.chessBoard.tile8g.color = sym
                self.chessBoard.tile8g.piece = piece
        elif col == "h":
            if row == 1:
                self.chessBoard.tile1h.color = sym
                self.chessBoard.tile1h.piece = piece
            elif row == 2:
                self.chessBoard.tile2h.color = sym
                self.chessBoard.tile2h.piece = piece
            elif row == 3:
                self.chessBoard.tile3h.color = sym
                self.chessBoard.tile3h.piece = piece
            elif row == 4:
                self.chessBoard.tile4h.color = sym
                self.chessBoard.tile4h.piece = piece
            elif row == 5:
                self.chessBoard.tile5h.color = sym
                self.chessBoard.tile5h.piece = piece
            elif row == 6:
                self.chessBoard.tile6h.color = sym
                self.chessBoard.tile6h.piece = piece
            elif row == 7:
                self.chessBoard.tile7h.color = sym
                self.chessBoard.tile7h.piece = piece
            elif row == 8:
                self.chessBoard.tile8h.color = sym
                self.chessBoard.tile8h.piece = piece
    def play_turn(self, pick_row, pick_col, place_row, place_col, sym):
        """initiate game play"""
        if self.check(pick_row,pick_col) == sym:
            if self.check(place_row,place_col) != sym:
                piece = self.get_piece(pick_row, pick_col)
                self.make_move(place_row, place_col, sym, piece)
                self.print_board()
            else:
                print("cannot place piece there")
        else:
            print("cannot pick this piece")
        print(sym +" turn played")
    
        """Save game"""
    def print_board(self):
        print("|",self.chessBoard.tile1h.piece,"|",self.chessBoard.tile1g.piece,"|",self.chessBoard.tile1f.piece,"|",self.chessBoard.tile1e.piece,"|",self.chessBoard.tile1d.piece,"|",self.chessBoard.tile1c.piece,"|",self.chessBoard.tile1b.piece,"|",self.chessBoard.tile1a.piece)
        print("|",self.chessBoard.tile2h.piece,"|",self.chessBoard.tile2g.piece,"|",self.chessBoard.tile2f.piece,"|",self.chessBoard.tile2e.piece,"|",self.chessBoard.tile2d.piece,"|",self.chessBoard.tile2c.piece,"|",self.chessBoard.tile2b.piece,"|",self.chessBoard.tile2a.piece)
        print("|",self.chessBoard.tile3h.piece,"|",self.chessBoard.tile3g.piece,"|",self.chessBoard.tile3f.piece,"|",self.chessBoard.tile3e.piece,"|",self.chessBoard.tile3d.piece,"|",self.chessBoard.tile3c.piece,"|",self.chessBoard.tile3b.piece,"|",self.chessBoard.tile3a.piece)
        print("|",self.chessBoard.tile4h.piece,"|",self.chessBoard.tile4g.piece,"|",self.chessBoard.tile4f.piece,"|",self.chessBoard.tile4e.piece,"|",self.chessBoard.tile4d.piece,"|",self.chessBoard.tile4c.piece,"|",self.chessBoard.tile4b.piece,"|",self.chessBoard.tile4a.piece)
        print("|",self.chessBoard.tile5h.piece,"|",self.chessBoard.tile5g.piece,"|",self.chessBoard.tile5f.piece,"|",self.chessBoard.tile5e.piece,"|",self.chessBoard.tile5d.piece,"|",self.chessBoard.tile5c.piece,"|",self.chessBoard.tile5b.piece,"|",self.chessBoard.tile5a.piece)
        print("|",self.chessBoard.tile6h.piece,"|",self.chessBoard.tile6g.piece,"|",self.chessBoard.tile6f.piece,"|",self.chessBoard.tile6e.piece,"|",self.chessBoard.tile6d.piece,"|",self.chessBoard.tile6c.piece,"|",self.chessBoard.tile6b.piece,"|",self.chessBoard.tile6a.piece)
        print("|",self.chessBoard.tile7h.piece,"|",self.chessBoard.tile7g.piece,"|",self.chessBoard.tile7f.piece,"|",self.chessBoard.tile7e.piece,"|",self.chessBoard.tile7d.piece,"|",self.chessBoard.tile7c.piece,"|",self.chessBoard.tile7b.piece,"|",self.chessBoard.tile7a.piece)
        print("|",self.chessBoard.tile8h.piece,"|",self.chessBoard.tile8g.piece,"|",self.chessBoard.tile8f.piece,"|",self.chessBoard.tile8e.piece,"|",self.chessBoard.tile8d.piece,"|",self.chessBoard.tile8c.piece,"|",self.chessBoard.tile8b.piece,"|",self.chessBoard.tile8a.piece)
   

game = ChessMain("Michael", "Computer")
game.play_turn(2,"a",3,"a", "B")
game.play_turn(7,"a",6,"a", "W")
