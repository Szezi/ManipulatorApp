from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplWidget(QWidget):
    """ MplWidget for simulation robotic movement"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111, projection='3d', position=[0.01, 0.01, 1, 1])
        self.setLayout(vertical_layout)

        self.canvas.axes.clear()
        self.canvas.axes.plot(0, 0, 118, color='green', marker='o', linestyle='solid',
                              linewidth=5, markersize=10)
        self.canvas.axes.plot(0, 0, 268, color='red', marker='o', linestyle='solid',
                              linewidth=5, markersize=10)
        self.canvas.axes.plot(0, 0, 418, color='blue', marker='o', linestyle='solid',
                              linewidth=5, markersize=10)
        self.canvas.axes.plot(0, 0, 472, color='purple', marker="h", linestyle='solid', linewidth=5,
                              markersize=10)
        self.Canvas()

        self.canvas.draw()

    def Canvas(self):
        self.canvas.axes.set_ylim([500, -500])
        self.canvas.axes.set_xlim([-50, 500])
        self.canvas.axes.set_zlim([0, 600])
        self.canvas.axes.set_xlabel('x')
        self.canvas.axes.set_ylabel('y')
        self.canvas.axes.set_zlabel('z')
