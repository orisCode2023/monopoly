from data import tiles_data as td
from tiels import *

class Board:
  def __init__(self):
    self.board = []

  def create_board(self):
    
    for tile in td:
        match tile["type"]:
          case "start":
            tile["name"] = Tile(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            
        
          case "tax":
            tile["name"] = Tax(tile["name"], tile["type"], False, tile["amount"])
            self.board.append(tile["name"])
            
          
          case "bonus":
            tile["name"] = Bonus(tile["name"], tile["type"], False, tile["amount"])
            self.board.append(tile["name"])
            
           
          case "end":
            tile["name"] = Tile(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            
           
          case "go_to_jail":
            tile["name"] = GoToJail(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            

          case "jail":
            tile["name"] = Jail(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            

          case "property":
            if "Rail" not in tile["name"]:
              tile["name"] = Property(tile["name"], tile["type"], True, tile["price"], tile["rent"], tile["city"])
              self.board.append(tile["name"])
              
            else:
              tile["name"] = Rail(tile["name"], tile["type"], True, tile["price"], tile["rent"], tile["city"])
              self.board.append(tile["name"])
              
          
    return self.board

     
     
    
  def check_boarders(self, current_location, steps_number):
    return (current_location + steps_number) % len(self.board)
  

       











  