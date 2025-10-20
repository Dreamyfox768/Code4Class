'''
Implemented a TrafficLight class with phases and timing.
'''
from enum import Enum, auto

class Phase(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class TrafficLight:
    def __init__(self, green_s=30, yellow_s=4, red_s=30):
        self.green_s = green_s
        self.yellow_s = yellow_s
        self.red_s = red_s
        self.phase = Phase.RED

    def next(self):
        if self.phase == Phase.RED:
            self.phase = Phase.GREEN
        elif self.phase == Phase.GREEN:
            self.phase = Phase.YELLOW
        else: 
            self.phase = Phase.RED

    def __str__(self):
        return f"TrafficLight(phase={self.phase.name}, G={self.green_s}, Y={self.yellow_s}, R={self.red_s})"

T1 = TrafficLight()
print(T1)
T1.next()
print(T1)
