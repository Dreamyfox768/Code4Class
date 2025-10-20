'''
class note
classes help to compile same data as atribute and method
attribute:define the state of the statement
Method: behavior the system possess

phone:
attritube: color, brand, size
method: call, message, video games

'''


#part 1

class TrafficLight:
    def __init__(self, phase = 'RED',green_s= 30, yellow_s=4, red_s=30 ):
        self.green_s = green_s
        self.yellow_s = yellow_s
        self.red_s = red_s
        self.phase= 'RED'

    def next(self):
        if self.phase == "RED":
            self.phase = "GREEN"
        elif self.phase == "GREEN":
            self.phase = "YELLOW"
        elif self.phase == "YELLOW":
            self.phase = "RED"
    def show(self):
        print(f"Phase: {self.phase} (G = {self.green_s}, Y = {self.yellow_s}, R = {self.red_s})")

    def start(self):
        self.phase = 'RED'
        print( f'Started: phase set to {self.phase}')
    def set_cycle(self, green , yellow, red):
        self.green_s = green
        self.yellow_s = yellow
        self.red_s = red
        
        
        
        
t1 = TrafficLight()
t2 = TrafficLight()
t1.start()
t1.show()
t1.next()
t1.show()


t2.start()
t2.show()
t2.next()
t2.show()


t2.set_cycle(25,3,15)

