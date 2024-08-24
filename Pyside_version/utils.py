import sys

from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QBrush, QPalette

from settings import *
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QWidget, QApplication, QPushButton
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
        # self.draw_brush_preview(20)

    def palette_setup(self):
        grid_layout = self.ui.frm_palette.layout()
        # add colors to the buttons
        for row in range(6):
            for col in range(4):
                button = grid_layout.itemAtPosition(row, col).widget()
                button.setStyleSheet(f"background-color: #{COLORS[row][col]}")

    def draw_brush_preview(self, brush_size: int, brush_color: str):
        self.ui.lbl_preview.setFixedSize(102, 102)
        pixmap = QPixmap(102, 102)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor(brush_color), Qt.BrushStyle.SolidPattern))
        radii = brush_size / 2
        painter.drawEllipse(QPoint(51, 51), radii, radii)
        painter.end()

        self.ui.lbl_preview.setPixmap(pixmap)

    def closeEvent(self, event):
        QApplication.instance().quit()
