"""PyCardsHandler"""

if __name__ == "__main__":
    from logging import logs, log
    log(logs.log_fail, "This is a module, do not run directly")
else:
    from PyCardsHandler.deck import Deck, DeckEmpty
    from PyCardsHandler.cards import Card, Rank, Suit
    from PyCardsHandler.cardsSelector import Selector