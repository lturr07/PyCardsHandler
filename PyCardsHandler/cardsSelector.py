"""CardsSelector"""

if __name__ == "__main__":
    from logging import logs, log
    import sys
    log(logs.log_fail, "This is a module, do not run directly")
    sys.exit()

class Selector():
    def All():
        """select all cards"""
        return (0,)
    def Last():
        """select card at index -1"""
        return Selector.Index(-1)
    def First():
        """select card at index 0"""
        return Selector.Index(0)
    def Index(index: int):
        """select card at specific index"""
        return (0, index)
    def Range(start: int, end: int):
        """Range of cards including both endpoints"""
        return (0, start, end)
    def Rank(rank: int):
        """select cards with specific rank"""
        return (1, rank)
    def Suit(suit: int):
        """select cards with specific suit"""
        return (2, suit)
    def Attribute(has_key: str, has_value):
        """select cards with specific attribute"""
        return (3, {has_key: has_value})
    def Both(Selector1, Selector2):
        """will get cards that match both selectors"""
        return (4, [Selector1, Selector2])
    def Random(amount: int):
        """random but specified amount of cards"""
        return (5, amount)
    def Not(Selector):
        """will get cards that don't match the selector"""
        return (6, Selector)