#used chatgpt for extracting player information
#following code actualy does extract player_info which it sees from in the .csv file
#berserk is the library here help us to connect online lichess player databse therefore extracting bulk data is really hard
#therefore I only extracted 1000 data for each elo from here


import pandas as pd
import berserk
import time
from tqdm import tqdm
import requests

# Step 1: Set up Lichess API session
TOKEN = "********************"  # Your actual Lichess API token
session = berserk.TokenSession(TOKEN)
client = berserk.Client(session)

# Step 2: Load game data
df = pd.read_csv("****_elo_games.csv")

# Step 3: Cache for player info to avoid duplicate API calls
player_cache = {}

# Step 4: Define player info fetch function with retry & 429 handling
def get_player_info(username, retries=3):
    if username in player_cache:
        return player_cache[username]

    for attempt in range(retries):
        try:
            data = client.users.get_public_data(username)
            stats = data.get("perfs", {})
            counts = data.get("count", {})

            most_played = max(
                ((mode, stats[mode].get("games", 0)) for mode in stats if isinstance(stats[mode], dict)),
                key=lambda x: x[1],
                default=("unknown", 0)
            )[0]

            def get_peak_rating(mode):
                perf = stats.get(mode, {})
                return None if perf.get("prov", False) else perf.get("rating", None)

            player_info = {
                "country": data.get("profile", {}).get("country", None),
                "title": data.get("title", None),
                "preferred_game": most_played,
                "peak_bullet": get_peak_rating("bullet"),
                "peak_blitz": get_peak_rating("blitz"),
                "peak_rapid": get_peak_rating("rapid"),
                "peak_classical": get_peak_rating("classical"),
                "total_wins": counts.get("win", 0),
                "total_draws": counts.get("draw", 0),
                "total_losses": counts.get("loss", 0)
            }

            player_cache[username] = player_info
            return player_info

        except berserk.exceptions.ResponseError as e:
            status_code = e.response.status_code
            print(f"[{username}] API error (try {attempt+1}/{retries}): HTTP {status_code}")
            if status_code == 429:
                print(" Too many requests. Waiting 60 seconds before retrying...")
                time.sleep(60)  # Respect the 60 seconds wait for rate limiting
        except requests.exceptions.RequestException as e:
            print(f"[{username}] Network error (try {attempt+1}/{retries}): {e}")

        time.sleep(1)  # short wait between retries

    print(f" Failed to fetch {username} after {retries} attempts.")
    return {
        "country": None, "title": None, "preferred_game": None,
        "peak_bullet": None, "peak_blitz": None, "peak_rapid": None,
        "peak_classical": None, "total_wins": None, "total_draws": None, "total_losses": None
    }

# Step 5: Enrich all rows with tqdm progress bar
white_data = []
black_data = []

for _, row in tqdm(df.iterrows(), total=len(df), desc="Enriching Games"):
    white_info = get_player_info(row["white"])
    black_info = get_player_info(row["black"])
    white_data.append(white_info)
    black_data.append(black_info)
    time.sleep(0.15)  # Respect API rate limit by waiting 0.15s between each call

# Step 6: Merge new data
white_df = pd.DataFrame(white_data).add_prefix("white_")
black_df = pd.DataFrame(black_data).add_prefix("black_")
df_enriched = pd.concat([df, white_df, black_df], axis=1)

# Step 7: Save final enriched dataset
df_enriched.to_csv("final_enriched_data_with_peaks.csv", index=False)
print(" Enriched CSV saved as final_enriched_data_with_peaks.csv")
