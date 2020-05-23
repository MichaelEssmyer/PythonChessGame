class Tile:
    def __init__(self, PIECE, COLOR):
        self.piece = PIECE
        self.color = COLOR
        
class Board(Tile): 
    def __init__(self):
        self.tiles = [[0 for i in range(8)] for j in range(8)]
        self.tiles[0][0] = Tile("R","B")
        self.tiles[0][1] = Tile("N","B")
        self.tiles[0][2] = Tile("B","B")
        self.tiles[0][3] = Tile("K","B")
        self.tiles[0][4] = Tile("Q","B")
        self.tiles[0][5] = Tile("B","B")
        self.tiles[0][6] = Tile("N","B")
        self.tiles[0][7] = Tile("R","B")
        self.tiles[1][0] = Tile("P","B")
        self.tiles[1][1] = Tile("P","B")
        self.tiles[1][2] = Tile("P","B")
        self.tiles[1][3] = Tile("P","B")
        self.tiles[1][4] = Tile("P","B")
        self.tiles[1][5] = Tile("P","B")
        self.tiles[1][6] = Tile("P","B")
        self.tiles[1][7] = Tile("P","B")
        self.tiles[2][0] = Tile(" ","")
        self.tiles[2][1] = Tile(" ","")
        self.tiles[2][2] = Tile(" ","")
        self.tiles[2][3] = Tile(" ","")
        self.tiles[2][4] = Tile(" ","")
        self.tiles[2][5] = Tile(" ","")
        self.tiles[2][6] = Tile(" ","")
        self.tiles[2][7] = Tile(" ","")
        self.tiles[3][0] = Tile(" ","")
        self.tiles[3][1] = Tile(" ","")
        self.tiles[3][2] = Tile(" ","")
        self.tiles[3][3] = Tile(" ","")
        self.tiles[3][4] = Tile(" ","")
        self.tiles[3][5] = Tile(" ","")
        self.tiles[3][6] = Tile(" ","")
        self.tiles[3][7] = Tile(" ","")
        self.tiles[4][0] = Tile(" ","")
        self.tiles[4][1] = Tile(" ","")
        self.tiles[4][2] = Tile(" ","")
        self.tiles[4][3] = Tile(" ","")
        self.tiles[4][4] = Tile(" ","")
        self.tiles[4][5] = Tile(" ","")
        self.tiles[4][6] = Tile(" ","")
        self.tiles[4][7] = Tile(" ","")
        self.tiles[5][0] = Tile(" ","")
        self.tiles[5][1] = Tile(" ","")
        self.tiles[5][2] = Tile(" ","")
        self.tiles[5][3] = Tile(" ","")
        self.tiles[5][4] = Tile(" ","")
        self.tiles[5][5] = Tile(" ","")
        self.tiles[5][6] = Tile(" ","")
        self.tiles[5][7] = Tile(" ","")
        self.tiles[6][0] = Tile("p","W")
        self.tiles[6][1] = Tile("p","W")
        self.tiles[6][2] = Tile("p","W")
        self.tiles[6][3] = Tile("p","W")
        self.tiles[6][4] = Tile("p","W")
        self.tiles[6][5] = Tile("p","W")
        self.tiles[6][6] = Tile("p","W")
        self.tiles[6][7] = Tile("p","W")
        self.tiles[7][0] = Tile("r","W")
        self.tiles[7][1] = Tile("n","W")
        self.tiles[7][2] = Tile("b","W")
        self.tiles[7][3] = Tile("q","W")
        self.tiles[7][4] = Tile("k","W")
        self.tiles[7][5] = Tile("B","W")
        self.tiles[7][6] = Tile("n","W")
        self.tiles[7][7] = Tile("r","W")        
        
        
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
        return self.chessBoard.tiles[row][col].color
    def get_piece(self, row, col):
        temp = self.chessBoard.tiles[row][col].piece
        self.chessBoard.tiles[row][col].piece = " "
        self.chessBoard.tiles[row][col].color = ""
        return temp
    def make_move(self, row, col, sym, piece):
        self.chessBoard.tiles[row][col].color = sym
        self.chessBoard.tiles[row][col].piece = piece
    def convert(self, a_col):
        if a_col == "a":
            return 1
        elif a_col == "b":
            return 2
        elif a_col == "c":
            return 3
        elif a_col == "d":
            return 4
        elif a_col == "e":
            return 5
        elif a_col == "f":
            return 6
        elif a_col == "g":
            return 7
        elif a_col == "h":
            return 8
    def play_turn(self, pick_row, pick_col, place_row, place_col, sym):
        pick_col = self.convert(pick_col) - 1
        place_col = self.convert(place_col) - 1
        pick_row -= 1
        place_row -=1
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
        print("|",self.chessBoard.tiles[0][7].piece,"|",self.chessBoard.tiles[0][6].piece,"|",self.chessBoard.tiles[0][5].piece,"|",self.chessBoard.tiles[0][4].piece,"|",self.chessBoard.tiles[0][3].piece,"|",self.chessBoard.tiles[0][2].piece,"|",self.chessBoard.tiles[0][1].piece,"|",self.chessBoard.tiles[0][0].piece,"| 1")
        print("|",self.chessBoard.tiles[1][7].piece,"|",self.chessBoard.tiles[1][6].piece,"|",self.chessBoard.tiles[1][5].piece,"|",self.chessBoard.tiles[1][4].piece,"|",self.chessBoard.tiles[1][3].piece,"|",self.chessBoard.tiles[1][2].piece,"|",self.chessBoard.tiles[1][1].piece,"|",self.chessBoard.tiles[1][0].piece,"| 2")
        print("|",self.chessBoard.tiles[2][7].piece,"|",self.chessBoard.tiles[2][6].piece,"|",self.chessBoard.tiles[2][5].piece,"|",self.chessBoard.tiles[2][4].piece,"|",self.chessBoard.tiles[2][3].piece,"|",self.chessBoard.tiles[2][2].piece,"|",self.chessBoard.tiles[2][1].piece,"|",self.chessBoard.tiles[2][0].piece,"| 3")
        print("|",self.chessBoard.tiles[3][7].piece,"|",self.chessBoard.tiles[3][6].piece,"|",self.chessBoard.tiles[3][5].piece,"|",self.chessBoard.tiles[3][4].piece,"|",self.chessBoard.tiles[3][3].piece,"|",self.chessBoard.tiles[3][2].piece,"|",self.chessBoard.tiles[3][1].piece,"|",self.chessBoard.tiles[3][0].piece,"| 4")
        print("|",self.chessBoard.tiles[4][7].piece,"|",self.chessBoard.tiles[4][6].piece,"|",self.chessBoard.tiles[4][5].piece,"|",self.chessBoard.tiles[4][4].piece,"|",self.chessBoard.tiles[4][3].piece,"|",self.chessBoard.tiles[4][2].piece,"|",self.chessBoard.tiles[4][1].piece,"|",self.chessBoard.tiles[4][0].piece,"| 5")
        print("|",self.chessBoard.tiles[5][7].piece,"|",self.chessBoard.tiles[5][6].piece,"|",self.chessBoard.tiles[5][5].piece,"|",self.chessBoard.tiles[5][4].piece,"|",self.chessBoard.tiles[5][3].piece,"|",self.chessBoard.tiles[5][2].piece,"|",self.chessBoard.tiles[5][1].piece,"|",self.chessBoard.tiles[5][0].piece,"| 6")
        print("|",self.chessBoard.tiles[6][7].piece,"|",self.chessBoard.tiles[6][6].piece,"|",self.chessBoard.tiles[6][5].piece,"|",self.chessBoard.tiles[6][4].piece,"|",self.chessBoard.tiles[6][3].piece,"|",self.chessBoard.tiles[6][2].piece,"|",self.chessBoard.tiles[6][1].piece,"|",self.chessBoard.tiles[6][0].piece,"| 7")
        print("|",self.chessBoard.tiles[7][7].piece,"|",self.chessBoard.tiles[7][6].piece,"|",self.chessBoard.tiles[7][5].piece,"|",self.chessBoard.tiles[7][4].piece,"|",self.chessBoard.tiles[7][3].piece,"|",self.chessBoard.tiles[7][2].piece,"|",self.chessBoard.tiles[7][1].piece,"|",self.chessBoard.tiles[7][0].piece,"| 8")
        print("  h   g   f   e   d   c   b   a")

game = ChessMain("Michael", "Computer")
game.play_turn(2,"a",3,"a", "B")
game.play_turn(7,"a",6,"a", "W")
