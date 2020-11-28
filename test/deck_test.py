import unittest
from models.deck import Deck
from models.flashcard import Flashcard

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck("Capitals", 15)

    def test_Deck_has_topic(self):
        self.assertEqual("Capitals", self.deck.topic)

    def test_Deck_has_card_limit(self):