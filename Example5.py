from PyCardsHandler import *

hand_amnt = 4
hands = [DeckEmpty() for _ in range(hand_amnt)]
deck = Deck(start_shuffled=True)
cards_selector = Selector.Range(0,6)

for y, hand in enumerate(hands):
    print(f"\nHand {y+1}")
    hand.add_cards(deck.deal_cards(cards_selector))
    for x, card in enumerate(hand.all_cards):
        print(x+1, "-", card)