CREATE TABLE about_games (
    steam_game_id INTEGER PRIMARY KEY NOT NULL,
    game_name TEXT NOT NULL,
    required_age INTEGER,
    release_date DATE,
    about_the_game TEXT,
    description TEXT,
    website TEXT,
    price float,
    header_image text
);

CREATE TABLE game_rating (
    steam_game_id INTEGER PRIMARY KEY NOT NULL,
    positive_ratings INTEGER,
    negative_ratings INTEGER,
    metacritic_score REAL,
    metacritic_url TEXT,
    recommendations INTEGER,
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id)
);

CREATE TABLE game_support (
    steam_game_id INTEGER PRIMARY KEY NOT NULL,
    supports_windows BOOLEAN,
    supports_mac BOOLEAN,
    supports_linux BOOLEAN,
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id)
);

CREATE TABLE game_misc (
    steam_game_id INTEGER PRIMARY KEY NOT NULL,
    recommendations INTEGER,
    median_playtime INTEGER,
    average_playtime INTEGER,
    peak_player_count INTEGER,
    estimated_owners_range TEXT,
    estimated_owners_low INTEGER,
    estimated_owners_high INTEGER,
    achievements INTEGER,
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id)
);

CREATE TABLE developers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    developer TEXT
);

CREATE TABLE game_developers (
    steam_game_id INTEGER,
    dev_id INTEGER,
    PRIMARY KEY (steam_game_id, dev_id),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id),
    FOREIGN KEY (dev_id) REFERENCES developers(id)
);

CREATE TABLE publishers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    publisher TEXT
);

CREATE TABLE game_publishers (
    steam_game_id INTEGER,
    publisher_id INTEGER,
    PRIMARY KEY (steam_game_id, publisher_id),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    genre TEXT
);

CREATE TABLE game_genres (
    steam_game_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (steam_game_id, genre_id),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tag TEXT
);

CREATE TABLE game_tags (
    steam_game_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (steam_game_id, tag_id),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    category TEXT
);

CREATE TABLE game_categories (
    steam_game_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (steam_game_id, category_id),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE screenshots (
    steam_game_id INTEGER,
    screenshot_url TEXT,
    PRIMARY KEY (steam_game_id, screenshot_url),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id)
);

CREATE TABLE trailers (
    steam_game_id INTEGER,
    trailer_url TEXT,
    PRIMARY KEY (steam_game_id, trailer_url),
    FOREIGN KEY (steam_game_id) REFERENCES about_games(steam_game_id)
);
