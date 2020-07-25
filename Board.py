from Pieces import pawn, Pawn, Rook, Bishop, Knight, Queen, King, Empty
class Board(pawn, Pawn, Rook, Bishop, Knight, Queen, King, Empty):
    def __init__(self):
        self.turn = "White"
        self.score_board = 0
        self.board_matrix = [[1,2,3,4,4,3,2,1],[2,3,4,5,5,4,3,2],[3,4,5,6,6,5,4,3],[4,5,6,7,7,6,5,4],[4,5,6,7,7,6,5,4],[3,4,5,6,6,5,4,3],[2,3,4,5,5,4,3,2],[1,2,3,4,4,3,2,1]]
        self.pickr = 8
        self.pickc = 8
        self.placer = 8
        self.placec = 8
        self.enemy = Empty("X"," ",self.placer,self.placec)
        self.player = Empty("X"," ",self.pickr,self.pickc)
        self.tiles = [[0 for i in range(8)] for j in range(8)]
        self.tiles[0][0] = Rook("Black","R",0,0)
        self.tiles[0][1] = Knight("Black","N",0,1)
        self.tiles[0][2] = Bishop("Black","B",0,2)
        self.tiles[0][3] = King("Black","K",0,3)
        self.tiles[0][4] = Queen("Black","Q",0,4)
        self.tiles[0][5] = Bishop("Black","B",0,5)
        self.tiles[0][6] = Knight("Black","N",0,6)
        self.tiles[0][7] = Rook("Black","R",0,7)
        self.tiles[1][0] = Pawn("Black","P",1,0)
        self.tiles[1][1] = Pawn("Black","P",1,1)
        self.tiles[1][2] = Pawn("Black","P",1,2)
        self.tiles[1][3] = Pawn("Black","P",1,3)
        self.tiles[1][4] = Pawn("Black","P",1,4)
        self.tiles[1][5] = Pawn("Black","P",1,5)
        self.tiles[1][6] = Pawn("Black","P",1,6)
        self.tiles[1][7] = Pawn("Black","P",1,7)
        self.tiles[2][0] = Empty("X"," ",2,0)
        self.tiles[2][1] = Empty("X"," ",2,1)
        self.tiles[2][2] = Empty("X"," ",2,2)
        self.tiles[2][3] = Empty("X"," ",2,3)
        self.tiles[2][4] = Empty("X"," ",2,4)
        self.tiles[2][5] = Empty("X"," ",2,5)
        self.tiles[2][6] = Empty("X"," ",2,6)
        self.tiles[2][7] = Empty("X"," ",2,7)
        self.tiles[3][0] = Empty("X"," ",3,0)
        self.tiles[3][1] = Empty("X"," ",3,1)
        self.tiles[3][2] = Empty("X"," ",3,2)
        self.tiles[3][3] = Empty("X"," ",3,3)
        self.tiles[3][4] = Empty("X"," ",3,4)
        self.tiles[3][5] = Empty("X"," ",3,5)
        self.tiles[3][6] = Empty("X"," ",3,6)
        self.tiles[3][7] = Empty("X"," ",3,7)
        self.tiles[4][0] = Empty("X"," ",4,0)
        self.tiles[4][1] = Empty("X"," ",4,1)
        self.tiles[4][2] = Empty("X"," ",4,2)
        self.tiles[4][3] = Empty("X"," ",4,3)
        self.tiles[4][4] = Empty("X"," ",4,4)
        self.tiles[4][5] = Empty("X"," ",4,5)
        self.tiles[4][6] = Empty("X"," ",4,6)
        self.tiles[4][7] = Empty("X"," ",4,7)
        self.tiles[5][0] = Empty("X"," ",5,0)
        self.tiles[5][1] = Empty("X"," ",5,1)
        self.tiles[5][2] = Empty("X"," ",5,2)
        self.tiles[5][3] = Empty("X"," ",5,3)
        self.tiles[5][4] = Empty("X"," ",5,4)
        self.tiles[5][5] = Empty("X"," ",5,5)
        self.tiles[5][6] = Empty("X"," ",5,6)
        self.tiles[5][7] = Empty("X"," ",5,7)
        self.tiles[6][0] = pawn("White","p",6,0)
        self.tiles[6][1] = pawn("White","p",6,1)
        self.tiles[6][2] = pawn("White","p",6,2)
        self.tiles[6][3] = pawn("White","p",6,3)
        self.tiles[6][4] = pawn("White","p",6,4)
        self.tiles[6][5] = pawn("White","p",6,5)
        self.tiles[6][6] = pawn("White","p",6,6)
        self.tiles[6][7] = pawn("White","p",6,7)
        self.tiles[7][0] = Rook("White","r",7,0)
        self.tiles[7][1] = Knight("White","n",7,1)
        self.tiles[7][2] = Bishop("White","b",7,2)
        self.tiles[7][3] = King("White","k",7,3)
        self.tiles[7][4] = Queen("White","q",7,4)
        self.tiles[7][5] = Bishop("White","b",7,5)
        self.tiles[7][6] = Knight("White","n",7,6)
        self.tiles[7][7] = Rook("White","r",7,7)
    def check_input(self):
        correct = True
        if self.pickr == -1:
            print("Incorrect row pick")
            correct = False
        if self.pickc == -1:
            print("Incorrect col pick")
            correct = False
        if self.placer == -1:
            print("Incorrect row place")
            correct = False
        if self.placec == -1:
            print("Incorrect col place")
            correct = False
        if self.check_pick(self) == False:
            print("cannot pickup piece from there")
            correct = False
        if self.check_place(self) == False:
            print("cannot place piece there")
            correct = False
        return correct
        
    def convert_input(self,pic,pir,plc,plr):
        if pic == "a" or pic == "A":
            self.pickc = 0
        elif pic == "b" or pic == "B":
            self.pickc = 1
        elif pic == "c" or pic == "C":
            self.pickc = 2
        elif pic == "d" or pic == "D":
            self.pickc = 3
        elif pic == "e" or pic == "E":
            self.pickc = 4
        elif pic == "f" or pic == "F":
            self.pickc = 5
        elif pic == "g" or pic == "G":
            self.pickc = 6
        elif pic == "h" or pic == "H":
            self.pickc = 7
        else:
            self.pickc = -1
        if plc == "a" or plc == "A":
            self.placec = 0
        elif plc == "b" or plc == "B":
            self.placec = 1
        elif plc == "c" or plc == "C":
            self.placec = 2
        elif plc == "d" or plc == "D":
            self.placec = 3
        elif plc == "e" or plc == "E":
            self.placec = 4
        elif plc == "f" or plc == "F":
            self.placec = 5
        elif plc == "g" or plc == "G":
            self.placec = 6
        elif plc == "h" or plc == "H":
            self.placec = 7
        else:
            self.placec = -1
        if pir == "1":
            self.pickr = 0
        elif pir == "2":
            self.pickr = 1
        elif pir == "3":
            self.pickr = 2
        elif pir == "4":
            self.pickr = 3
        elif pir == "5":
            self.pickr = 4
        elif pir == "6":
            self.pickr = 5
        elif pir == "7":
            self.pickr = 6
        elif pir == "8":
            self.pickr = 7
        else:
            self.placer = -1
        if plr == "1":
            self.placer = 0
        elif plr == "2":
            self.placer = 1
        elif plr == "3":
            self.placer = 2
        elif plr == "4":
            self.placer = 3
        elif plr == "5":
            self.placer = 4
        elif plr == "6":
            self.placer = 5
        elif plr == "7":
            self.placer = 6
        elif plr == "8":
            self.placer = 7
        else:
            self.placer = -1

    def check_pick(self):
        if self.tiles[self.pickr][self.pickc].piece.color == self.turn:
            #print("pick", self.pickr, self.pickc, "is",self.turn)
            return True
        else:
            #print("pick", self.pickr, self.pickc, "is not",self.turn)
            return False
        
    def check_place(self):
        piece = self.tiles[self.pickr][self.pickc].piece.char
        if piece == "p":
            return self.cp_pawn(piece)
        elif piece == "P":
            return self.cp_Pawn(piece)
        elif piece == "n" or piece == "N":
            return self.cp_Knight(piece)
        elif piece == "b" or piece == "B":
            return self.cp_Bishop(piece)
        elif piece == "r" or piece == "R":
            return self.cp_Rook(piece)
        elif piece == "q" or piece == "Q":
            return self.cp_Queen(piece)
        elif piece == "k" or piece == "K":
            return self.cp_King(piece)
        else:
            print("placement error")
            return self.check_input()

    def cp_pawn(self, piece):
        if self.pickc == self.placec and (self.pickr - self.placer) <= 2:
            for x in range(self.pickr-1,self.placer-1,-1):
                    if x == self.placer and self.tiles[x][self.placec].piece.color == "X":
                        return True
                    elif self.tiles[x][self.placec].piece.color == "X":
                        pass
                    else:
                        False
        elif (self.pickc-self.placec == 1 or self.pickc-self.placec == -1) and self.pickr - self.placer == 1:
            if self.tiles[self.placer][self.placec].piece.color != self.tiles[self.pickr][self.pickc].piece.color and self.tiles[self.placer][self.placec].piece.color != "X":
                return True
            else:
                return False
        else:
            #print(piece,self.pickr,self.pickc,self.placer,self.placec,"out of range palcement")
            return False
    def cp_Pawn(self, piece):
        if self.pickc == self.placec and (self.placer - self.pickr) <= 2:
            for x in range(self.pickr+1,self.placer+1,1):
                    if x == self.placer and self.tiles[x][self.placec].piece.color == "X":
                        return True
                    elif self.tiles[x][self.placec].piece.color == "X":
                        pass
                    else:
                        False
        elif (self.pickc-self.placec == 1 or self.pickc-self.placec == -1) and self.placer - self.pickr == 1:
            if self.tiles[self.placer][self.placec].piece.color != self.sym and self.tiles[self.placer][self.placec].piece.color != "X":
                return True
            else:
                return False
        else:
            #print(piece,self.pickr,self.pickc,self.placer,self.placec,"out of range palcement")
            return False
    def cp_Knight(self, piece):
        if self.tiles[self.pickr][self.pickc].piece.color != self.tiles[self.placer][self.placec].piece.color:
            if (piece == "n"or piece == "N") and ((self.pickr == self.placer-2 and self.pickc == self.placec+1)or (self.pickr == self.placer+2 and self.pickc == self.placec-1)
                                                    or (self.pickr == self.placer+2 and self.pickc == self.placec+1)or(self.pickr == self.placer+1 and self.pickc == self.placec+2)
                                                    or (self.pickr == self.placer-2 and self.pickc == self.placec-1)or(self.pickr == self.placer+1 and self.pickc == self.placec-2)
                                                    or(self.pickr == self.placer-1 and self.pickc == self.placec-2)or(self.pickr == self.placer-1 and self.pickc == self.placec+2)):
                    #print("moving knight")
                    return True
                
            else:
                #print(piece,self.pickr,self.pickc,self.placer,self.placec, "incorrect placement")
                return False
        else:
            #print(piece,self.pickr,self.pickc,self.placer,self.placec, "moving on own piece")
            return False
    def cp_Bishop(self, piece):
        row = []
        col = []
        if self.pickr - self.placer == self.pickc - self.placec:
            #print("/")
            if self.pickr < self.placer and self.pickc < self.placec:
                #print("V")
                for i in range(self.pickr,self.placer+1):
                    row.append(i)
                for j in range(self.pickc,self.placec+1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
            elif self.pickr > self.placer and self.pickc > self.placec:
                #print("A")
                for i in range(self.pickr,self.placer-1,-1):
                    row.append(i)
                for j in range(self.pickc,self.placec-1,-1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
        elif self.pickr - self.placer == -(self.pickc - self.placec):
            #print("\ ")
            if self.pickr > self.placer and self.pickc < self.placec:
                #print("^")
                for i in range(self.pickr,self.placer-1,-1):
                    row.append(i)
                for j in range(self.pickc,self.placec+1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
                    
            elif self.pickr < self.placer and self.pickc > self.placec:
                #print("V")
                for i in range(self.pickr,self.placer+1):
                    row.append(i)
                for j in range(self.pickc,self.placec-1,-1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
    def cp_Rook(self, piece):
        if self.pickr == self.placer:
            if self.pickc < self.placec:
                for i in range(self.pickc,self.placec+1):
                    #print("<")
                    if i == self.placec:
                        if self.tiles[self.placer][i].piece.color == "X":
                            return True
                        elif self.tiles[self.placer][i].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placec:
                        if self.tiles[self.placer][i].piece.color == self.turn:
                            if i == self.pickc:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[self.placer][i].piece.color)
                                return False
                        elif self.tiles[self.placer][i].piece.color == "X":
                            pass
                        elif self.tiles[self.placer][i].piece.color != self.turn and self.tiles[self.placer][i].piece.color != "X":
                            if i == self.placec:
                                return True
                            else:
                                print("rook not happy")
                                return False
            elif self.placec < self.pickc:
                for i in range(self.pickc,self.placec-1,-1):
                    #print(">")
                    if i == self.placec:
                        if self.tiles[self.placer][i].piece.color == "X":
                            return True
                        elif self.tiles[self.placer][i].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placec:
                        if self.tiles[self.placer][i].piece.color == self.turn:
                            if i == self.pickc:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[self.placer][i].piece.color)
                                return False
                        elif self.tiles[self.placer][i].piece.color == "X":
                            pass
                        elif self.tiles[self.placer][i].piece.color != self.turn and self.tiles[self.placer][i].piece.color != "X":
                            if i == self.placec:
                                return True
                            else:
                                print("rook not happy")
                                return False
        elif self.pickc == self.placec:
            if self.pickr < self.placer:
                for i in range(self.pickr,self.placer+1):
                    #print("V")
                    if i == self.placer:
                        if self.tiles[i][self.placec].piece.color == "X":
                            return True
                        elif self.tiles[i][self.placec].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placer:
                        if self.tiles[i][self.placec].piece.color == self.turn:
                            if i == self.pickc:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[i][self.placec].piece.color)
                                return False
                        elif self.tiles[i][self.placec].piece.color == "X":
                            pass
                        elif self.tiles[i][self.placec].piece.color != self.turn and self.tiles[i][self.placec].piece.color != "X":
                            print("rook not happy")
                            return False
            elif self.placer < self.pickr:
                for i in range(self.pickr,self.placer-1,-1):
                    #print("A")
                    if i == self.placer:
                        if self.tiles[i][self.placec].piece.color == "X":
                            return True
                        elif self.tiles[i][self.placec].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placer:
                        if self.tiles[i][self.placec].piece.color == self.turn:
                            if i == self.pickr:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[i][self.placec].piece.color)
                                return False
                        elif self.tiles[i][self.placec].piece.color == "X":
                            pass
                        elif self.tiles[i][self.placec].piece.color != self.turn and self.tiles[i][self.placec].piece.color != "X":
                            print("rook not happy")
                            return False
    def cp_Queen(self, piece):
        row = []
        col = []
        if self.pickr - self.placer == self.pickc - self.placec:
            #print("/")
            if self.pickr < self.placer and self.pickc < self.placec:
                #print("V")
                for i in range(self.pickr,self.placer+1):
                    row.append(i)
                for j in range(self.pickc,self.placec+1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
            elif self.pickr > self.placer and self.pickc > self.placec:
                #print("A")
                for i in range(self.pickr,self.placer-1,-1):
                    row.append(i)
                for j in range(self.pickc,self.placec-1,-1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
        elif self.pickr - self.placer == -(self.pickc - self.placec):
            #print("\ ")
            if self.pickr > self.placer and self.pickc < self.placec:
                #print("^")
                for i in range(self.pickr,self.placer-1,-1):
                    row.append(i)
                for j in range(self.pickc,self.placec+1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
                    
            elif self.pickr < self.placer and self.pickc > self.placec:
                #print("V")
                for i in range(self.pickr,self.placer+1):
                    row.append(i)
                for j in range(self.pickc,self.placec-1,-1):
                    col.append(j)
                x = len(col)
                y = len(row)
                if x != y:
                    return False
                for h in range(0,x):
                    #print('here',h,x,y)
                    if self.tiles[row[h]][col[h]].piece.color != self.turn:
                        #print("in1")
                        if self.tiles[row[h]][col[h]].piece.color == "X":
                            #print("open")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                pass
                        elif self.tiles[row[h]][col[h]].piece.color != "X":
                            #print("enemy")
                            if row[h] == self.placer and col[h] == self.placec:
                                return True
                            else:
                                #print("enemy in way")
                                return False
                    elif self.tiles[row[h]][col[h]].piece.color == self.turn:
                        #print("in2")
                        if row[h] == self.pickr and col[h] == self.pickc:
                            pass
                        else:
                            #print("own piece in way")
                            return False
        elif self.pickr == self.placer:
            if self.pickc < self.placec:
                for i in range(self.pickc,self.placec+1):
                    #print("<")
                    if i == self.placec:
                        if self.tiles[self.placer][i].piece.color == "X":
                            return True
                        elif self.tiles[self.placer][i].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placec:
                        if self.tiles[self.placer][i].piece.color == self.turn:
                            if i == self.pickc:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[self.placer][i].piece.color)
                                return False
                        elif self.tiles[self.placer][i].piece.color == "X":
                            pass
                        elif self.tiles[self.placer][i].piece.color != self.turn and self.tiles[self.placer][i].piece.color != "X":
                            if i == self.placec:
                                return True
                            else:
                                print("queen not happy")
                                return False
            elif self.placec < self.pickc:
                for i in range(self.pickc,self.placec-1,-1):
                    #print(">")
                    if i == self.placec:
                        if self.tiles[self.placer][i].piece.color == "X":
                            return True
                        elif self.tiles[self.placer][i].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placec:
                        if self.tiles[self.placer][i].piece.color == self.turn:
                            if i == self.pickc:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[self.placer][i].piece.color)
                                return False
                        elif self.tiles[self.placer][i].piece.color == "X":
                            pass
                        elif self.tiles[self.placer][i].piece.color != self.turn and self.tiles[self.placer][i].piece.color != "X":
                            if i == self.placec:
                                return True
                            else:
                                print("queen not happy")
                                return False
        elif self.pickc == self.placec:
            if self.pickr < self.placer:
                for i in range(self.pickr,self.placer+1):
                    #print("V")
                    if i == self.placer:
                        if self.tiles[i][self.placec].piece.color == "X":
                            return True
                        elif self.tiles[i][self.placec].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placer:
                        if self.tiles[i][self.placec].piece.color == self.turn:
                            if i == self.pickc:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[i][self.placec].piece.color)
                                return False
                        elif self.tiles[i][self.placec].piece.color == "X":
                            pass
                        elif self.tiles[i][self.placec].piece.color != self.turn and self.tiles[i][self.placec].piece.color != "X":
                            print("queen not happy")
                            return False
            elif self.placer < self.pickr:
                for i in range(self.pickr,self.placer-1,-1):
                    #print("A")
                    if i == self.placer:
                        if self.tiles[i][self.placec].piece.color == "X":
                            return True
                        elif self.tiles[i][self.placec].piece.color == self.turn:
                            return False
                        else:
                            return True
                    elif i != self.placer:
                        if self.tiles[i][self.placec].piece.color == self.turn:
                            if i == self.pickr:
                                pass
                            else:
                                #print(piece,self.pickr,self.pickc,self.placer,i,"piece in the way",self.tiles[i][self.placec].piece.color)
                                return False
                        elif self.tiles[i][self.placec].piece.color == "X":
                            pass
                        elif self.tiles[i][self.placec].piece.color != self.turn and self.tiles[i][self.placec].piece.color != "X":
                            print("queen not happy")
                            return False
    def cp_King(self, piece):
        if ((self.pickr == self.placer+1 and self.pickc == self.placec)
         or(self.pickr == self.placer-1 and self.pickc ==self.placec)
         or(self.pickr == self.placer and self.pickc == self.placec+1)
         or(self.pickr == self.placer and self.pickc == self.placec-1)):
            if(self.tiles[self.placer][self.placec].piece.color != self.turn):
                print("Moving King")
                return True
            else:
                #print(self.placer,self.placec,"piece in the way")
                return False
        else:
            print("out of range")
            return False
    def score_board(self):
        self.board.score_board = 0
        for i in range(0,8):
            for j in range(0,8):
                if self.board.tiles[i][j].piece.color == "Black":
                    #print("+",self.board.tiles[i][j].value,"*",self.board.board_matrix[i][j],self.board.tiles[i][j].piece.char)
                    self.board.score_board += (self.board.board_matrix[i][j]*self.board.tiles[i][j].value)
                elif self.board.tiles[i][j].piece.color == "White":
                    #print("-",self.board.tiles[i][j].value,"*",self.board.board_matrix[i][j],self.board.tiles[i][j].piece.char)
                    self.board.score_board -= (self.board.board_matrix[i][j]*self.board.tiles[i][j].value)
        
    def print_board(self):
        print("|",self.tiles[0][7].piece.char,"|",self.tiles[0][6].piece.char,"|",self.tiles[0][5].piece.char,"|",self.tiles[0][4].piece.char,"|",self.tiles[0][3].piece.char,"|",self.tiles[0][2].piece.char,"|",self.tiles[0][1].piece.char,"|",self.tiles[0][0].piece.char,"| 1")
        print("|",self.tiles[1][7].piece.char,"|",self.tiles[1][6].piece.char,"|",self.tiles[1][5].piece.char,"|",self.tiles[1][4].piece.char,"|",self.tiles[1][3].piece.char,"|",self.tiles[1][2].piece.char,"|",self.tiles[1][1].piece.char,"|",self.tiles[1][0].piece.char,"| 2")
        print("|",self.tiles[2][7].piece.char,"|",self.tiles[2][6].piece.char,"|",self.tiles[2][5].piece.char,"|",self.tiles[2][4].piece.char,"|",self.tiles[2][3].piece.char,"|",self.tiles[2][2].piece.char,"|",self.tiles[2][1].piece.char,"|",self.tiles[2][0].piece.char,"| 3")
        print("|",self.tiles[3][7].piece.char,"|",self.tiles[3][6].piece.char,"|",self.tiles[3][5].piece.char,"|",self.tiles[3][4].piece.char,"|",self.tiles[3][3].piece.char,"|",self.tiles[3][2].piece.char,"|",self.tiles[3][1].piece.char,"|",self.tiles[3][0].piece.char,"| 4")
        print("|",self.tiles[4][7].piece.char,"|",self.tiles[4][6].piece.char,"|",self.tiles[4][5].piece.char,"|",self.tiles[4][4].piece.char,"|",self.tiles[4][3].piece.char,"|",self.tiles[4][2].piece.char,"|",self.tiles[4][1].piece.char,"|",self.tiles[4][0].piece.char,"| 5")
        print("|",self.tiles[5][7].piece.char,"|",self.tiles[5][6].piece.char,"|",self.tiles[5][5].piece.char,"|",self.tiles[5][4].piece.char,"|",self.tiles[5][3].piece.char,"|",self.tiles[5][2].piece.char,"|",self.tiles[5][1].piece.char,"|",self.tiles[5][0].piece.char,"| 6")
        print("|",self.tiles[6][7].piece.char,"|",self.tiles[6][6].piece.char,"|",self.tiles[6][5].piece.char,"|",self.tiles[6][4].piece.char,"|",self.tiles[6][3].piece.char,"|",self.tiles[6][2].piece.char,"|",self.tiles[6][1].piece.char,"|",self.tiles[6][0].piece.char,"| 7")
        print("|",self.tiles[7][7].piece.char,"|",self.tiles[7][6].piece.char,"|",self.tiles[7][5].piece.char,"|",self.tiles[7][4].piece.char,"|",self.tiles[7][3].piece.char,"|",self.tiles[7][2].piece.char,"|",self.tiles[7][1].piece.char,"|",self.tiles[7][0].piece.char,"| 8")
        print("  _   _   _   _   _   _   _   _")
        print("  h   g   f   e   d   c   b   a")
