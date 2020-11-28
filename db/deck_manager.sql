DROP TABLE IF EXISTS decks;
DROP TABLE IF EXISTS flashcards;


CREATE TABLE flashcards (
    id SERIAL PRIMARY KEY,
    answer VARCHAR(255),
    question VARCHAR(255)
);

CREATE TABLE decks (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255),
    card_limit INT,
    card_id SERIAL REFERENCES flashcards(id)
);