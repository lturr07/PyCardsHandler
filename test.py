# import PyCardsHandler
from PyCardsHandler.cards import *
from PyCardsHandler.deck import *

deck = Deck(jokers=2)
selector = SelectRank(Rank.Ace)
aces = deck.get_cards(selector)
aces_index = deck.get_cards(selector, True)
Attrib = {"Attribute1":"I'm An Ace!"}
for ace in zip(aces, aces_index):
    print(f"{ace[0].card_name()} | At Pos: {ace[1]} | Before Adding Custom Attribute: {ace[0].get_attributes()}")
    ace[0].set_attributes(**Attrib)
    deck.replace_card(ace[0], ace[1])
aces = deck.get_cards(selector)
aces_index = deck.get_cards(selector, True)
for ace in zip(aces, aces_index):
    print(f"{ace[0].card_name()} | At Pos: {ace[1]} | After Adding Custom Attribute: {ace[0].get_attributes()}")