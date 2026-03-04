"""Load games from local replays."""
from pathlib import Path
import json


def load_games(replays_path: Path):
    if not replays_path.is_dir():
        raise RuntimeError(f'Invalid directory: {replays_path}')
    