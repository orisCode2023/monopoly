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
        if self.location + value > 33:
            self.location = (self.location + value) - 34
        else:
            self.location += value
        return self.location
    
    def choice(self):
        return input("Enter S to skip the turn or P to purches ")
 
    def __str__(self):
        lst = []
        for city in self.propertys:
            lst.append(city.name)
        return f"{self.name} has money left: {self.money}, He is the owner of {lst} "

    

class ComputerPlayer(Player):
    def __init__(self, name="AI", location=0, money=1500):
        super().__init__(name, location, money)
        
    def check_money(self):
        return self.money >= 200
    
    def check_other_player_property(self, other: Player, board:list[object], location):
        counter  = 0
        for prop in self.propertys:
            if prop.city == board[location].city:
                counter += 1
        return counter <= 2
    
    def calc_avg_price(self, board: list[object]):
        total = counter = 0
        for tile in board:
            if tile.available is True:
                counter += 1
                total += tile.price
        return total / counter
    
    def is_cheap(self, board: list[object], location):
        return board[location].price <= self.calc_avg_price(board) 
    
    def is_buy(self, board: list[object], other: Player, location):
        return self.is_cheap(board, location) and self.check_other_player_property(other, board, location) and self.check_money()
            

    
# p = Player("aksjdf")
# a = ComputerPlayer()


 
