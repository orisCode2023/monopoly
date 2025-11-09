class Banker():
    def __init__(self):
        self.money = 10000
        self.propertys = []

    
    def transfer_ownership(self, property: object):
        self.propertys.pop(property)

    def get_tax(self, amount):
        self.money += amount

    def pay_bonus(self, amount):
        self.money -= amount

    def house_and_hotel(self):
        pass

    def lown_money(self, amount):
        self.money -= amount

