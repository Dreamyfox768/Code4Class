'''



Problem Question:
• Build a tiny Tkinter simulator that visualizes the provided TrafficLight model running
in real time. You will be given the model file (traffic_light.py) containing Phase, Timer,
and TrafficLight. Do not modify that model. Your job is to write a small GUI wrapper
that simulates the model by periodically calling its tick() method and updating the
Canvas display.
• Write a main() function (and a runnable if __name__ == '__main__': main() at the
bottom).
• Creates a Canvas (e.g., 320×320) and draws three ovals for the red/yellow/green
lamps. Draw them using canvas.create_oval.
• A small text label on the canvas showing the current phase and remaining seconds
(for example: GREEN (3s) t=7). Create that text item once and update it each tick.
• Two buttons below the canvas: Start and Stop.
• Methods:
• update_view() — read tl.phase and tl._remaining, set fills for id_red, id_yel,
id_grn and update text_id with f"{tl.phase.name} ({tl._remaining}s) t={tl.timer.t}".
• canvas.itemconfigure(red, fill='#ff0000')
• gui_tick() — call tl.tick() (only place in the program that advances the model), call
update_view(), and if root.running is True schedule the next tick with
root.after(interval_ms, gui_tick).
• start() — if not already running set root.running = True, call update_view() once,
then schedule the first gui_tick with root.after(interval_ms, gui_tick).
• stop() — set root.running = False.

'''
import tkinter as tk
from enum import Enum, auto

# ---------- model (as before) ----------
class Phase(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class Timer:
    def __init__(self):
        self.t = 0
    def tick(self):
        self.t += 1
        return self.t

class TrafficLight:
    def __init__(self, green_s=30, yellow_s=4, red_s=30):
        self.green_s  = int(green_s)
        self.yellow_s = int(yellow_s)
        self.red_s    = int(red_s)
        self.phase    = Phase.RED
        self.timer    = Timer()
        self._remaining = self.red_s

    def next(self):
        if   self.phase == Phase.RED:
            self.phase = Phase.GREEN
            self._remaining = self.green_s
        elif self.phase == Phase.GREEN:
            self.phase = Phase.YELLOW
            self._remaining = self.yellow_s
        else:
            self.phase = Phase.RED
            self._remaining = self.red_s

    def tick(self):
        self.timer.tick()
        if self._remaining <= 0:
            self.next()
            return True
        self._remaining -= 1
        if self._remaining == 0:
            self.next()
            return True
        return False

# ---------- GUI wrapper ----------
def main():
    global root, canvas, id_red, id_yel, id_grn, text_id, tl, interval_ms
    root = tk.Tk()
    root.title("Traffic Light Simulator")
    root.geometry("320x400")
    root.running = False
    interval_ms = 50

    tl = TrafficLight()

    canvas = tk.Canvas(root, width=320, height=320, bg='white')
    canvas.pack()

    positions = [
        (100, 10, 200, 100),   # red
        (100, 100, 202, 200),  # yellow
        (100, 200, 200, 300),  # green
    ]

    id_red = canvas.create_oval(*positions[0], fill='gray')
    id_yel = canvas.create_oval(*positions[1], fill='gray')
    id_grn = canvas.create_oval(*positions[2], fill='gray')

    text_id = canvas.create_text(300, 10, fill="purple", font=('Times', 20))

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    start_btn = tk.Button(button_frame, text="Start", command=start, width=10)
    start_btn.pack(side='left', padx=10)

    stop_btn = tk.Button(button_frame, text="Stop", command=stop, width=10)
    stop_btn.pack(side='right', padx=10)

    root.mainloop()

def update_view():
    # Red light
    if tl.phase == Phase.RED:
        canvas.itemconfigure(id_red, fill='#ff0000')
    else:
        canvas.itemconfigure(id_red, fill='gray')

    # Yellow light
    if tl.phase == Phase.YELLOW:
        canvas.itemconfigure(id_yel, fill='#ffff00')
    else:
        canvas.itemconfigure(id_yel, fill='gray')

    # Green light
    if tl.phase == Phase.GREEN:
        canvas.itemconfigure(id_grn, fill='#00ff00')
    else:
        canvas.itemconfigure(id_grn, fill='gray')

    canvas.itemconfigure(text_id, text=f"{tl.phase.name} ({tl._remaining}s) t={tl.timer.t}")


def gui_tick():
    if not root.running:
        return
    tl.tick()
    update_view()
    if root.running:
        root.after(interval_ms, gui_tick)

def start():
    if not root.running:
        root.running = True
        update_view()
        root.after(interval_ms, gui_tick)

def stop():
    root.running = False

if __name__ == "__main__":
    main()
