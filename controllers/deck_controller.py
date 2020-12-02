from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.deck import Deck
import repositories.deck_repository as deck_repository
import repositories.flashcard_repository as flashcard_repository

decks_blueprint = Blueprint("decks", __name__)

@decks_blueprint.route("/decks")
def decks():
    decks = deck_repository.select_all()
    return render_template("decks/index.html", all_decks = decks)

@decks_blueprint.route("/decks/new", methods=['GET'])
def new_deck():
    flashcards = flashcard_repository.select_all()
    return render_template("decks/new.html", all_flashcards = flashcards)

@decks_blueprint.route("/decks", methods=['POST'])
def create_decks():
    topic = request.form['topic']
    card_limit = request.form['card_limit']
    deck = Deck(topic, card_limit)
    deck_repository.save(deck)
    return redirect('/decks')

@decks_blueprint.route("/decks/<id>", methods=['GET'])
def show_deck(id):
    deck = deck_repository.select(id)
    return render_template('decks/show.html', deck = deck)

@decks_blueprint.route("/decks/<id>/edit", methods=['GET'])
def edit_deck(id):
    deck = deck_repository.select(id)
    return render_template('decks/edit.html', deck = deck)

@decks_blueprint.route("/decks/<id>", methods=['POST'])
def update_deck(id):
    topic = request.form['topic']
    card_limit = request.form['card_limit']
    deck = Deck(topic, card_limit, id)
    deck_repository.update(deck)
    return redirect('/decks')

@decks_blueprint.route("/decks/<id>/delete", methods=['POST'])
def delete_deck(id):
    deck_repository.delete(id)
    return redirect('/decks')

@decks_blueprint.route("/decks/<id>/play", methods=['GET'])
def play_deck(id):
    deck = deck_repository.select(id)
    flashcards = flashcard_repository.select_all()
    return render_template('decks/play.html', deck = deck, flashcards = flashcards)