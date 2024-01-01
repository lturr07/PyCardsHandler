"""Card Constants"""

class Suit():
    Hearts = 1
    Diamonds = 2
    Clubs = 3
    Spades = 4

_suit_info = \
[
    "Hearts",
    "Diamonds",
    "Clubs",
    "Spades"
]

class Rank():
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
    Joker = 14

_rank_info = \
[
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

def get_card_name(rank: int, suit: int = 0) -> str:
    if not (suit >= 0 and suit <= len(_suit_info)):
        raise Exception(f"suit must be at least 0 and at max {len(_suit_info)}")
    if not(rank >= 1 and rank <= len(_rank_info)):
        raise Exception(f"rank must be at least 1 and at max {len(_rank_info)}")
    if suit == 0 or rank == 14:
        return _rank_info[rank-1]
    else:
        return _rank_info[rank-1] + " of " + _suit_info[suit-1]