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
        self.tiles[2][0] = Tile(" ","X")
        self.tiles[2][1] = Tile(" ","X")
        self.tiles[2][2] = Tile(" ","X")
        self.tiles[2][3] = Tile(" ","X")
        self.tiles[2][4] = Tile(" ","X")
        self.tiles[2][5] = Tile(" ","X")
        self.tiles[2][6] = Tile(" ","X")
        self.tiles[2][7] = Tile(" ","X")
        self.tiles[3][0] = Tile(" ","X")
        self.tiles[3][1] = Tile(" ","X")
        self.tiles[3][2] = Tile(" ","X")
        self.tiles[3][3] = Tile(" ","X")
        self.tiles[3][4] = Tile(" ","X")
        self.tiles[3][5] = Tile(" ","X")
        self.tiles[3][6] = Tile(" ","X")
        self.tiles[3][7] = Tile(" ","X")
        self.tiles[4][0] = Tile(" ","X")
        self.tiles[4][1] = Tile(" ","X")
        self.tiles[4][2] = Tile(" ","X")
        self.tiles[4][3] = Tile(" ","X")
        self.tiles[4][4] = Tile(" ","X")
        self.tiles[4][5] = Tile(" ","X")
        self.tiles[4][6] = Tile(" ","X")
        self.tiles[4][7] = Tile(" ","X")
        self.tiles[5][0] = Tile(" ","X")
        self.tiles[5][1] = Tile(" ","X")
        self.tiles[5][2] = Tile(" ","X")
        self.tiles[5][3] = Tile(" ","X")
        self.tiles[5][4] = Tile(" ","X")
        self.tiles[5][5] = Tile(" ","X")
        self.tiles[5][6] = Tile(" ","X")
        self.tiles[5][7] = Tile(" ","X")
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
        self.tiles[7][3] = Tile("k","W")
        self.tiles[7][4] = Tile("q","W")
        self.tiles[7][5] = Tile("B","W")
        self.tiles[7][6] = Tile("n","W")
        self.tiles[7][7] = Tile("r","W")        
        
class Player():
    def __init__(self, name, sym):
        self.name = name
        self.sym = sym
        self.turn = True
