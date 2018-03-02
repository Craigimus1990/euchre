from enum import Enum
import random

class Card:
  def __init__(self, suit, pip):
    self.suit = suit
    self.pip = pip

  def __str__(self):
    return self.pip.name + self.suit.name


class Deck:
  suits = Enum('Suits', '♠ ♦ ♥ ♣')
  pips = Enum('Pips', '9 10 J Q K A')

  def __init__(self):
    self.cards = []
    self.deck = []
    random.seed()

    for suit in self.suits:
      for pip in self.pips:
        self.cards.append(Card(suit, pip))

    self.deck = self.cards

  def deal(self, count=1):
    if (count > self.deck.__len__()):
      raise "Not enough cards in the deck!"

    ret = self.deck[:count]
    self.deck = self.deck[count:]

    return ret
    
  #Fisher-Yates
  def shuffle(self):
    self.deck = self.cards
    n = self.deck.__len__()

    for i in range(n-1, 0, -1):
      j = random.randint(0,i)
      self.deck[j], self.deck[i] = self.deck[i], self.deck[j]

  def remaining(self):
    print(self.deck.__len__())
