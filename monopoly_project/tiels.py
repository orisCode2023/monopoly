class Tile:
    def __init__(self, name, tile_type, available):
        self.name = name
        self.tile = tile_type
        self.available = available

    def is_available(self):
        return self.available

    def __str__(self):
        return f"{self.name}, is available {self.available}"
        

    
class Property(Tile):
    def __init__(self, name, tile_type, available, price_purch, rent_price, city):
        super().__init__(name, tile_type, available)
        self.price = price_purch
        self.rent = rent_price
        self.city = city
        self.ownership = None

    def __str__(self):
        return super().__str__() , f"city: {self.city}, purch: {self.price}, rent: {self.rent} "
        

class Rail(Property):
    def __init__(self, name, tile_type, available, price_purch, rent, city=None):
        super().__init__(name, tile_type, price_purch, available, rent, city=None)
    

class Bonus(Tile):
    def __init__(self, name, tile_type, available, amount):
        super().__init__(name, tile_type, available)
        self.amount = amount
        
    def __str__(self):
        return super().__str__(), f"Get: {self.amount}"



class Tax(Bonus):
    def __init__(self, name, tile_type, available, amount):
        super().__init__(name, tile_type, available, amount)
        
    def __str__(self):
        return super().__str__(), f"Pay: {self.amount}"



class Jail(Tile):
    def __init__(self, name, tile_type, available):
        super().__init__(name, tile_type, available)
        

class GoToJail(Tile):
    def __init__(self, name, tile_type, available):
        super().__init__(name, tile_type, available)
       