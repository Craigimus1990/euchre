from deck import Deck, Card

d = Deck()

d.remaining()
d.deal(10)
d.remaining()
d.shuffle()
d.remaining()

hand = d.deal(5)
for card in hand:
  print(card.__str__())
