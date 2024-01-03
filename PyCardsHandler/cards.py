"""Card Handler"""
from typing import Optional, Any, Union


class Suit():
    Wildcard = 0
    Hearts = 1
    Diamonds = 2
    Clubs = 3
    Spades = 4

_suit_info = \
[
    "Wildcard",
    "Hearts",
    "Diamonds",
    "Clubs",
    "Spades"
]

class Rank():
    Joker = 0
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

_rank_info = \
[
    "Joker",
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Joker"
]


class Card():
    def __init__(self, rank: int, suit: int = 0, attributes: Optional[dict] = None):
        _validate_card(rank, suit)
        self._r: int = rank
        self._s: int = suit
        self._a: Optional[dict] = dict() if attributes is None else attributes

    def set_attributes(self, **attributes) -> None:
        self._a.update(attributes)

    def remove_attributes(self, *keys) -> None:
        if keys == ():
            self._a = None
        else:
            for key in keys:
                del self._a[key]    

    def card_name(self) -> str:
        return _get_card_name(self._r, self._s)
    
    def card_rank(self) -> str:
        return _rank_info[self._r]

    def card_suit(self) -> str:
        return _suit_info[self._s]

    def raw_card_rank(self) -> int:
        return self._r

    def raw_card_suit(self) -> int:
        return self._s
    
    def get_attributes(self, *keys) -> Union[Union[Any, list[Any]], dict]:
        if keys == ():
            return self._a
        else:
            attribs = list()
            for key in keys:
                attribs.append(self._a[key])
            return attribs[0] if len(attribs) == 1 else attribs
    
def _validate_card(rank: int, suit: int) -> bool:
    if not (suit >= 0 and suit <= 4):
        raise Exception(f"suit must be at least 0 and at max 4")
    if not(rank >= 0 and rank <= 13):
        raise Exception(f"rank must be at least 0 and at max 13")
    if (rank == 0 or suit == 0) and suit != rank:
        raise Exception(f"If suit or rank are zero both have to be zero")
    
def _get_card_name(rank: int, suit: int = 0) -> str:
    # _validate_card(rank, suit)
    if suit == 0 and rank == 0:
        return _rank_info[rank]
    else:
        return _rank_info[rank] + " of " + _suit_info[suit]
    
if __name__ == "__main__":
    from PyCardsHandler.logging import logs, log
    log(logs.log_fail, "This is a module, do not run directly")