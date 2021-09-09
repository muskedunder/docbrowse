CREATE TABLE document (
    id bytea PRIMARY KEY,
    day date NOT NULL,
    author text NOT NULL,
    body text NOT NULL
)
