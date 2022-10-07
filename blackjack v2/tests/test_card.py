"""
Test module for card.py
"""

import unittest
import card

class Testcard(unittest.TestCase):
    """
    Test the card functions for blackjack
    """
    
    # def __init__(self, suit: str, value: str):

    # def suit(self) -> str:
    def test_card_suit(self) -> None:
        testCard = card.Card("Spades", "Ace")
        assert testCard.suit() == "Spades"

    # def value(self) -> str:
    def test_card_value(self) -> None:
        testCard = card.Card("Spades", "Ace")
        assert testCard.value() == "Ace"

    # def __str__(self) -> str:
    def test_card_str(self) -> None:
        testCard = card.Card("Spades", "Ace")
        assert testCard.__str__() == "Ace of Spades"