from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.flashcard import Flashcard
import repositories.deck_repository as deck_repository
import repositories.flashcard_repository as flashcard_repository

flashcards_blueprint = Blueprint("flashcards", __name__)

@flashcards_blueprint.route("/flashcards")
def flashcards():
    flashcards = flashcard_repository.select_all()
    return render_template("flashcards/index.html", all_flashcards = flashcards)

@flashcards_blueprint.route("/flashcards/new", methods=['GET'])
def new_flashcard():
    decks = deck_repository.select_all()
    return render_template("flashcards/new.html", all_decks = decks)

@flashcards_blueprint.route("/flashcards", methods=['POST'])
def create_flashcard():
    answer = request.form['answer']
    question = request.form['question']
    deck = deck_repository.select(request.form['deck_id'])
    flashcard = Flashcard(answer, question, deck)
    flashcard_repository.save(flashcard)
    return redirect('/flashcards')

@flashcards_blueprint.route("/flashcards/<id>", methods=['GET'])
def show_flashcard(id):
    flashcard = flashcard_repository.select(id)
    return render_template('flashcards/show.html', flashcard = flashcard)

@flashcards_blueprint.route("/flashcards/<id>/edit", methods=['GET'])
def edit_flashcard(id):
    flashcard = flashcard_repository.select(id)
    decks = deck_repository.select_all()
    return render_template('flashcards/edit.html', flashcard = flashcard, all_decks = decks)

@flashcards_blueprint.route("/flashcards/<id>", methods=['POST'])
def update_flashcard(id):
    answer = request.form['answer']
    question = request.form['question']
    deck = deck_repository.select(request.form['deck_id'])
    flashcard = Flashcard(answer, question, deck, id)
    flashcard_repository.update(flashcard)
    return redirect('/flashcards')

@flashcards_blueprint.route("/flashcards/<id>/delete", methods=['POST'])
def delete_flashcard(id):
    flashcard_repository.delete(id)
    return redirect('/flashcards')

@flashcards_blueprint.route("/flashcards/<id>/answer", methods=['POST'])
def show_answer(id):
    flashcard = flashcard_repository.select(id)
    return render_template('flashcards/answer.html', flashcard = flashcard)