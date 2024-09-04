from PyCardsHandler import *

deck = DeckEmpty()

joker1 = Card(Rank.Joker, Suit.Wildcard, {"name":"I'm Joker 1"})
joker1_selector = joker1.card_selector

joker2 = Card(Rank.Joker, Suit.Wildcard, {"name":"I'm Joker 2"})
joker2_selector = joker2.card_selector

all_jokers_selector = Selector.Rank(Rank.Joker)

# add both jokers to the deck
deck.add_cards([joker1, joker2])

found_joker1 = deck.get_cards(joker1_selector)
found_joker2 = deck.get_cards(joker2_selector)
found_all_jokers = deck.get_cards(all_jokers_selector)

def format_cards(cards: list[Card]) -> str:
    return [x.get_attributes("name") for x in cards]

print("\njoker1_selector found card with attribute: ", format_cards(found_joker1))
print("joker2_selector found card with attribute: ", format_cards(found_joker2))
print("all_jokers_selector found cards with attributes: ", format_cards(found_all_jokers), "\n")
