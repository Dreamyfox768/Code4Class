'''
Implement a TrafficLight class with phases and forecasting.
'''

from enum import Enum, auto

class Phase(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class TrafficLight:

    def __init__(self, green_s=30, yellow_s=4, red_s=30):
        self.green_s = green_s
        self.red_s = red_s
        self.yellow_s = yellow_s
        self.phase = Phase.RED

    def next(self):
        if self.phase == Phase.RED:
            self.phase = Phase.GREEN
        elif self.phase == Phase.GREEN:
            self.phase = Phase.YELLOW
        elif self.phase == Phase.YELLOW:
            self.phase = Phase.RED

    def forecast(self, foward):
        phasingorder = [Phase.RED, Phase.GREEN, Phase.YELLOW]
        curent_position = phasingorder.index(self.phase)
        upcoming_phases = []

        for step in range(1, foward + 1):
            next_phase = (curent_position + step) % len(phasingorder)
            upcoming_phases.append(phasingorder[next_phase].name)

        return upcoming_phases

    def show(self):
        print(f"Phase: {self.phase.name} (G = {self.green_s}, Y = {self.yellow_s}, R = {self.red_s})")

# Demonstration

T1 = TrafficLight()
T1.show()
print(T1.forecast(7))
T1.next()
T1.show()
