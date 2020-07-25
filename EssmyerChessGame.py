from Players import Player
class Chess(Player):
    def __init__(self):
        self.players = [0 for i in range(2)]
        self.players[0] = Player("White")
        self.players[1] = Player("Black")
        self.winner = False
    def play(self):
        while self.winner == False:
            self.players[0].play_turn()
            self.players[0].board.turn = "Black"
            self.players[0].board.print_board()
            self.comp_turn()
            #self.players[0].board.print_board()
            self.players[0].board.turn = "White"
    def search_moves(self):
        play_board = self.players[0].board
        opp_moves = []
        play_moves = []
        play_moves = self.players[0].simulate_boards()
        
        self.players[0].board.pickr = play_moves[1]
        self.players[0].board.pickc = play_moves[2]
        self.players[0].board.placer = play_moves[3]
        self.players[0].board.placec = play_moves[4]
        self.players[0].make_move()
        #play_list[0].board.print_board()
        #self.players[0] = play_list[0]
        self.players[0].color = "White"
        self.players[0].board.turn = "White"
        #for i in range(0,len(play_list)):
            #for j in range(0,len(play_list[i])):
               # print(play_list[i][j])
                #opp_moves.append(play_list[i][j].simulate_boards())
        #for i in range(0,len(opp_moves)):
            #play_moves.append(opp_moves[i].simulate_boards())
        #for i in range(0,len(play_moves)):
            #for j in range(0,len(i)):
                #print(j.score)
        #print(len(play_moves))
        #self.players[0].board = play_moves[0]
            
    def comp_turn(self):
        print("computer thinking...")
        self.search_moves()
        print("finished")
    
Game = Chess()
Game.play()
#still needs depth to simulations
#still needs to check check and mate
#still needs to upgrade pawns
#still needs to castle
