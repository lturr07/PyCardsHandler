"""Deck Handler"""

if __name__ == "__main__":
    from logging import logs, log
    import sys
    log(logs.log_fail, "This is a module, do not run directly")
    sys.exit()

from typing import Optional, Union
from PyCardsHandler.cards import Card, _rank_info, _suit_info
from PyCardsHandler.cardsSelector import Selector
from random import shuffle, sample

class Deck():
    def __init__(self, ranks: int = 13, suits: int = 4, jokers: int = 0, def_attributes: Optional[dict] = None, start_shuffled: bool = False):
        self._c: list[Card] = []
        for suit in range(1, suits+1):
            for rank in range(1, ranks+1):
                self._c.append(
                    Card(rank, suit, def_attributes)
                )
        for _ in range(jokers):
            self._c.append(Card(0, 0, def_attributes))
        if start_shuffled:
            self.shuffle_cards()

    def add_cards(self, cards: Union[Card, list[Card]]) -> None:
        if isinstance(cards, list):
            for card in cards:
                self._c.append(card)
        else:
            self._c.append(cards)

    def insert_cards(self, index: int, cards: Union[Card, list[Card]]) -> None:
        if isinstance(cards, list):
            for card in cards:
                self._c.insert(index, card)
        else:
            self._c.insert(index, cards)
    
    def deal_cards(self, selector: Selector) -> list[Card]:
        return self._get_cards(selector, True)
    
    def probability(self, selector: Selector) -> float:
        return len(self._get_cards(selector)) / len(self._c)

    def shuffle_cards(self) -> None:
        shuffle(self._c)

    def _get_cards(self, selector: Selector, removeFromDeck: bool = False) -> list[Card]:
        searchIn = self._c.copy()
        if selector[0] == 0:
            if len(selector) == 1:
                out = searchIn
            elif len(selector) == 2:
                out = searchIn[selector[1]]
            elif len(selector) == 3:
                out = searchIn[selector[1]:selector[2]]
                out.append(searchIn[selector[2]])
            else:
                raise Exception(f"Invalid Card Selector -> {repr(selector)}")
        elif selector[0] == 1:
            out = list(filter(lambda x: x.raw_card_rank == selector[1], searchIn))
        elif selector[0] == 2:
            out = list(filter(lambda x: x.raw_card_suit == selector[1], searchIn))
        elif selector[0] == 3:
            out = list(filter(lambda x: x.get_attributes(selector[1][0])[0] == selector[1][1], searchIn))
        elif selector[0] == 4:
            out = list(self._get_cards(selector[1][0]))
            out.extend(list(self._get_cards(selector[1][1])))
            for i in list(set(out)):
                del out[out.index(i)]  # del non duplicates
        elif selector[0] == 5:
            out = sample(searchIn, selector[1])
        elif selector[0] == 6:
            out = self.get_cards(selector[1], True)
            for i in out:
                del searchIn[i]
            out = searchIn
        elif selector[0] == 7:
            out = list(filter(lambda x: id(x) == selector[1], searchIn))
        else:
            raise Exception(f"Invalid Card Selector -> {repr(selector)}")
        if removeFromDeck:
            if isinstance(out, list):
                for x in out:
                    del self._c[self._c.index(x)]
            else:
                del self._c[self._c.index(out)]
        return out if isinstance(out, list) else [out]
    
    def __str__(self) -> str:
        return "\n".join([str(card) for card in self._c])
    
    def __len__(self) -> int:
        return self.card_amount
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Deck):
            temp1 = self._c.copy()
            temp2 = __value._c.copy()
            temp1.sort_cards()
            temp2.sort_cards()
            return str(temp1) == str(temp2)

    def sort_cards(self, suitSortAsc: bool = True, rankSortAsc: bool = True, groupBySuit: bool = True, jokersAtEnd: bool = True) -> None:
        """"""
        # sort_alg returns another function
        sort_alg = lambda sortAsc, _info, y: lambda x: x-y if sortAsc else (len(_info) - 1) - x

        # s_sort and r_sort 'invert' value if the corresponding -SortAsc bool is False
        # unless value is 0 meaning wildcard suit or joker rank, which it instead pushes to high sort value
        s_sort = sort_alg(suitSortAsc, _suit_info, 0)
        r_sort = sort_alg(rankSortAsc, _rank_info, 0)

        # remove jokers as they have suit and rank value of 0
        jokers = self.deal_cards((2,0))
        
        if groupBySuit:
            # sorts the calculated values by suit
            group_suit_sort = lambda x: ((s_sort(x._s) - 1) * (len(_rank_info) - 1)) + r_sort(x._r)
            self._c.sort(key=group_suit_sort)
            # debug
            # print("\n".join(list(map(lambda x: f"{x} -> (({s_sort(x._s)} - 1) * ({len(_rank_info)} - 1)) + {r_sort(x._r)} = {group_suit_sort(x)}", self._c))))
        else:
            # sorts the calculated values by rank
            group_rank_sort = lambda x: ((r_sort(x._r) - 1) * (len(_suit_info) - 1)) + s_sort(x._s)
            self._c.sort(key=group_rank_sort)
            # debug
            # print("\n".join(list(map(lambda x: f"{x} -> (({r_sort(x._r)} - 1) * ({len(_suit_info)} - 1)) + {s_sort(x._s)} = {group_rank_sort(x)}", self._c))))
        
        
        # add back jokers
        if jokersAtEnd:
            self.add_cards(jokers)
        else:
            self.insert_cards(0, jokers)

    def clear(self) -> list[Card]:
        temp = self._c
        self._c = []
        return temp

    @property
    def all_cards(self) -> list[Card]:
        return self._c
    
    @property
    def card_amount(self) -> int:
        return len(self._c)
    
    def get_cards(self, selector: Selector, getIndex: bool = False) -> list[Card]:
        x = self._get_cards(selector)
        if getIndex:
            x = list(map(lambda y: self._c.index(y) ,x))
        return x

    def replace_cards(self, cards: list[Card], selector: Selector) -> None:
        if isinstance(cards, list):
            rep = zip(self.get_cards(selector, True), cards)
        else:
            rep = zip(self.get_cards(selector, True), [cards])
        for i in rep:
            self._c[i[0]] = i[1]

def DeckEmpty() -> Deck:
    return Deck(0, 0)