from dataclasses import dataclass


@dataclass
class GameStep:
    game_id: str
    iteration: int
    units: list
    structures: list
    enemy_units: list
    enemy_structures: list
