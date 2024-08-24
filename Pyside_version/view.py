from PySide6.QtCore import Qt, QPoint, QLine
from PySide6.QtGui import QIcon, QPixmap, QPainter, QBrush, QColor, QPen, QPalette
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsScene, QVBoxLayout

import resources_rc
from utils import ToolPanel, Canvas


class PaintView(QWidget):
    def __init__(self):
        super().__init__()
        self.eraser_mode = False
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle(' ')
        self.setWindowIcon(QIcon(":assets/empty.ico"))

        self.tool_panel = ToolPanel()
        # Create a QGraphicsScene
        self.scene = QGraphicsScene()
        # Create a Canvas (QGraphicsView)
        self.canvas = Canvas(self.scene)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)

        self.tool_panel.ui.lbl_preview.setFixedSize(102, 102)

    def draw_line(self, line: QLine, pen: QPen):
        self.scene.addLine(line, pen)

    def clear_canvas(self):
        self.scene.clear()

    def closeEvent(self, event):
        QApplication.instance().quit()

    def wheelEvent(self, event):
        # Check the direction of the wheel movement
        current_brush_size = self.get_brush_size()

        if event.angleDelta().y() > 0:
            self.set_brush_size(min(100, current_brush_size + 5))
        else:
            self.set_brush_size(max(20, current_brush_size - 5))

    def draw_brush_preview(self, brush_size: int, brush_color: str):
        pixmap = QPixmap(102, 102)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.SolidLine if self.eraser_mode else Qt.PenStyle.NoPen)
        painter.setBrush(
            QBrush(QColor(Qt.GlobalColor.transparent if self.eraser_mode else brush_color), Qt.BrushStyle.SolidPattern))
        radii = brush_size / 2
        # Draw the ellipse at the center of our pixmap
        painter.drawEllipse(QPoint(51, 51), radii, radii)
        painter.end()

        self.tool_panel.ui.lbl_preview.setPixmap(pixmap)

    def set_eraser_mode(self, state: bool):
        self.eraser_mode = state

    def update_rgb_sliders(self, r: int, g: int, b: int):
        self.tool_panel.ui.slider_red.setValue(r)
        self.tool_panel.ui.slider_green.setValue(g)
        self.tool_panel.ui.slider_blue.setValue(b)

    def get_rgb_sliders_values(self) -> tuple[int, int, int]:
        red = self.tool_panel.ui.slider_red.value()
        green = self.tool_panel.ui.slider_green.value()
        blue = self.tool_panel.ui.slider_blue.value()
        return red, green, blue

    def get_brush_size(self):
        return self.tool_panel.ui.slider_brush_size.value()

    def set_brush_size(self, value):
        self.tool_panel.ui.slider_brush_size.setValue(value)

    def update_slider_accent_color(self, color: str):
        palette = self.tool_panel.ui.slider_brush_size.palette()
        palette.setColor(QPalette.ColorRole.Accent, QColor(color))
        self.tool_panel.ui.slider_brush_size.setPalette(palette)
