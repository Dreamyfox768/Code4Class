from enum import Enum, auto
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame
)
from PyQt6.QtGui import QPainter, QBrush, QColor, QFont

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
        self.green_s = int(green_s)
        self.yellow_s = int(yellow_s)
        self.red_s = int(red_s)
        self.ped_s = int(ped_s)
        self.phase = Phase.RED
        self.timer = Timer()
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


class TrafficLightWidget(QFrame):
    def __init__(self, tl: TrafficLight, parent=None):
        super().__init__(parent)
        self.tl = tl
        self.setFixedSize(320, 400)
        self.setStyleSheet("background-color: white; border: 1px solid gray;")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        centers = [(160, 50), (160, 140), (160, 230), (160, 320)]
        radius = 30
        colors = {
            Phase.RED: QColor('#ff0000'),
            Phase.YELLOW: QColor('#ffff00'),
            Phase.GREEN: QColor('#00ff00'),
            Phase.PED_CROSS: QColor('#0000ff')
        }
        off = QColor('#2b2b2b')

        for i, phase in enumerate([Phase.RED, Phase.YELLOW, Phase.GREEN, Phase.PED_CROSS]):
            c = colors[phase] if self.tl.phase == phase else off
            painter.setBrush(QBrush(c))
            painter.drawEllipse(centers[i][0]-radius, centers[i][1]-radius, radius*2, radius*2)


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TrafficLight — Simulator (PyQt)")
        self.tl = TrafficLight(green_s=5, yellow_s=2, red_s=4)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.gui_tick)
        self.running = False

        # --- Layout ---
        vbox = QVBoxLayout(self)

        self.tl_widget = TrafficLightWidget(self.tl)
        vbox.addWidget(self.tl_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        self.status_label = QLabel("", self)
        self.status_label.setFont(QFont('Arial', 12))
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.status_label)

        self.msg_label = QLabel("", self)
        self.msg_label.setFont(QFont('Arial', 10, QFont.FontStyle.StyleItalic))
        self.msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.msg_label)

        # Buttons
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")
        self.ped_btn = QPushButton("Ped Request")
        for b in [self.start_btn, self.stop_btn, self.reset_btn, self.ped_btn]:
            hbox.addWidget(b)

        # Connect buttons
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)
        self.ped_btn.clicked.connect(self.PED_CROSS)

        self.update_view()

    def update_view(self):
        self.tl_widget.update()
        self.status_label.setText(f"{self.tl.phase.name} ({self.tl._remaining}s) t={self.tl.timer.t}")

    def gui_tick(self):
        self.tl.tick()
        self.update_view()
        if self.running:
            self.timer.start()

    def start(self):
        if self.running:
            return
        self.running = True
        self.update_view()
        self.timer.start()

    def stop(self):
        self.running = False
        self.timer.stop()

    def PED_CROSS(self):
        self.tl.request_ped()
        self.msg_label.setText("Pedestrian Request Received!")
        QTimer.singleShot(2000, lambda: self.msg_label.setText(""))

    def reset(self):
        self.stop()
        self.tl.reset()
        self.update_view()
        self.msg_label.setText("System Reset to Initial State")
        QTimer.singleShot(2000, lambda: self.msg_label.setText(""))


def main():
    app = QApplication([])
    win = Main()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
