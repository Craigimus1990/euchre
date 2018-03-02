from deck import Deck, Card
import random

class Euchre:

  def __init__(self):
    ## Setup game
    self.deck = Deck()
    random.seed()

    # Setup team 1
    self.team1Score = 0
    playerA_1 = []
    playerB_1 = []
    
    # Setup team 2
    self.team2Score = 0
    playerA_2 = []
    playerB_2 = []
    
    # Setup order
    self.turn_order = [playerA_1, playerA_2, playerB_1, playerB_2]
    start_at = random.randint(0,3)
    
    for i in range(start_at):
      self.advance(self.turn_order)
    
  def advance(self, arr):
    arr = arr[1:arr.__len__()] + [arr[0]]  

  def dealPhase(self):
    self.deck.shuffle()
    
    for player in self.turn_order:
      player.extend(self.deck.deal(5))
    
    kitty = self.deck.deal(1)
    print("Kitty: " + kitty[0].__str__())
    
  def playPhase(self):
    for player in self.turn_order:
      for card in player:
        print(card.__str__(), end=' ')
      print("")
    
  def play(self):
    while (self.team1Score < 10 and self.team2Score < 10):
      self.team1Score = 10
      self.dealPhase()
      self.playPhase()  


game = Euchre()
game.play()
