from typing import List
from card import Card as Card
from deck import Deck as Deck

class Blackjack:
  # Creates a Blackjack game with a new Deck.
  def __init__(self):
    self.deck = Deck()
    self.discardPile = []
    self.currentHand = []
    self.handContainsHighAce = False
    

  # Computes the score of a hand. 
  # For examples of hands and scores as a number.
  # 2,5 -> 7
  # 3, 10 -> 13
  # 5, King -> 15
  # 10, Ace -> 21
  # 10, 8, 4 -> Bust so return -1
  # 9, Jack, Ace -> 20 
  # If the Hand is a bust return -1 (because it always loses)
  def _get_score(self, hand: List[Card]) -> int:
    score = int(0)
    cardValue = 0
    for card in hand:
      # if card is face card, value is 10
      if card.value() == "King" or card.value() == "Queen" or card.value() == "Jack":
        cardValue = 10
      elif card.value() == "Ace":
        # if score is 11 or over, use 1, else use 11
        if score > 11:
          cardValue = 1
        else:
          # if ace detected, flip boolean
          self.handContainsHighAce = True
          cardValue = 11
      else:
        help_dict = {
          'Two': '2',
          'Three': '3',
          'Four': '4',
          'Five': '5',
          'Six': '6',
          'Seven': '7',
          'Eight': '8',
          'Nine': '9',
          'Ten': '10'
        }
        cardValue = help_dict[card.value()]
      
      print("Adding -", cardValue, "- to Score:", score)
      score += int(cardValue)

      # compensate for ace
      # If bust, check boolean and compensate
      if self.handContainsHighAce & score > 21:
          score -= 10
          self.handContainsHighAce = False

      if score > 21:
        score = -1
        break

    return score

  
  # Prints the current hand and score.
  # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
  # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
  def _print_current_hand(self) -> None:
    for card in self.currentHand:
      print(card.__str__(), ", ")

    score = self._get_score(self.currentHand)

    if (score) == -1:
      print("Bust!")
      # if bust, empty hand to discard pile
      for card in self.currentHand:
        self.discardPile.insert(0, self.currentHand.pop())
    else:
      print(score)
    
  
  # The previous hand is discarded and shuffled back into the deck*.DISCARD PILE
  # Should remove the top 2 cards from the current deck and 
  # Set those 2 cards as the "current hand". 
  # It should also print the current hand and score of that hand.
  # If less than 2 cards are in the deck, 
  # then print an error instructing the client to shuffle the deck.
  def deal_new_hand(self) -> None:
    # if hand has cards, add to discard pile
    if len(self.currentHand) != 0:
      for card in self.currentHand:
        self.discardPile.insert(0, self.currentHand.pop())
    #draw two cards
    if self.deck.size() < 2:
      print("Error: Less than 2 cards in deck, shuffle deck")
    else:
      self.currentHand.insert(0, self.deck.draw())
      self.currentHand.insert(0, self.deck.draw())


  # Deals one more card to the current hand and prints the hand and score.
  # If no cards remain in the deck, print an error.
  def hit(self) -> None: 
    if len(self.currentHand) == 0:
      print("Cannot call 'hit' on an empty hand")
    elif self.deck.size() < 1:
      print("Error: Less than 1 card in deck, shuffle deck")
    else:
      self.currentHand.insert(0, self.deck.draw())
      self._print_current_hand()
       
  
  # Reshuffles all cards in the "current hand" and "discard pile"
  # and shuffles everything back into the Deck.
  def reshuffle(self) -> None:
    self.__init__()