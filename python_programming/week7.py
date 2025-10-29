import tkinter as tk
from enum import Enum, auto

# ---------- model (as before) ----------
class Phase(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    PED_CROSS = auto()


class Timer:
    def __init__(self):
        self.t = 0
    def tick(self):
        self.t += 1
        return self.t

class TrafficLight:
    def __init__(self, green_s=30, yellow_s=4, red_s=30, ped_s=5):
        self.green_s  = int(green_s)
        self.yellow_s = int(yellow_s)
        self.red_s    = int(red_s)
        self.ped_s = int(ped_s)
        self.phase    = Phase.RED
        self.timer    = Timer()
        self._remaining = self.red_s
        self.ped_requested = False

    def next(self):
        if self.phase == Phase.RED:
            if self.ped_requested:
                self.phase = Phase.PED_CROSS
                self._remaining = self.ped_s
                self.ped_requested = False
            else:
                self.phase = Phase.GREEN
                self._remaining = self.green_s
        elif self.phase == Phase.GREEN:
            self.phase = Phase.YELLOW
            self._remaining = self.yellow_s
        elif self.phase == Phase.YELLOW:
            self.phase = Phase.RED
            self._remaining = self.red_s
        elif self.phase == Phase.PED_CROSS:
            self.phase = Phase.GREEN
            self._remaining = self.green_s

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

    def request_ped(self):
        self.ped_requested = True

    def reset(self):
        self.phase = Phase.RED
        self.timer = Timer()
        self._remaining = self.red_s
        self.ped_requested = False

# ---------- minimal GUI that uses only root.running ----------
def main():
    root = tk.Tk()
    root.title("TrafficLight — Simulator")

    canvas = tk.Canvas(root, width=420, height=400, bg='white')
    canvas.pack(padx=15, pady=15)

    # small durations to see transitions during class
    tl = TrafficLight(green_s=5, yellow_s=2, red_s=4)

    # draw three lights once and keep their IDs (explicit coordinates)
    r = 30
    id_red = canvas.create_oval(160 - r, 50 - r, 160 + r, 50 + r, fill='#2b2b2b')
    id_yel = canvas.create_oval(160 - r, 140 - r, 160 + r, 140 + r, fill='#2b2b2b')
    id_grn = canvas.create_oval(160 - r, 230 - r, 160 + r, 230 + r, fill='#2b2b2b')
    id_blue = canvas.create_oval(160 - r, 320 - r, 160 + r, 320 + r, fill='#2b2b2b')
    text_id = canvas.create_text(100, 370, text='' , font=('Arial', 12))
    text_id2 = canvas.create_text(110, 170, text='', font=('Arial', 12))

    root.running = False
    interval_ms = 1000  # 1 second

    def update_view():
        """Set fills and label from the model state (very small)."""
        canvas.itemconfigure(id_red, fill='#ff0000' if tl.phase == Phase.RED else '#2b2b2b')
        canvas.itemconfigure(id_yel, fill='#ffff00' if tl.phase == Phase.YELLOW else '#2b2b2b')
        canvas.itemconfigure(id_grn, fill='#00ff00' if tl.phase == Phase.GREEN else '#2b2b2b')
        canvas.itemconfigure(id_blue, fill='#0000ff' if tl.phase == Phase.PED_CROSS else '#2b2b2b')

        canvas.itemconfigure(text_id, text=f"{tl.phase.name} ({tl._remaining}s)   t={tl.timer.t}", fill='black')
        canvas.lift(text_id)

    def gui_tick():
        tl.tick()
        update_view()
        if root.running:
            root.after(interval_ms, gui_tick)

    def start():
        if root.running:
            return
        root.running = True
        update_view()
        root.after(interval_ms, gui_tick)

    def stop():
        root.running = False

    def PED_CROSS():
        tl.request_ped()
        canvas.itemconfigure(text_id2, text="Pedestrian Request Received!")
        canvas.after(2000, lambda: canvas.itemconfigure(text_id2, text=""))

    def reset():
        stop()
        tl.reset()
        update_view()
        canvas.itemconfigure(text_id2, text="System Reset to Initial State")
        canvas.after(2000, lambda: canvas.itemconfigure(text_id2, text=""))

    ctrl = tk.Frame(root)
    ctrl.pack(pady=(6, 10))
    tk.Button(ctrl, text='Start', command=start, width=8).grid(row=0, column=0, padx=6)
    tk.Button(ctrl, text='Stop', command=stop, width=8).grid(row=0, column=1, padx=6)
    tk.Button(ctrl, text='reset', command=reset, width=8).grid(row=0, column=2, padx=6)
    tk.Button(ctrl, text='Ped request', command=PED_CROSS, width=10).grid(row=0, column=3, padx=6)

    update_view()
    root.mainloop()

if __name__ == '__main__':
    main()
