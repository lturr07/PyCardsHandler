"""PyCardsHandler"""

if __name__ == "__main__":
    from PyCardsHandler.logging import logs, log
    log(logs.log_fail, "This is a module, do not run directly")
else:
    from PyCardsHandler.const.cards import *
    from PyCardsHandler.handler.deck import *
