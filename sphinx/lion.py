from human import Prey

class Lion:
    def eat_prey(self, prey: Prey):
        self.energy += len(prey.name)
