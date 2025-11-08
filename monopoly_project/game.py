from board import Board
from player import ComputerPlayer, Player


class Game:
    def __init__(self):
        self.board = Board()
        # self.player = Player(input("Enter your name: "))
        self.player = Player("ori")
        self.AI = ComputerPlayer()
       
    def roll_to_start(self):
        while True:
            print(f"{self.player.name} roll the dice ")
            first = self.player.roll_the_dice()
            print(first)
            print(f"{self.AI.name} roll the dice ")
            second = self.AI.roll_the_dice()
            print(second)
            if first > second:
                print(f"{self.player.name} starts")
                return self.player
            elif first <  second:
                print(f"{self.AI.name} starts")
                return self.AI
            else:
                continue
    
    def show_menu(self, player: Player, location:int):
        print(self.board.board[location].name)
        print(player)
     
    def move_on_board(self, player: Player, ):
        roll = player.roll_the_dice()
        print(f"The dice rolled {roll}")
        return player.move(roll)
    
    def tranfer_ownership(self, location: int, player: Player):
        price = self.board.board[location].price
        player.payment(price)
        self.board.board[location].available = False
        player.propertys.append(self.board.board[location])

    
        
    def player_choice(self, location:int , player: Player):
        choose = player.choice()
        if choose == "s":
            return 
        else:
            if self.board.board[location].is_available():
                print(f"the price is {self.board.board[location].price}")
                answer = input("Do you want to purch? ")
                if answer == "no":
                    return
                else:
                    self.tranfer_ownership(location, player)
                        
    def handel_tile(self, tile, player: Player):
        match tile.tile:
            case "property":
                if isinstance(player, ComputerPlayer):
                    if player.check_money():
                        self.tranfer_ownership(self.board.board.index(tile), self.AI)
                else:
                    self.player_choice(self.board.board.index(tile), player)
            case "start":
                player.get_payment(400)
            case "tax":
                player.payment(tile.amount)
            case "bonus":
                player.get_payment(tile.amount)
            case "end":
                print("This is the last tile in the board ")
            case "go to jail":
                player.location = self.board.board["jail"]
            case "jail":
                print("This is just visiting no need to stay ")
        print(player)
  
    def round(self, player: Player):
        current_location = self.move_on_board(player)
        self.show_menu(player, current_location)
        self.handel_tile(self.board.board[current_location], player)
                 
            
    def run_game(self):
        start_first = self.roll_to_start()
        rounds = 1
        self.board.board = self.board.create_board()
        while rounds <= 20:
            print(f"----- Round {rounds} -----")
            if isinstance(start_first, ComputerPlayer):
                self.round(self.AI)
                self.round(self.player)
               
            else:
                self.round(self.player)
                self.round(self.AI)
            rounds += 1


game = Game()
game.run_game()



