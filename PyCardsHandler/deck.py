"""Deck Handler"""
from typing import Optional, Any, Union
from PyCardsHandler.cards import Card
from random import shuffle


def SelectRank(rank: int) -> tuple[int, int]:
    return (1, rank)
def SelectSuit(suit: int) -> tuple[int, int]:
    return (2, suit)
def SelectAttribute(has_key: str, has_value: Optional[str] = None) -> tuple[int, int]:
    return (3, {has_key: has_value})

class Deck():
    def __init__(self, ranks: int = 13, suits: int = 4, jokers: int = 0, def_attributes: Optional[dict] = None):
        self.cards: list[Card] = []
        for suit in range(1, suits+1):
            for rank in range(1, ranks+1):
                self.cards.append(
                    Card(rank, suit, def_attributes)
                )
        for _ in range(jokers):
            self.cards.append(Card(0, 0, def_attributes))

    def insert_card(self, card: Card, index = -1) -> None:
        self.cards.insert(index, card)
    
    def deal_card(self, index = -1) -> Card:
        return self.cards.pop(index)

    def shuffle_cards(self) -> None:
        shuffle(self.cards)

    def get_cards(self, cardSelector: tuple[int, Any], getIndex: bool = False) -> Union[list[Card], list[tuple[int, Card]]]:
        searchIn = list(enumerate(self.cards))
        if cardSelector[0] == 0:
            out = searchIn
        elif cardSelector[0] == 1:
            out = list(filter(lambda x: x[1].raw_card_rank() == cardSelector[1], searchIn))
        elif cardSelector[0] == 2:
            out = list(filter(lambda x: x[1].raw_card_suit() == cardSelector[1], searchIn))
        elif cardSelector[0] == 3:
            out = list(filter(lambda x: x[1].get_attributes(cardSelector[1][0])[0] == cardSelector[1][1], searchIn))
        else:
            raise Exception(f"Invalid Card Selector -> {repr(cardSelector)}")
        if getIndex:
            out = list(map(lambda x: x[0], out))
        else:
            out = list(map(lambda x: x[1], out))
        return out
    
    def get_all_cards(self) -> list[Card]:
        return self.cards
    
    def replace_card(self, card: Card, index = -1) -> None:
        self.cards[index] = card
        

if __name__ == "__main__":
    from PyCardsHandler.logging import logs, log
    log(logs.log_fail, "This is a module, do not run directly")