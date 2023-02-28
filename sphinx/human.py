class Prey:
    name: str

class Human(Prey):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> str:
        pass

    def process_riddle(self, riddle: str):
        pass

