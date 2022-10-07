class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit: str, value: str):
        self.card = {"suit": suit, "value": value}
    
    # Returns the suit of the card.
    def suit(self) -> str:
        return self.card["suit"]
    
    # Returns the value of the card.
    def value(self) -> str:
        return self.card["value"]
      
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self) -> str:
        card_name = self.value() + " of " + self.suit()
        return card_name