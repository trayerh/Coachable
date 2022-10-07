"""
Test module for blackjack.py
"""

import unittest
import deck
import card
import blackjack

class Testblackjack(unittest.TestCase):
    """
    Test the blackjack functions for blackjack
    """
   
    # Creates a Blackjack game with a new Deck.
    # def __init__(self):

    # def _get_score(self, hand: List[Card]) -> int:
    def test_bj_score(self) -> None:
        testGame = blackjack.Blackjack()
        testFirstCard = card.Card("Clubs", "Two")
        testSecondCard = card.Card("Spades", "Nine")
        testGame.currentHand.insert(0, testFirstCard)
        testGame.currentHand.insert(0, testSecondCard)
        assert testGame._get_score(testGame.currentHand) == 11
    # test Ace
    # test bust

    # def _print_current_hand(self) -> None:

    # def deal_new_hand(self) -> None:
    def test_bj_deal_hand(self) -> None:
        testGame = blackjack.Blackjack()
        testGame.deal_new_hand()
        deckSize = testGame.deck.size()
        discardSize = len(testGame.discardPile)
        handSize = len(testGame.currentHand)
        print("Cards in...")
        print("Deck: ", deckSize, " Hand: ", handSize, " Discard Pile: ", discardSize)
        assert ((deckSize == 50) & (handSize == 2))


    # def hit(self) -> None: 
    def test_bj_hit(self) -> None:
        testGame = blackjack.Blackjack()
        testGame.deal_new_hand()
        testGame.hit()
        deckSize = testGame.deck.size()
        discardSize = len(testGame.discardPile)
        handSize = len(testGame.currentHand)
        print("Cards in...")
        print("Deck: ", deckSize, " Hand: ", handSize, " Discard Pile: ", discardSize)
        assert ((deckSize == 49) & ((handSize + discardSize) == 3))


    # def reshuffle(self) -> None:
    def test_bj_reshuffle(self) -> None:
        testGame = blackjack.Blackjack()
        testGame.deal_new_hand()
        testGame.hit()
        deckSizePreShuffle = testGame.deck.size()
        testGame.reshuffle()
        deckSizePostShuffle = testGame.deck.size()

        assert deckSizePreShuffle != deckSizePostShuffle
