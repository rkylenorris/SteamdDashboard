CREATE TABLE about_games (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    steam_game_id INTEGER NOT NULL,
    game_name TEXT NOT NULL,
    release_date DATE,
    about_the_game TEXT,
    description TEXT,
    website TEXT
);

CREATE TABLE game_rating (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    game_id INTEGER,
    positive_ratings INTEGER,
    negative_ratings INTEGER,
    metacritic_score REAL,
    metacritic_url TEXT,
    FOREIGN KEY (game_id) REFERENCES about_games(id)
);

CREATE TABLE game_support (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    game_id INTEGER,
    supports_windows BOOLEAN,
    supports_mac BOOLEAN,
    support_linux BOOLEAN,
    FOREIGN KEY (game_id) REFERENCES about_games(id)
);

CREATE TABLE game_misc (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    game_id INTEGER,
    recommendations INTEGER,
    achievements INTEGER,
    median_playtime INTEGER,
    average_playtime INTEGER,
    peak_player_count INTEGER,
    estimated_owners TEXT,
    FOREIGN KEY (game_id) REFERENCES about_games(id)
);

CREATE TABLE developers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    developer TEXT
);

CREATE TABLE dev_game_junction (
    game_id INTEGER,
    dev_id INTEGER,
    PRIMARY KEY (game_id, dev_id),
    FOREIGN KEY (game_id) REFERENCES about_games(id),
    FOREIGN KEY (dev_id) REFERENCES developers(id)
);

CREATE TABLE publishers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    publisher TEXT
);

CREATE TABLE pub_game_junction (
    game_id INTEGER,
    publisher_id INTEGER,
    PRIMARY KEY (game_id, publisher_id),
    FOREIGN KEY (game_id) REFERENCES about_games(id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    genre TEXT
);

CREATE TABLE genre_game_junction (
    game_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (game_id, genre_id),
    FOREIGN KEY (game_id) REFERENCES about_games(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tag TEXT
);

CREATE TABLE tag_game_junction (
    game_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (game_id, tag_id),
    FOREIGN KEY (game_id) REFERENCES about_games(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    category TEXT
);

CREATE TABLE category_game_junction (
    game_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (game_id, category_id),
    FOREIGN KEY (game_id) REFERENCES about_games(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE screenshots (
    game_id INTEGER,
    screenshot_url TEXT,
    PRIMARY KEY (game_id, screenshot_url),
    FOREIGN KEY (game_id) REFERENCES about_games(id)
);

CREATE TABLE trailers (
    game_id INTEGER,
    trailer_url TEXT,
    PRIMARY KEY (game_id, trailer_url),
    FOREIGN KEY (game_id) REFERENCES about_games(id)
);
