import unittest
from models.deck import Deck
from models.flashcard import Flashcard

class TestFlashcard(unittest.TestCase):

    def setUp(self):
        self.flashcard = Flashcard("Paris", "What is the capital of France")

    def test_Flashcard_has_answer(self):
        self.assertEqual("Paris", self.flashcard.answer)

    def test_Flashcard_has_card_question(self):
        self.assertEqual("What is the capital of France", self.flashcard.question)