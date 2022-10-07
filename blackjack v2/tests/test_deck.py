"""
Test module for deck.py
"""

import unittest
import deck
import card

class Testdeck(unittest.TestCase):
    """
    Test the deck functions for blackjack
    """
   
    # def shuffle(self) -> None:
    def test_deck_shuffle(self) -> None:
        testDeck = deck.Deck()
        preShuffleTop = testDeck.peek().__str__()
        testDeck.shuffle()
        postShuffleTop = testDeck.peek().__str__()
        # print("pre:", preShuffleTop)
        # print("post: ", postShuffleTop)
        assert preShuffleTop != postShuffleTop
    
    # def peek(self) -> card.Card:
 
    # def draw(self) -> card.Card:
    def test_deck_draw(self) -> None:
        testDeck = deck.Deck()
        drawnCard = testDeck.draw()
        # if card drawn not present in deck
        # for loop all cards in deck
        status = True
        for card in testDeck.cards:
            if card.__str__() == drawnCard.__str__():
                status = False
        # if match found, testSTatus fail
        # testStatus assert
        assert status
   
    # def add_card(self, card: card.Card) -> None:
    def test_deck_add_card(self) -> None:
        testDeck = deck.Deck()
        testDeck.draw() # remove a card to make space
        testDeck.draw() # remove a card to make space
        testCard = card.Card("Spades", "Ace")
        testDeck.add_card(testCard)
    #     testDeck.print_deck()
        topCardName = testDeck.peek().__str__()
    #     print("\nTest Card: ", testCard.__str__())
    #     print("Top Card: ", topCardName)
        assert testCard.__str__() == topCardName
        
  
    # def print_deck(self) -> None:
  
    # def reset(self) -> None: