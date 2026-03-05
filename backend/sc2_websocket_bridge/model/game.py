import datetime
from dataclasses import dataclass


@dataclass
class GameStep:
    game_id: str
    iteration: int
    units: list
    structures: list
    enemy_units: list
    enemy_structures: list

@dataclass
class GameInfo:
    game_id: str
    bot_name: str
    map: str
    opponent_name: str
    started: datetime.datetime
    finished: datetime.datetime
