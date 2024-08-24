from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QApplication
import resources_rc
from utils import ToolPanel


class PaintView(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle(' ')
        self.setWindowIcon(QIcon(":assets/empty.ico"))

        self.tool_panel = ToolPanel()
        self.tool_panel.show()

    def closeEvent(self, event):
        QApplication.instance().quit()

    def update_brush(self, brush_size: int, color: str):
        self.tool_panel.draw_brush_preview(brush_size, color)

    def update_rgb_sliders(self, r: int, g: int, b: int):
        self.tool_panel.ui.slider_red.setValue(r)
        self.tool_panel.ui.slider_green.setValue(g)
        self.tool_panel.ui.slider_blue.setValue(b)

    def get_rgb_sliders_values(self) -> tuple[int, int, int]:
        red = self.tool_panel.ui.slider_red.value()
        green = self.tool_panel.ui.slider_green.value()
        blue = self.tool_panel.ui.slider_blue.value()
        return red, green, blue
