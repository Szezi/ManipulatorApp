from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ManipulatorApp.modules import trajectory


class MplWidget(QWidget):
    """ MplWidget for simulation robotic movement"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111, projection='3d', position=[0.01, 0.01, 1, 1])
        self.setLayout(vertical_layout)

    def Canvas(self):
        self.canvas.axes.set_ylim([500, -500])
        self.canvas.axes.set_xlim([-50, 500])
        self.canvas.axes.set_zlim([0, 600])
        self.canvas.axes.set_xlabel('x')
        self.canvas.axes.set_ylabel('y')
        self.canvas.axes.set_zlabel('z')

    def mpl_draw(self, xyz_1=[0, 0, 268], xyz_2=[0, 0, 418], xyz_3=[0, 0, 472], xyz_4=[0, 0, 472]):
        n = 2
        base = trajectory.cp_linear([0.0, 0.0, 0.0], [0.0, 0.0, 118.0], n)
        link1 = trajectory.cp_linear([0.0, 0.0, 118.0], xyz_1, n)
        link2 = trajectory.cp_linear(xyz_1, xyz_2, n)
        link3 = trajectory.cp_linear(xyz_2, xyz_3, n)
        link4 = trajectory.cp_linear(xyz_3, xyz_4, n)

        self.canvas.axes.clear()
        self.canvas.axes.plot(base[:, 0], base[:, 1], base[:, 2], color='green', marker='o',
                              linestyle='solid', linewidth=5, markersize=10)
        self.canvas.axes.plot(link1[:, 0], link1[:, 1], link1[:, 2], color='red', marker='o',
                              linestyle='solid', linewidth=5, markersize=10)
        self.canvas.axes.plot(link2[:, 0], link2[:, 1], link2[:, 2], color='blue', marker='o',
                              linestyle='solid', linewidth=5, markersize=10)
        self.canvas.axes.plot(link3[:, 0], link3[:, 1], link3[:, 2], color='purple', marker="h",
                              linestyle='solid', linewidth=5,
                              markersize=5)
        self.canvas.axes.plot(link4[:, 0], link4[:, 1], link4[:, 2], color='purple', marker="h",
                                           linestyle='solid', linewidth=5,
                                           markersize=5)
        self.canvas.axes.text(xyz_4[0], xyz_4[1], xyz_4[2], '({:.2f}, {:.2f}, {:.2f})'.format(xyz_4[0], xyz_4[1], xyz_4[2]), weight='bold',
                                                fontsize=10)
        self.Canvas()

        self.canvas.draw()