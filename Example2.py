from PyCardsHandler import *

# init deck
deck = Deck()

# init selectors
ace_selector = Selector.Rank(Rank.Ace)
hearts_selector = Selector.Suit(Suit.Hearts)

# combine selectors
selector = Selector.Both(ace_selector, hearts_selector)

# get probability using combined selectors
prob = deck.probability(selector)

# print probability as percentage
print(f"Probability of getting Ace of Hearts: {round(prob*100, 2)}%")