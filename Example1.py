from PyCardsHandler import *

# init deck
deck = Deck(jokers = 2)
# try adding more jokers and seeing what new percentages you get

# init selectors
selector = Selector.Rank(Rank.Joker)

# get probability using combined selectors
prob = deck.probability(selector)

# print probability as percentage
print(f"Probability of getting Joker: {round(prob*100, 2)}%")

