from random import randint

from human import Human
from lion import Lion
from riddles import riddles

class Sphinx(Human, Lion):
    def pose_riddle(self) -> str:
        idx = randint(0, len(riddles) - 1)
        self.riddle_idx = idx
        return riddles[idx]["q"]

    def evaluate_answer(self, answer: str) -> bool:
        return answer == riddles[self.riddle_idx]["a"]
