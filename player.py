import math
import random

class player:
    def __init__(self,symbol):
        self.symbol=symbol


    def get_move(self,game):
        pass


class randomComputerPlayer(player):

      def __init__(self,symbol):
        super().__init__(symbol)
          
      def get_move(self,game):
        square=random.choice(game.available_moves())
        return square

class humanPlayer(player):
     def __init__(self,symbol):
        super().__init__(symbol)  

     def get_move(self,game):
        valid_square=False
        val=None 
        while not valid_square: 
            square=input(self.symbol+'\'s turn.Input move (0-9):') 

            try:

              val=int(square)
              if val not in game.available_move():
                  raise ValueError
              valid_square=True
            except ValueError:
                print("invalid .Try again") 
              
            return val     





