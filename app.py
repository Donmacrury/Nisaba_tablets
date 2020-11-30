from flask import Flask, render_template

from controllers.flashcard_controller import flashcards_blueprint
from controllers.deck_controller import decks_blueprint

app = Flask(__name__)

app.register_blueprint(flashcards_blueprint)
app.register_blueprint(decks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

