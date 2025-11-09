from board import Board
from player import ComputerPlayer, Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player("user")
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
    

    def show_menu(self, player: Player, location:int, board: list[object]):
        print(board[location].name)
        print(player)


    def move_on_board(self, player: Player):
        roll = player.roll_the_dice()
        print(f"The dice rolled {roll}")
        return player.move(roll)
    

    def tranfer_ownership(self, location: int, player: Player, board: list[object]):
        price = board[location].price
        player.payment(price)
        board[location].available = False
        player.propertys.append(board[location])   

       
    def player_choice(self, location:int , player: Player, board: list[object]):
        choose = player.choice()
        if choose == "s":
            return 
        else:
            if board[location].is_available():
                print(f"the price is {board[location].price}")
                answer = input("Do you want to purch? ")
                if answer == "no":
                    return
                else:
                    self.tranfer_ownership(location, player, board)
                        
   
        
    def handel_tile(self, board: list[object], player: Player, location :int):
        match board[location].tile:
            case "property":
                if board[location].is_available():
                    if isinstance(player, ComputerPlayer):
                        if player.is_buy(board, player, location):
                            self.tranfer_ownership(location, self.AI, board)
                        else:
                            print("The AI did not purch anything")
                    else:
                        self.player_choice(location, player, board)
                else:
                    # player.payment(board[location].rent)
                    pass
            case "start":
                print("Congratulation, you stept on the start board so you get a 400 $ ")
                player.get_payment(400)
            case "tax":
                player.payment(board[location].amount)
                print(f"You need to pay {board[location].amount}")
            case "bonus":
                player.get_payment(board[location].amount)
                print(f"Congratulation, you got a bonus of {board[location].amount}")
            case "end":
                print("This is the last board in the board ")
            case "go to jail":
                print("Sorry, you need to spent two rounds in jail")
                player.location = board["jail"]
            case "jail":
                print("This is just visiting no need to stay ")
        print(player)
  

    def round(self, player: Player, board: list[object]):
        current_location = self.move_on_board(player)
        self.show_menu(player, current_location, board)
        self.handel_tile(board, player, current_location)
                 
            
    def run_game(self):  
        start_first = self.roll_to_start()
        rounds = 1
        game_board = self.board.create_board()
        while rounds <= 20:
            print(f"----- Round {rounds} -----")
            if isinstance(start_first, ComputerPlayer):
                self.round(self.AI, game_board)
                print("user turn")
                self.round(self.player, game_board)
               
            else:
                self.round(self.player, game_board)
                print("AI turn")
                self.round(self.AI, game_board)
            rounds += 1


game = Game()
game.run_game()



