import pdb

from models.deck import Deck
from models.flashcard import Flashcard

import repositories.deck_repository as deck_repository
import repositories.flashcard_repository as flashcard_repository

flashcard_repository.delete_all()
deck_repository.delete_all()


deck_1 = Deck("Capitals", 8)
deck_repository.save(deck_1)

card_1 = Flashcard("Paris", "What is the capital of France?", deck_1)
flashcard_repository.save(card_1)
card_2 = Flashcard("Rome", "what is the capital of Italy?", deck_1)
flashcard_repository.save(card_2)
card_3 = Flashcard("London", "What is the capital of England?", deck_1)
flashcard_repository.save(card_3)
card_4 = Flashcard("Athens", "what is the capital of Greece?", deck_1)
flashcard_repository.save(card_4)
card_5 = Flashcard("Dublin", "What is the capital of Ireland?", deck_1)
flashcard_repository.save(card_5)
card_6 = Flashcard("Berlin", "what is the capital of Germany?", deck_1)
flashcard_repository.save(card_6)
card_7 = Flashcard("Cairo", "What is the capital of Egypt?", deck_1)
flashcard_repository.save(card_7)
card_8 = Flashcard("Marakesh", "what is the capital of Moroco?", deck_1)
flashcard_repository.save(card_8)


pdb.set_trace()