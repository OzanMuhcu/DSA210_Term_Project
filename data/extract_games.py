#used chatgpt to extract information from 2016 February chess data from lichess databse
#pgn.zst file was large for submitting on github therefore I didnt included one can easily reach the data from https://database.lichess.org/
#this following code extract information for unqie players only

import zstandard as zstd
import chess.pgn
from io import TextIOWrapper
from tqdm import tqdm
import json

# ---- CONFIG ----
INPUT_FILE = "lichess_db_standard_rated_2016-02.pgn.zst"
MAX_GAMES_PER_BUCKET = 1000
MAX_GAMES_PER_PLAYER = 1

# --- DATA HOLDERS ---
games_by_bucket = {"low": [], "mid": [], "high": []}
counts = {"low": 0, "mid": 0, "high": 0}
player_game_counts = {"low": {}, "mid": {}, "high": {}}

# --- HELPER FUNCTIONS ---
def get_bucket(avg_elo):
    if avg_elo < 1400:
        return "low"
    elif avg_elo <= 2000:
        return "mid"
    else:
        return "high"

def extract_headers(game):
    return {
        "white": game.headers.get("White"),
        "black": game.headers.get("Black"),
        "white_elo": int(game.headers.get("WhiteElo", 0)),
        "black_elo": int(game.headers.get("BlackElo", 0)),
        "result": game.headers.get("Result"),
        "opening": game.headers.get("Opening"),
        "eco": game.headers.get("ECO"),
        "site": game.headers.get("Site"),
        "time_control": game.headers.get("TimeControl"),
        "termination": game.headers.get("Termination"),
    }

def all_buckets_full():
    return all(counts[bucket] >= MAX_GAMES_PER_BUCKET for bucket in counts)

# --- MAIN PARSING LOOP ---
with open(INPUT_FILE, "rb") as f:
    dctx = zstd.ZstdDecompressor()
    stream = dctx.stream_reader(f)
    text_stream = TextIOWrapper(stream, encoding='utf-8', errors='ignore')

    print("Parsing games from PGN with player diversity...")
    pbar = tqdm(total=MAX_GAMES_PER_BUCKET * 3)

    while not all_buckets_full():
        game = chess.pgn.read_game(text_stream)
        if game is None:
            break

        try:
            white = game.headers.get("White")
            black = game.headers.get("Black")
            white_elo = int(game.headers.get("WhiteElo", 0))
            black_elo = int(game.headers.get("BlackElo", 0))

            if not white or not black or white_elo == 0 or black_elo == 0:
                continue

            avg_elo = (white_elo + black_elo) / 2
            bucket = get_bucket(avg_elo)

            # Skip if player has hit max quota
            white_count = player_game_counts[bucket].get(white, 0)
            black_count = player_game_counts[bucket].get(black, 0)
            if white_count >= MAX_GAMES_PER_PLAYER or black_count >= MAX_GAMES_PER_PLAYER:
                continue

            if counts[bucket] < MAX_GAMES_PER_BUCKET:
                data = extract_headers(game)
                games_by_bucket[bucket].append(data)
                counts[bucket] += 1

                player_game_counts[bucket][white] = white_count + 1
                player_game_counts[bucket][black] = black_count + 1

                pbar.update(1)
        except Exception:
            continue

    pbar.close()

# --- SAVE RESULTS ---
for bucket in games_by_bucket:
    with open(f"{bucket}_elo_games.json", "w") as f:
        json.dump(games_by_bucket[bucket], f, indent=2)

print("✅ Done! Extracted and saved 10K diverse games per Elo level.")