class ChessMain(Board, Player):
    def __init__(self,Player1,Player2):
        self.game_won = False
        """create starting board"""
        self.chessBoard = Board()
        """input players"""
        self.players = [0 for i in range(2)]
        self.players[0] = Player(Player1, "W")
        self.players[1] = Player(Player2, "B")
    def check_check(self):
        """king is on tile in range of opponent"""
    def check_winner(self):
        """king is in check and cannot be saved"""
    def check_pick(self, row, col):
        print("checking pick")
        return self.chessBoard.tiles[row][col].color
    def check_place(self, pickr, pickc, row, col, piece, player):
        print("checking placement")
        if piece == "p" and ((pickr == row+1 and pickc == col and self.chessBoard.tiles[pickr][pickc].color == "X")
                             or ((pickr == row+1 and (pickc+1 == col or pickc-1 == col)
                                 and (self.chessBoard.tiles[row][col].color != "X"
                                and self.chessBoard.tiles[row][col].color !=self.chessBoard.tiles[pickr][pickc].color))
                             or((pickr==row+2 and pickc==col) and self.chessBoard.tiles[pickr-1][pickc].color == "X"
                                and self.chessBoard.tiles[row][col].color == "X"))):
            print("moving pawn")
            return self.chessBoard.tiles[row][col].color            
        elif piece == "P"and ((pickr == row-1 and pickc == col and self.chessBoard.tiles[pickr][pickc].color == "X")
                             or ((pickr == row-1 and (pickc-1 == col or pickc+1 == col)
                                 and (self.chessBoard.tiles[row][col].color != "X"
                                and self.chessBoard.tiles[row][col].color !=self.chessBoard.tiles[pickr][pickc].color)))
                             or((pickr==row-2 and pickc==col) and self.chessBoard.tiles[pickr+1][pickc].color == "X"
                                and self.chessBoard.tiles[row][col].color == "X")):
            print("moving pawn")
            return self.chessBoard.tiles[row][col].color

        elif (piece == "n"or piece == "N") and ((pickr == row-2 and pickc == col+1)or (pickr == row+2 and pickc == col-1)
                                                or (pickr == row+2 and pickc == col+1)or(pickr == row+1 and pickc == col+2)
                                                or (pickr == row-2 and pickc == col-1)or(pickr == row+1 and pickc == col-2)
                                                or(pickr == row-1 and pickc == col-2)or(pickr == row-1 and pickc == col+2)):
            print("moving knight")
            return self.chessBoard.tiles[row][col].color
        
        elif (piece == "k" or piece == "K") and ((pickr == row+1 and pickc ==col)or(pickr == row-1 and pickc ==col) or(pickr == row and pickc ==col+1)or(pickr == row and pickc ==col-1)) and (self.chessBoard.tiles[row][col].color != self.players[player].sym):
            print("moving king")
            return self.chessBoard.tiles[row][col].color
        
        elif (piece == "b" or piece == "B"):
            if pickr < row:
                if pickc < col:
                    for i in range(pickr, row):
                        for j in range(pickc, col):
                            print("<r<c", i, j)
                            if (i-row) == (j-col):
                                if self.chessBoard.tiles[i][j].color != "X":
                                    return self.players[player].sym
                            else:
                                pass
                elif pickc > col:
                    for i in range(pickr, row):
                        for j in range(col, pickc):
                            print("<r>c",i,j)
                            if (i-row) == (col-j):
                                if self.chessBoard.tiles[i][j].color != "X":
                                    return self.players[player].sym
                            else:
                                pass
            elif pickr > row:
                if pickc < col:
                    for i in range(row,pickr):
                        for j in range(pickc, col):
                            print(">r<c",i,j)
                            if (row-i) == (j-col):
                                if self.chessBoard.tiles[i][j].color != "X":
                                    return self.players[player].sym
                            else:
                                pass
                elif pickc > col:
                    for i in range(row,pickr):
                        for j in range(col, pickc):
                            print(">r>c",i,j)
                            if (row-i) == (col-j):
                                if self.chessBoard.tiles[i][j].color != "X":
                                    return self.players[player].sym
                            else:
                                pass
            print("moving bishop")
            return self.chessBoard.tiles[row][col].color
        
        elif (piece == "r" or piece == "R"):
            if pickc != col and pickr == row:
                if pickc > col:
                    for x in range(pickc, col,-1):
                        if self.chessBoard.tiles[row][x].color != "X":
                            return self.players[player].sym
                elif pickc < col:
                    for x in range(pickc, col,1):
                        if self.chessBoard.tiles[row][x].color != "X":
                            return self.players[player].sym
            elif pickr != row and pickc == col:
                if pickr > row:
                    for t in range(pickr, row,-1):
                        if self.chessBoard.tiles[t][col].color != "X":
                            return self.players[player].sym
                elif pickr < row:
                    for t in range(pickr, row,1):
                        if self.chessBoard.tiles[t][col].color != "X":
                            return self.players[player].sym
            else:
                return self.players[player].sym
            print("moving rook")
            return self.chessBoard.tiles[row][col].color
        
        elif (piece == "q" or piece == "Q"):
            if ((pickr - row == pickc-col or pickr - row == -(pickc-col)
                or row-pickr == pickc-col or row-pickr  == -(pickc-col))
                or((pickr == row and pickc != col) or (pickc == col and pickr != row))):
                if pickc != col and pickr == row:
                    if pickc > col:
                        for x in range(pickc, col,-1):
                            if self.chessBoard.tiles[row][x].color != "X":
                                return self.players[player].sym
                    elif pickc < col:
                        for x in range(pickc, col,1):
                            if self.chessBoard.tiles[row][x].color != "X":
                                return self.players[player].sym
                elif pickr != row and pickc == col:
                    if pickr > row:
                        for t in range(pickr, row,-1):
                            if self.chessBoard.tiles[t][col].color != "X":
                                return self.players[player].sym
                    elif pickr < row:
                        for t in range(pickr, row,1):
                            if self.chessBoard.tiles[t][col].color != "X":
                                return self.players[player].sym
                else:
                    if pickr < row:
                        if pickc < col:
                            for i in range(pickr, row):
                                for j in range(pickc, col):
                                    print("<r<c", i, j)
                                    if (i-row) == (j-col):
                                        if self.chessBoard.tiles[i][j].color != "X":
                                            return self.players[player].sym
                                    else:
                                        pass
                        elif pickc > col:
                            for i in range(pickr, row):
                                for j in range(col, pickc):
                                    print("<r>c",i,j)
                                    if (i-row) == (col-j):
                                        if self.chessBoard.tiles[i][j].color != "X":
                                            return self.players[player].sym
                                    else:
                                        pass
                    elif pickr > row:
                        if pickc < col:
                            for i in range(row,pickr):
                                for j in range(pickc, col):
                                    print(">r<c",i,j)
                                    if (row-i) == (j-col):
                                        if self.chessBoard.tiles[i][j].color != "X":
                                            return self.players[player].sym
                                    else:
                                        pass
                        elif pickc > col:
                            for i in range(row,pickr):
                                for j in range(col, pickc):
                                    print(">r>c",i,j)
                                    if (row-i) == (col-j):
                                        if self.chessBoard.tiles[i][j].color != "X":
                                            return self.players[player].sym
                                    else:
                                        pass
                        print("moving queen")
                        return self.chessBoard.tiles[row][col].color
                    else:
                        return self.players[player].sym
        else:
            return self.players[player].sym
                             
    def get_piece(self, row, col):
        temp = self.chessBoard.tiles[row][col].piece
        self.chessBoard.tiles[row][col].piece = " "
        self.chessBoard.tiles[row][col].color = "X"
        return temp
    def make_move(self, row, col, sym, piece):
        self.chessBoard.tiles[row][col].color = sym
        self.chessBoard.tiles[row][col].piece = piece
    def convert_col(self, a_col):
        if a_col == "a":
            return 0
        elif a_col == "b":
            return 1
        elif a_col == "c":
            return 2
        elif a_col == "d":
            return 3
        elif a_col == "e":
            return 4
        elif a_col == "f":
            return 5
        elif a_col == "g":
            return 6
        elif a_col == "h":
            return 7
    def convert_row(self, a_row):
        if a_row == "1":
            return 0
        elif a_row == "2":
            return 1
        elif a_row == "3":
            return 2
        elif a_row == "4":
            return 3
        elif a_row == "5":
            return 4
        elif a_row == "6":
            return 5
        elif a_row == "7":
            return 6
        elif a_row == "8":
            return 7
    def play_turn(self, pick_row, pick_col, place_row, place_col, player):
        pick_c = self.convert_col(pick_col)
        place_c = self.convert_col(place_col) 
        pick_r = self.convert_row(pick_row)
        place_r = self.convert_row(place_row)
        """initiate game play"""
        if self.check_pick(pick_r,pick_c) == self.players[player].sym:
            if self.check_place(pick_r, pick_c, place_r,place_c, self.chessBoard.tiles[pick_r][pick_c].piece,player) != self.players[player].sym:
                piece = self.get_piece(pick_r, pick_c)
                self.make_move(place_r, place_c, self.players[player].sym, piece)
                self.players[player].turn=False
                print(self.players[player].name +" turn played")
            else:
                print("cannot place piece ",pick_r+1,pick_c+1, " there",place_r+1, place_c+1)
        else:
            print("cannot pick this piece")
        
    
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
while game.game_won == False:
    while game.players[0].turn == True:
        try:
            print("It is ",game.players[0].name, "'s turn")
            game.print_board()
            Michael_pick_row = input("Select pick Row: ")
            Michael_pick_col = input("Select pick Col: ")
            Michael_place_row = input("Select place Row: ")
            Michael_place_col = input("Select place Col: ")
            game.play_turn(Michael_pick_row,Michael_pick_col,Michael_place_row,Michael_place_col, 0)
        except TypeError:
            print("Incorrect input")
            continue
        game.players[1].turn = True
    """check board state"""
    while game.players[1].turn == True:
        try:
            print("It is ",game.players[1].name, "'s turn")
            game.print_board()
            Computer_pick_row = input("Select pick Row: ")
            Computer_pick_col = input("Select pick Col: ")
            Computer_place_row = input("Select place Row: ")
            Computer_place_col = input("Select place Col: ")
            game.play_turn(Computer_pick_row,Computer_pick_col,Computer_place_row,Computer_place_col, 1)
        except TypeError:
            print("Incorrect input")
            continue
        game.players[0].turn = True
    """check board state"""
"""report winner"""

