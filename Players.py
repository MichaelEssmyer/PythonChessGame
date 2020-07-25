import copy
from Board import Board
from Board import Empty

class Player(Board):
    def __init__(self, COLOR):
        self.board = Board()
        self.color = COLOR
    def make_move(self):
        self.board.player = copy.deepcopy(self.board.tiles[self.board.pickr][self.board.pickc])
        self.board.enemy = copy.deepcopy(self.board.tiles[self.board.placer][self.board.placec])
        self.board.tiles[self.board.placer][self.board.placec].piece.char = self.board.tiles[self.board.pickr][self.board.pickc].piece.char
        self.board.tiles[self.board.placer][self.board.placec].piece.color = self.board.tiles[self.board.pickr][self.board.pickc].piece.color
        self.board.tiles[self.board.placer][self.board.placec].value = self.board.tiles[self.board.pickr][self.board.pickc].value
        self.board.tiles[self.board.placer][self.board.placec].moves = self.board.tiles[self.board.pickr][self.board.pickc].moves
        self.board.tiles[self.board.placer][self.board.placec].movesR = self.board.tiles[self.board.pickr][self.board.pickc].movesR
        self.board.tiles[self.board.placer][self.board.placec].movesC = self.board.tiles[self.board.pickr][self.board.pickc].movesC
        self.board.tiles[self.board.pickr][self.board.pickc].piece.color = "X"
        self.board.tiles[self.board.pickr][self.board.pickc].piece.char = " "
        self.board.tiles[self.board.pickr][self.board.pickc] = Empty("X"," ",self.board.pickr,self.board.pickc)
    def reverse_move(self):
        self.board.tiles[self.board.pickr][self.board.pickc] = self.board.player
        self.board.tiles[self.board.placer][self.board.placec] = self.board.enemy
    def play_turn(self):
        Turn = True
        while Turn == True:
            print("Player's turn")
            self.board.print_board()
            pick_col = input("Select pick Col: ")
            pick_row = input("Select pick Row: ")
            place_col = input("Select place Col: ")
            place_row = input("Select place Row: ")
            self.board.convert_input(pick_col,pick_row,place_col,place_row)
            if self.board.check_pick() == True:
                if self.board.check_place() == True:
                    self.make_move()
                    Turn = False
    def simulate(self, player_copy):
        every_piece = []
        for i in range(0,8):
            for j in range(0,8):
                if player_copy.board.tiles[i][j].piece.color == player_copy.board.turn:
                    player_copy.board.pickr = i
                    player_copy.board.pickc = j
                    every_move = []
                    #every_move.append([0,0,0,0,0])
                    if player_copy.board.check_pick() == True and player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].moves != 0:
                        for x in range(0,player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].moves):
                            player_copy.board.placer = player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesR[x] + player_copy.board.pickr
                            player_copy.board.placec = player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesC[x] + player_copy.board.pickc
                            if (((player_copy.board.pickr + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesR[x] < 8)
                                and (player_copy.board.pickr + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesR[x] >= 0))
                                and ((player_copy.board.pickc + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesC[x] < 8)
                                and (player_copy.board.pickc + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesC[x] >= 0))):
                                if player_copy.board.check_place() == True:
                                    #print("simulating", player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].piece.char)
                                    player_copy.make_move()
                                    player_copy.score_board()
                                    #player_copy.board.print_board()
                                    opp_score = 0
                                    #self.opp_choice(copy.deepcopy(player_copy))
                                    info = [player_copy.board.score_board-opp_score,player_copy.board.pickr,player_copy.board.pickc,player_copy.board.placer,player_copy.board.placec]
                                    every_move.append(info)
                                    player_copy.reverse_move()
                            else:
                                #print("sim piece off board, no checking placement")
                                pass
                        if len(every_move) > 0:
                            every_piece.append(self.sort_list(every_move))
        return self.choose_move(every_piece)
    def opp_choice(self,player_copy):
        every_piece = []
        for i in range(0,8):
            for j in range(0,8):
                if player_copy.board.tiles[i][j].piece.color == player_copy.board.turn:
                    player_copy.board.pickr = i
                    player_copy.board.pickc = j
                    every_move = []
                    #every_move.append([0,0,0,0,0])
                    if player_copy.board.check_pick() == True and player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].moves != 0:
                        for x in range(0,player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].moves):
                            player_copy.board.placer = player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesR[x] + player_copy.board.pickr
                            player_copy.board.placec = player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesC[x] + player_copy.board.pickc
                            if (((player_copy.board.pickr + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesR[x] < 8)
                                and (player_copy.board.pickr + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesR[x] >= 0))
                                and ((player_copy.board.pickc + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesC[x] < 8)
                                and (player_copy.board.pickc + player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].movesC[x] >= 0))):
                                if player_copy.board.check_place() == True:
                                    #print("simulating", player_copy.board.tiles[player_copy.board.pickr][player_copy.board.pickc].piece.char)
                                    player_copy.make_move()
                                    player_copy.score_board()
                                    #player_copy.board.print_board()
                                    info = [player_copy.board.score_board,player_copy.board.pickr,player_copy.board.pickc,player_copy.board.placer,player_copy.board.placec]
                                    every_move.append(info)
                                    player_copy.reverse_move()
                            else:
                                #print("sim piece off board, no checking placement")
                                pass
                        if len(every_move) > 0:
                            every_piece.append(self.sort_list(every_move))
        return self.opp_score(every_piece)
    def sort_list(self, a_list):
        #sorting the move of every piece
        for i in range(0,len(a_list)):
            if a_list[0][0] <= a_list[i][0]:
                a_list.insert(0,a_list[i])
                del a_list[i+1]
            else:
                pass
        return a_list
    def opp_score(self, a_list):
        #print(a_list[0][0].board.print_board())
        ind = len(a_list)
        #print(ind)
        for i in range(0,ind):
            lim =len(a_list[i])
            for j in range(0,lim):
                
                #print("sim opp",a_list[i][0])
                if lim == 0:
                    pass
                elif a_list[0][0] < a_list[i][0]:
                        a_list.insert(0,a_list[i])
                        del a_list[i+1]
        #print("choosing",a_list
        return a_list[0][0][0]
    def choose_move(self, a_list):
        #print(a_list[0][0].board.print_board())
        ind = len(a_list)
        #print(ind)
        for i in range(0,ind):
            lim =len(a_list[i])
            for j in range(0,lim):
                print("sim play",a_list[i][0])
                if lim == 0:
                    pass
                elif a_list[0][0] < a_list[i][0]:
                        a_list.insert(0,a_list[i])
                        del a_list[i+1]
        #print("choosing",a_list[0])
        return a_list[0][0]
                  
    def simulate_boards(self):
        every_tile = []
        player_copy = copy.deepcopy(self)
        the_move = self.simulate(player_copy)
        return the_move
    
