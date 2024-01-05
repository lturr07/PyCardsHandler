"""PyCardsHandler"""

if __name__ == "__main__":
    from logging import logs, log
    log(logs.log_fail, "This is a module, do not run directly")
else:
    from PyCardsHandler.deck import Deck, CardSelector
    from PyCardsHandler.cards import Card, Rank, Suit