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
            break
        
          case "tax":
            tile["name"] = Tax(tile["name"], tile["type"], False, tile["amount"])
            self.board.append(tile["name"])
            break
          
          case "bonus":
            tile["name"] = Bonus(tile["name"], tile["type"], False, tile["amount"])
            self.board.append(tile["name"])
            break
           
          case "end":
            tile["name"] = Tile(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            break
           
          case "go_to_jail":
            tile["name"] = GoToJail(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            break

          case "jail":
            tile["name"] = Jail(tile["name"], tile["type"], False)
            self.board.append(tile["name"])
            break

          case "property":
            if "Rail" not in tile["name"]:
              tile["name"] = Property(tile["name"], tile["type"], True, tile["price"], tile["rent"], tile["city"])
              self.board.append(tile["name"])
              break
            else:
              tile["name"] = Rail(tile["name"], tile["type"], True, tile["price"], tile["rent"], tile["city"])
              self.board.append(tile["name"])
              break
          
    return self.board

     
  def check_boarders(self, current_location, steps_number):
    location = current_location
    if (current_location + steps_number) > len(self.board):
        location = ((len(self.board) - current_location) + steps_number ) -1 
    return location
                       











  