from deck import Deck, Card
import random

class EuchrePlayer:

  def __init__(self, team):
    self.team = team

  def dealHand(self, hand):
    self.hand = hand

  def playCard(self, pot, trump, handScores, teamScores):
    return self.hand.pop(0)

  def pickKitty(self, kitty):
    return True

  def pickTrump(self, invalid, forced=False):
    return self.hand[0].suit

  def exchangeCard(self, card):
    ret, self.hand[0] = self.hand[0], card
    return ret

class Euchre:

  def __init__(self, player1, player2, player3, player4):
    ## Setup game
    self.deck = Deck()
    random.seed()

    # Setup team 1
    self.team1Score = 0
    self.playerA_1 = player1
    self.playerB_1 = player2
    
    # Setup team 2
    self.team2Score = 0
    self.playerA_2 = player3
    self.playerB_2 = player4
    
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
      (self.deck.deal(5))
    
    kitty = self.deck.deal(1)[0]
    picking = False
    print("Kitty: " + kitty.__str__())

    for player in self.turn_order:
      picking = player.pickKitty(kitty)

      if (picking):
        break

    
    if (picking):
      exchange_check = self.turn_order[-1].exchangeCard(kitty)
      if (exchange_check == kitty):
        self.add_score(self.turn_order[0], 2)
        return -1
      return kitty.suit

    for player in self.turn_order:
      forced = (player == self.turn_order[-1])
      suit = player.pickTrump(kitty.suit, forced)
      if (suit == kitty.suit or (suit is None and forced == True)):
        renegedPlayer = self.turn_order.index(player)
        self.add_score(self.turn_order[(renegedPlayer + 1) % 4], 2)
        return -1
      
      if (suit is not None):
        return suit
      

  def playPhase(self, trump):
    for player in self.turn_order:
      for card in player:
        print(card.__str__(), end=' ')
      print("")
    
  def play(self):
    while (self.team1Score < 10 and self.team2Score < 10):
      self.team1Score = 10
      suit = self.dealPhase()
      if (suit == -1):
        continue

      self.playPhase(trump=suit)  


game = Euchre()
game.play()
