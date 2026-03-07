"""Load games from local replays."""
import json
from pathlib import Path

from .model.game import GameInfo


def load_games(replays_path: Path) -> dict:
    if not replays_path.is_dir():
        raise RuntimeError(f'Invalid directory: {replays_path.absolute()}')
    games = {}
    for game_info_path in replays_path.glob('info_*.json'):
        with open(game_info_path, 'r', encoding='utf-8') as fd:
            game_info_raw = json.load(fd)
            game_info = GameInfo(**game_info_raw)
            games[game_info.game_id] = game_info
    return games
