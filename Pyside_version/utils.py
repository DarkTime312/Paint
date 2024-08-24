import sys

from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QBrush, QPalette

from settings import *
from PySide6.QtCore import Qt, QPoint, QRectF, Signal
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QGraphicsView
from interface_ui import Ui_ToolPanel


class ToolPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ToolPanel()
        self.ui.setupUi(self)
        self.setGeometry(1020, 200, 200, 350)
        self.setWindowTitle(' ')
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.palette_setup()
        self.show()
        # self.draw_brush_preview(20)

    def palette_setup(self):
        grid_layout = self.ui.frm_palette.layout()
        # add colors to the buttons
        for row in range(6):
            for col in range(4):
                button = grid_layout.itemAtPosition(row, col).widget()
                button.setStyleSheet(f"background-color: #{COLORS[row][col]}")

    def closeEvent(self, event):
        QApplication.instance().quit()


class Canvas(QGraphicsView):
    mouse_pressed = Signal(object)
    mouse_moved = Signal(object)
    mouse_released = Signal(object)

    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def mouseMoveEvent(self, event):
        # Emit the signal with the event
        self.mouse_moved.emit(event)

        # # print('mouse moved')
        # pos = event.position()
        # # print(pos)
        # # super().mouseMoveEvent(event)  # Call the base class implementation
        #
        # if self.last_x is None:  # First event.
        #     self.last_x = pos.x()
        #     self.last_y = pos.y()
        #     return  # Ignore the first time.
        # self.scene().addLine(self.last_x, self.last_y, pos.x(), pos.y())
        #
        # # Update the origin for next time.
        #
        # self.last_x = pos.x()
        # self.last_y = pos.y()

    def mouseReleaseEvent(self, event):
        self.mouse_released.emit(event)

    def mousePressEvent(self, event):
        self.mouse_pressed.emit(event)

    def resizeEvent(self, event):
        # Resize the scene to match the view
        self.setSceneRect(QRectF(self.viewport().rect()))
        super().resizeEvent(event)
