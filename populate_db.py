import json
from dotenv import load_dotenv
import pandas as pd
import os
import sqlite3
from datetime import datetime
from pathlib import Path

load_dotenv()

def load_json(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

games = load_json('data/games.json')

# initalize empty lists to store cleaned game data per table
about_games_cleaned = []
ratings_cleaned = []
support_cleaned = []
game_misc_cleaned = []
tags_cleaned = []
screenshots_cleaned = []
trailers_cleaned = []
categories_cleaned = []
genres_cleaned = []
developers_cleaned = []
publishers_cleaned = []

# sets to store all unique values for these data for their dim tables
all_tags = set()
all_categories = set()
all_genres = set()
all_developers = set()
all_publishers = set()

for gameID in games:
    # get game from games dict using gameID key
    game = games[gameID]
    # store gameID in variable for later use as steam_game_id in main table
    steam_game_id = gameID
    
    # initialize dictionaries for table entry
    about_game = {}
    ratings = {}
    support = {}
    game_misc = {}

    # data for about_games table
    game_name = game.get('name', 'Unknown Game')
    required_age = int(game.get('required_age', 0))
    release_date = game.get('release_date', None)
    price = float(game.get('price', 0.00))
    about_the_game = game.get('about_the_game', 'No description available.')
    description = game.get('detailed_description', 'No description available.')
    header_image = game.get('header_image', 'No image available.')
    website = game.get('website', 'No website available.')
    
    # add to about game dictionary
    about_game['steam_game_id'] = steam_game_id
    about_game['game_name'] = game_name
    about_game['required_age'] = required_age
    about_game['release_date'] = release_date
    about_game['price'] = price
    about_game['about_the_game'] = about_the_game
    about_game['description'] = description
    about_game['header_image'] = header_image
    about_game['website'] = website
    
    about_games_cleaned.append(about_game)
    
    # each of these will be extracted and put into its own table, one value per line
    developers = [dev.strip() for dev in game.get('developers', [])]
    publishers = [pub.strip() for pub in game.get('publishers', [])]
    genres = [genre.strip() for genre in game.get('genres', [])]
    categories = [cat.strip() for cat in game.get('categories', [])]
    screenshots = [screenshot.strip() for screenshot in game.get('screenshots', [])]
    movies = [movie.strip() for movie in game.get('movies', [])]
    tags = [tag.strip() for tag in game.get('tags', [])]
    
    # update sets with data
    all_tags.update(tags)
    all_categories.update(categories)
    all_genres.update(genres)
    all_developers.update(developers)
    all_publishers.update(publishers)
    
    # create developers dictionary
    for dev in developers:
        developers_cleaned.append({
            'steam_game_id': steam_game_id,
            'developer': dev
        })
    
    # create publishers dictionary
    for pub in publishers:
        publishers_cleaned.append({
            'steam_game_id': steam_game_id,
            'publisher': pub
        })
    
    # create genres dictionary
    for genre in genres:
        genres_cleaned.append({
            'steam_game_id': steam_game_id,
            'genre': genre
        })
        
    # create categories dictionary
    for cat in categories:
        categories_cleaned.append({
            'steam_game_id': steam_game_id,
            'category': cat
        })
        
    # create screenshots dictionary
    for screenshot in screenshots:
        screenshots_cleaned.append({
            'steam_game_id': steam_game_id,
            'screenshot_url': screenshot
        })
    
    # create trailers dictionary
    for movie in movies:
        trailers_cleaned.append({
            'steam_game_id': steam_game_id,
            'trailer_url': movie
        })
    
    # create tags dictionary
    for tag in tags:
        tags_cleaned.append({
            'steam_game_id': steam_game_id,
            'tag': tag
        })

    # data for ratings table
    positive_ratings = int(game.get('positive', 0))
    negative_ratings = int(game.get('negative', 0))
    metacritic_score = float(game.get("metacritic_score", "Unknown"))
    metacritic_url = game.get("metacritic_url", "Unknown")
    recommendations = int(game.get("recommendations", "Unknown"))
    # add to ratings dictionary
    ratings['steam_game_id'] = steam_game_id
    ratings['positive_ratings'] = positive_ratings
    ratings['negative_ratings'] = negative_ratings
    ratings['metacritic_score'] = metacritic_score
    ratings['metacritic_url'] = metacritic_url
    ratings['recommendations'] = recommendations
    ratings_cleaned.append(ratings)
    
    # data for game_misc table
    achievements = int(game.get("achievements", 0))
    median_playtime = int(game.get("median_playtime_forever", 0))
    average_playtime = int(game.get("average_playtime_forever", 0))
    peak_players = int(game.get("peak_ccu", 0))
    estimated_owners = game.get("estimated_owners", "Unknown")
    # add to game_misc dictionary
    game_misc['steam_game_id'] = steam_game_id
    game_misc['achievements'] = achievements
    game_misc['median_playtime'] = median_playtime
    game_misc['average_playtime'] = average_playtime
    game_misc['peak_player_count'] = peak_players
    game_misc['estimated_owners_range'] = estimated_owners
    estimated_ranges = [ int(players) for players in estimated_owners.split("-")]
    game_misc['estimated_owners_low'] = min(estimated_ranges)
    game_misc['estimated_owners_high'] = max(estimated_ranges)
    game_misc_cleaned.append(game_misc)
    
    # data for support table
    supports_windows = bool(game.get("windows", False))
    supports_mac = bool(game.get("mac", False))
    supports_linux = bool(game.get("linux", False))
    # add to support dictionary
    support['steam_game_id'] = steam_game_id
    support['supports_windows'] = supports_windows
    support['supports_mac'] = supports_mac
    support['supports_linux'] = supports_linux
    
    support_cleaned.append(support)
    
# convert sets to list of dictionaries for each table
tags_all_cleaned = []
categories_all_cleaned = []
genres_all_cleaned = []
developers_all_cleaned = []
publishers_all_cleaned = []
for i, tag in enumerate(all_tags):
    tags_all_cleaned.append({
        'id': i + 1,
        'tag': tag
    })

for i, category in enumerate(all_categories):
    categories_all_cleaned.append({
        'id': i + 1,
        'category': category
    })

for i, genre in enumerate(all_genres):
    genres_all_cleaned.append({
        'id': i + 1,
        'genre': genre
    })

for i, developer in enumerate(all_developers):
    developers_all_cleaned.append({
        'id': i + 1,
        'developer': developer
    })

for i, publisher in enumerate(all_publishers):
    publishers_all_cleaned.append({
        'id': i + 1,
        'publisher': publisher
    })

# convert lists of dictionaries to pandas dataframes

# main tables
about_games_df = pd.DataFrame(about_games_cleaned)
about_games_df['release_date'] = pd.to_datetime(about_games_df['release_date'], errors='coerce') # convert to datetime
ratings_df = pd.DataFrame(ratings_cleaned)
support_df = pd.DataFrame(support_cleaned)
game_misc_df = pd.DataFrame(game_misc_cleaned)


# print(about_games_df.head())

# about_games_df.to_csv('data/about_games.csv', index=False)

# screenshots and trailers fact tables
screenshots_df = pd.DataFrame(screenshots_cleaned)
trailers_df = pd.DataFrame(trailers_cleaned)

# junction tables info
tags_df = pd.DataFrame(tags_cleaned) 
categories_df = pd.DataFrame(categories_cleaned) 
genres_df = pd.DataFrame(genres_cleaned) 
developers_df = pd.DataFrame(developers_cleaned) 
publishers_df = pd.DataFrame(publishers_cleaned) 

# dim tables
tags_all_df = pd.DataFrame(tags_all_cleaned) # dim table
categories_all_df = pd.DataFrame(categories_all_cleaned) # dim table
genres_all_df = pd.DataFrame(genres_all_cleaned) # dim table
developers_all_df = pd.DataFrame(developers_all_cleaned) # dim table
publishers_all_df = pd.DataFrame(publishers_all_cleaned) # dim table

# create junction tables dfs
tag_junction_df = tags_df.merge(tags_all_df, on='tag', how='inner')
tag_junction_df = tag_junction_df[['steam_game_id', 'id']].rename(columns={"id": "tag_id"})

category_junction_df = categories_df.merge(categories_all_df, on='category', how='inner')
category_junction_df = category_junction_df[['steam_game_id', 'id']].rename(columns={"id": "category_id"})

genre_junction_df = genres_df.merge(genres_all_df, on='genre', how='inner')
genre_junction_df = genre_junction_df[['steam_game_id', 'id']].rename(columns={"id": "genre_id"})

developer_junction_df = developers_df.merge(developers_all_df, on='developer', how='inner')
developer_junction_df = developer_junction_df[['steam_game_id', 'id']].rename(columns={"id": "developer_id"})

publisher_junction_df = publishers_df.merge(publishers_all_df, on='publisher', how='inner')
publisher_junction_df = publisher_junction_df[['steam_game_id', 'id']].rename(columns={"id": "publisher_id"})

# load to db
db_path = Path(__file__).parent / "data" / "games.db"
conn = sqlite3.connect(db_path)

about_games_df.to_sql('about_games', conn, if_exists='append', index=False)
ratings_df.to_sql('game_rating', conn, if_exists='append', index=False)
support_df.to_sql('game_support', conn, if_exists='append', index=False)
game_misc_df.to_sql('game_misc', conn, if_exists='append', index=False)
screenshots_df.to_sql('screenshots', conn, if_exists='append', index=False)
trailers_df.to_sql('trailers', conn, if_exists='append', index=False)
tags_all_df.to_sql('tags', conn, if_exists='append', index=False)
categories_all_df.to_sql('categories', conn, if_exists='append', index=False)
genres_all_df.to_sql('genres', conn, if_exists='append', index=False)
developers_all_df.to_sql('developers', conn, if_exists='append', index=False)
publishers_all_df.to_sql('publishers', conn, if_exists='append', index=False)
tag_junction_df.to_sql('game_tags', conn, if_exists='append', index=False)
category_junction_df.to_sql('game_categories', conn, if_exists='append', index=False)
genre_junction_df.to_sql('game_genres', conn, if_exists='append', index=False)
developer_junction_df.to_sql('game_developers', conn, if_exists='append', index=False)
publisher_junction_df.to_sql('game_publishers', conn, if_exists='append', index=False)

print("Data loaded into database successfully.")
conn.commit()
conn.close()
