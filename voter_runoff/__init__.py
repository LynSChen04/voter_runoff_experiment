from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Candidate:
    name: str
    payoffs: Tuple[int, int, int]  # (voter_1, voter_2, voter_3)

@dataclass
class ExperimentConfig:
    num_rounds: int = 3
    num_players: int = 12
    players_per_role: int = 4  # 12 / 3 roles
    candidates: List[Candidate] = None
    
    def __post_init__(self):
        if self.candidates is None:
            self.candidates = [
                Candidate("A", (3, 2, 1)),
                Candidate("B", (1, 3, 2)),
                Candidate("C", (2, 1, 3)),
            ]

# Initialize experiment configuration
config = ExperimentConfig()