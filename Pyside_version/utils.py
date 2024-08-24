from PySide6.QtCore import Qt, QRectF, Signal
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsView

from interface_ui import Ui_ToolPanel
from settings import *


class ToolPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ToolPanel()
        self.ui.setupUi(self)
        self.setGeometry(1020, 200, 200, 350)
        self.setWindowTitle(' ')
        # Make the tool panel to be always on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.palette_setup()
        self.show()

    def palette_setup(self):
        grid_layout = self.ui.frm_palette.layout()
        # add colors to the buttons
        for row in range(COLOR_ROWS):
            for col in range(COLOR_COLS):
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

    def mouseMoveEvent(self, event):
        self.mouse_moved.emit(event)

    def mouseReleaseEvent(self, event):
        self.mouse_released.emit(event)

    def mousePressEvent(self, event):
        self.mouse_pressed.emit(event)

    def resizeEvent(self, event):
        # Resize the scene to match the view
        self.setSceneRect(QRectF(self.viewport().rect()))
        super().resizeEvent(event)
