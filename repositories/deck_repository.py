from db.run_sql import run_sql
from models.deck import Deck
from models.flashcard import Flashcard


def save(deck):
    sql = "INSERT INTO decks (topic, card_limit) VALUES (%s, %s) RETURNING *"
    values = [deck.topic, deck.card_limit]
    results = run_sql(sql, values)
    id = results[0]['id']
    deck.id = id
    return deck

def select_all():
    decks = []

    sql = "SELECT * FROM decks"
    results = run_sql(sql)

    for row in results:
        deck = Deck(row['topic'], row['card_limit'], row['id'])
        decks.append(deck)
    return decks

def select(id):
    deck = None
    sql = "SELECT * FROM decks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        deck = Deck(result['topic'], result['card_limit'], result['id'] )
    return deck

def delete_all():
    sql = "DELETE FROM decks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM decks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(deck):
    sql = "UPDATE decks SET (topic, card_limit) = (%s, %s) WHERE id = %s"
    values = [deck.topic, deck.card_limit, deck.id]
    run_sql(sql, values)

def flashcard(deck):
    flashcards = []

    sql = "SELECT * FROM flashcards WHERE deck_id = %s"
    values = [deck.id]
    results = run_sql(sql, values)

    for row in results:
        flashcard = Flashcard(row['asnwer'], row['question'], row['deck_id'], row['id'])
        flashcards.append(flashcard)
    return flashcards