from board import Board
from player import ComputerPlayer, Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player = Player(input("Enter your name: "))
        self.AI = ComputerPlayer()
       

    def roll_to_start(self):
        while True:
            print("Player roll the dice ")
            first = self.player.roll_the_dice()
            print(first)
            print("AI roll the dice ")
            second = self.AI.roll_the_dice()
            print(second)
            if first > second:
                print( "player starts")
                break
            elif first <  second:
                print ("AI starts")
                break
            else:
                continue

    def run_game(self):
        self.roll_to_start()
        rounds = 1
        while rounds <= 20:
            print(f"----- Round {rounds} -----")
            roll = self.player.roll_the_dice()
            current = self.player.move(roll)
            location = self.board.check_boarders(self.player.location, roll)
            print(self.board.board[location])
            # choose = self.player.choice()
            # if choose == "s":
            #     continue
            # else:
            #     if self.board.board[current].is_available:
            #         answer = input("Do you want to purch? ")
            #         if answer == "no":
            #             continue
            #         else:
            #             price = self.board.board[current].price
            #             self.player.payment(price)
            #             self.board.board[current].available = False



            
            
         
            rounds += 1


game = Game()
game.run_game()