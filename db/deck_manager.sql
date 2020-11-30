DROP TABLE IF EXISTS flashcards;
DROP TABLE IF EXISTS decks;

CREATE TABLE decks (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255),
    card_limit INT
);

CREATE TABLE flashcards (
    id SERIAL PRIMARY KEY,
    answer VARCHAR(255),
    question VARCHAR(255),
    deck_id INT REFERENCES decks (id)
);

