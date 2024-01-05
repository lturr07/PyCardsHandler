"""Deck Handler"""

if __name__ == "__main__":
    from logging import logs, log
    import sys
    log(logs.log_fail, "This is a module, do not run directly")
    sys.exit()

from typing import Optional, Any, Union
from PyCardsHandler.cards import Card
from random import shuffle, randint

class CardSelector():
    All = (0,)
    Index = lambda index: (0, index)
    Rank = lambda rank: (1, rank)
    Suit = lambda suit: (2, suit)
    Attribute = lambda has_key, has_value: (3, {has_key: has_value})
    Both = lambda a, b: (4, [a, b])
    Random = lambda amount: (5, amount)

class Deck():
    def __init__(self, ranks: int = 13, suits: int = 4, jokers: int = 0, def_attributes: Optional[dict] = None):
        self._c: list[Card] = []
        for suit in range(1, suits+1):
            for rank in range(1, ranks+1):
                self._c.append(
                    Card(rank, suit, def_attributes)
                )
        for _ in range(jokers):
            self._c.append(Card(0, 0, def_attributes))

    def insert_card(self, card: Card, index = -1) -> None:
        self._c.insert(index, card)
    
    def deal_cards(self, selector: CardSelector) -> Union[list[Card],Card]:
        return self.get_cards(selector, True)
    
    def probability(self, selector: CardSelector) -> float:
        return len(self._get_cards(selector)) / len(self._c)

    def shuffle_cards(self) -> None:
        shuffle(self._c)

    def _get_cards(self, selector: CardSelector, removeFromDeck: bool = False) -> Union[list[Card], Card]:
        # searchIn = list(enumerate(self.cards))
        searchIn = self._c.copy()
        if selector[0] == 0:
            if len(selector) == 1:
                out = searchIn
            else:
                out = searchIn[selector[1]]
        elif selector[0] == 1:
            out = list(filter(lambda x: x.raw_card_rank() == selector[1], searchIn))
        elif selector[0] == 2:
            out = list(filter(lambda x: x.raw_card_suit() == selector[1], searchIn))
        elif selector[0] == 3:
            out = list(filter(lambda x: x.get_attributes(selector[1][0])[0] == selector[1][1], searchIn))
        elif selector[0] == 4:
            out = list(self._get_cards(selector[1][0]))
            out.extend(list(self._get_cards(selector[1][1])))
            for i in list(set(out)):
                del out[out.index(i)]  # del non duplicates
        elif selector[0] == 5:
            out = []
            for i in range(selector[1]):
                out.append(searchIn.pop(randint(0, len(searchIn) - 1)))
        else:
            raise Exception(f"Invalid Card Selector -> {repr(selector)}")
        if removeFromDeck:
            for x in range(out):
                del self._c[self._c.index(x)]
        # out = list(map(lambda x: x[0], out))
        # out = list(map(lambda x: x[1], out))
        return out
    
    def get_all_cards(self) -> list[Card]:
        return self._c
    
    def replace_card(self, card: Card, index = -1) -> None:
        self._c[index] = card