import random
import card

class Deck:
    
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
      self.cards = []
      SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
      VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
      for suit in SUITS:
        for value in VALUES:
          new_card = card.Card(suit, value)
          self.cards.insert(0, new_card)

      random.shuffle(self.cards)
      
    
    # Returns the number of Cards in the Deck
    def size(self) -> int:
      return len(self.cards)
    
    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self) -> None:
      random.shuffle(self.cards)
    
    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> card.Card:
      return self.cards[0]
    
    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> card.Card:
      if len(self.cards) > 0:
        return self.cards.pop(0)
      elif len(self.cards) == 0:
        return Exception("cannot draw, deck is empty")
  
    # Adds the input card to the deck. 
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: card.Card) -> None:
      if len(self.cards) < 52:
        print("Appending:", card.__str__())
        self.cards.insert(0, card)
      elif len(self.cards) >= 52:
        return Exception("cannot add_card, deck has 52 cards already")
    
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
      for card in self.cards:
        print(card)
      
    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
      self.__init__()