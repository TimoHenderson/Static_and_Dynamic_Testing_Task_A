import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace_of_spades = Card("Spades", 1)
        self.five_of_clubs = Card("Clubs", 5)
        self.cg = CardGame()

    def test_check_for_ace__true(self):
        actual = self.cg.check_for_ace(self.ace_of_spades)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_for_ace__false(self):
        actual = self.cg.check_for_ace(self.five_of_clubs)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_ace__card1_higher(self):
        actual = self.cg.highest_card(self.five_of_clubs, self.ace_of_spades)
        expected = self.five_of_clubs
        self.assertEqual(actual, expected)

    def test_check_for_ace__card2_higher(self):
        actual = self.cg.highest_card(self.ace_of_spades, self.five_of_clubs)
        expected = self.five_of_clubs
        self.assertEqual(actual, expected)

    def test_cards_total(self):
        cards = [self.ace_of_spades, self.five_of_clubs]
        actual = self.cg.cards_total(cards)
        expected = "You have a total of 6"
        self.assertEqual(actual, expected)
