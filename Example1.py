from PyCardsHandler import *

# init deck
deck = Deck()

# init selectors
ace_selector = CardSelector.Rank(Rank.Ace)
hearts_selector = CardSelector.Suit(Suit.Hearts)

# combine selectors
selector = CardSelector.Both(ace_selector, hearts_selector)

# get probability using combined selectors
prob = deck.probability(selector)

# print probability as percentage
print(f"Probability of getting Ace of Hearts: {round(prob*100, 2)}%")