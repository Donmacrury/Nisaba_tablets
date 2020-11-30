from db.run_sql import run_sql
from models.flashcard import Flashcard
from models.deck import Deck
import repositories.deck_repository as deck_repository

def save(flashcard):
    sql = "INSERT INTO flashcards (answer, question, deck_id) VALUES (%s, %s, %s) RETURNING *"
    values = [flashcard.answer, flashcard.question, flashcard.deck.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    flashcard.id = id
    return flashcard

def select_all():
    flashcards = []

    sql = "SELECT * FROM flashcards"
    results = run_sql(sql)

    for row in results:
        deck = deck_repository.select(row['deck_id'])
        flashcard = Flashcard(row['answer'], row['question'], deck, row['id'])
        flashcards.append(flashcard)
    return flashcards

def select(id):
    flashcard = None
    sql = "SELECT * FROM flashcards WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        deck = deck_repository.select(result['deck_id'])
        flashcard = Flashcard(result['answer'], result['question'], deck, result['id'])
    return flashcard

def delete_all():
    sql = "DELETE FROM flashcards"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM flashcards WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(flashcard):
    sql = "UPDATE flashcards SET (answer, question, deck_id) = (%s, %s, %s) WHERE id = %s"
    values = [flashcard.answer, flashcard.question, flashcard.deck.id, flashcard.id]
    run_sql(sql, values)