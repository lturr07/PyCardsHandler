from PyCardsHandler import *

# init deck
deck = Deck()

# init selectors
selector = CardSelector.Rank(Rank.Joker)

# get probability using combined selectors
prob = deck.probability(selector)  # will return 0. as there are no jokers in the deck

# print probability as percentage
print(f"Probability of getting Joker: {round(prob*100, 2)}%")