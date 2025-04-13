import json
from dotenv import load_dotenv
import pandas as pd
import os
import sqlite3

load_dotenv()

def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

games = load_json('data/games.json')
games_cleaned = []

for gameID in games:
    game = games[gameID]
    
    processed_game = {}
    
    processed_game['game_id'] = gameID
    processed_game['game_name'] = game.get('name', 'Unknown Game')
    processed_game['required_age'] = game.get('required_age', 0)
    processed_game['release_date'] = game.get('release_date', 'Unknown Release Date')
    processed_game['price'] = game.get('price', 0.00)
    processed_game['about_the_game'] = game.get('about_the_game', 'No description available.')
    processed_game['description'] = game.get('detailed_description', 'No description available.')
    processed_game['header_image'] = game.get('header_image', 'No image available.')
    processed_game['website'] = game.get('website', 'No website available.')
    processed_game['developers'] = ",".join([dev for dev in game.get('developers', [])])
    processed_game['publishers'] = ",".join([pub for pub in game.get('publishers', [])])
    processed_game['genres'] = ",".join([genre for genre in game.get('genres', [])])
    processed_game['categories'] = ",".join([cat for cat in game.get('categories', [])])
    processed_game['screenshots'] = ",".join([screenshot for screenshot in game.get('screenshots', [])])
    processed_game['movies'] = ",".join([movie for movie in game.get('movies', [])])
    processed_game['tags'] = ",".join([tag for tag in game.get('tags', [])])
    processed_game['positive_ratings'] = game.get('positive', 0)
    processed_game['negative_ratings'] = game.get('negative', 0)
    processed_game['estimated_owners'] = game.get("estimated_owners", "Unknown")
    processed_game['metacritic_score'] = game.get("metacritic_score", "Unknown")
    processed_game['metacritic_url'] = game.get("metacritic_url", "Unknown")
    processed_game['recommendations'] = game.get("recommendations", "Unknown")
    processed_game['achievements'] = game.get("achievements", "Unknown")
    processed_game['median_playtime'] = game.get("median_playtime_forever", "Unknown")
    processed_game['average_playtime'] = game.get("average_playtime_forever", "Unknown")
    processed_game['peak_players'] = game.get("peak_ccu", "Unknown")
    processed_game['supports_windows'] = game.get("windows", False)
    processed_game['supports_mac'] = game.get("mac", False)
    processed_game['supports_linux'] = game.get("linux", False)
    
    games_cleaned.append(processed_game)
    
games_df = pd.DataFrame(games_cleaned)

with open('data/columns.txt', 'w') as f:
    for column in games_df.columns:
        f.write(f"{column}\n")

# conn = sqlite3.connect("data/games.db")

# games_df.to_sql(
#     'games',
#     con=conn,
#     if_exists='replace',
#     index=False
# )

# conn.commit()
# conn.close()