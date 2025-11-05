from itertools import count
import random


class Player:
    def __init__(self, name, location=0, money=1500):
        self.name = name
        self.location = location
        self.money = money
        self.propertys = []

    
    def payment(self, amount):
        self.money -= amount

    def get_payment(self, amount):
        self.money += amount

    def is_lost(self):
        return self.money == 0
    
    def roll_the_dice(self):
        return random.randint(1, 6)

    def move(self, value):
        self.location += value
        return self.location
    
    def choice(self):
        return input("Enter S to skip the turn or P to purches")
    
    def __str__(self):
        return f"Money left: {self.money}, You the owner of {self.propertys} "

    

class ComputerPlayer(Player):
    def __init__(self, name="AI", location=0, money=1500):
        super().__init__(name, location, money)
        self.name = name
        self.location = location
        self.money = money

    def check_money(self):
        return self.money <= 200
    
    def check_other_player_property(self, other, board):
        return count (other.city == board.city) >= 2
    
    def calc_avg_price(self, board):
        total = counter = 0
        for tile in board:
            if tile.available is True:
                counter += 1
                total += tile.price_purch
        return total / counter
    
    def is_cheap(self, board):
        return board.price <= self.calc_avg_price(board) 


    
        