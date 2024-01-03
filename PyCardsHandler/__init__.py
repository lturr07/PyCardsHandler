"""PyCardsHandler"""

if __name__ == "__main__":
    from PyCardsHandler.logging import logs, log
    log(logs.log_fail, "This is a module, do not run directly")
else:
    from PyCardsHandler.deck import *
    from PyCardsHandler.cards import Card, Rank, Suit