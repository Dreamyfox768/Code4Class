from enum import Enum, auto

class Phase(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class Timer:
    def __init__(self):
        self.time = 0

    def tick(self):
        self.time += 1
        return self.time


class TrafficLight:
    def __init__(self, green_s=30, yellow_s=4, red_s=30):
        self.phase = Phase.RED
        self.green_s = green_s
        self.yellow_s = yellow_s
        self.red_s = red_s
        self.timer = Timer()
        self.set_remaining = red_s + 1



    def next(self):
        if self.phase == Phase.RED:
            self.phase = Phase.GREEN
            self.set_remaining = self.green_s
        elif self.phase == Phase.GREEN:
            self.phase = Phase.YELLOW
            self.set_remaining = self.yellow_s
        else:
            self.phase = Phase.RED
            self.set_remaining = self.red_s
            
    def tick(self):
        self.timer.tick()
        self.set_remaining -= 1
        if self.set_remaining == 0:
            self.next()
            return True
        return False

    def __eq__(self, other):
        return (self.green_s, self.yellow_s, self.red_s, self.phase) == (other.green_s, other.yellow_s, other.red_s,
                                                                         other.phase)
    def __str__(self):
        return f"T={self.timer.time} | Phase={self.phase.name}   |Rem={self.set_remaining}  |(green_s={self.green_s}, yellow_s={self.yellow_s}, red_s={self.red_s})"

light = TrafficLight(green_s=5, yellow_s=2, red_s=4)

for _ in range(13):
    changed = light.tick()
    print(light)
    if changed:
        print("___+ Phase changed above")

