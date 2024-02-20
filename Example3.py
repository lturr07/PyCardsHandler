from PyCardsHandler import *

hand = DeckEmpty()
pile = Deck(jokers=2)

is_hearts = Selector.Suit(Suit.Hearts)
not_hearts = Selector.Not(is_hearts)

is_ace = Selector.Rank(Rank.Ace)

is_ace_and_not_hearts = Selector.Both(is_ace, not_hearts)

cards = pile.get_cards(is_ace_and_not_hearts)
probability = pile.probability(is_ace_and_not_hearts)

print("Cards Found:\n* " + "\n* ".join([str(x) for x in cards]))
print(f"Probability of getting any of the above cards is {round(probability*100, 2)}%")
