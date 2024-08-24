from PySide6.QtWidgets import QPushButton
from functools import partial

from view import PaintView
from model import PaintModel


class PaintController:
    def __init__(self):
        self.view = PaintView()
        self.model = PaintModel()
        self.add_functionality()

    def add_functionality(self):
        for btn in self.view.tool_panel.ui.frm_palette.findChildren(QPushButton):
            btn.clicked.connect(partial(self.change_brush_color, btn.styleSheet().split(' ')[1]))

        self.view.tool_panel.ui.slider_brush_size.valueChanged.connect(self.change_brush_size)
        self.view.tool_panel.ui.slider_red.valueChanged.connect(self.rgb_slider_moved)
        self.view.tool_panel.ui.slider_green.valueChanged.connect(self.rgb_slider_moved)
        self.view.tool_panel.ui.slider_blue.valueChanged.connect(self.rgb_slider_moved)

    def change_brush_color(self, color: str):
        self.update_rgb_sliders(color)
        self.model.set_brush_color(color)
        brush_size = self.model.get_brush_size()
        self.view.update_brush(brush_size, color)

    def change_brush_size(self, size: int):
        self.model.set_brush_size(size)
        brush_color = self.model.get_brush_color()
        self.view.update_brush(size, brush_color)

    def update_rgb_sliders(self, color: str):
        rgb = self.model.convert_hex_to_rgb(color)
        self.view.update_rgb_sliders(rgb.red, rgb.green, rgb.blue)

    def rgb_slider_moved(self):
        hex_color = self.model.convert_rgb_to_hex(*self.view.get_rgb_sliders_values())
        self.view.update_brush(self.model.get_brush_size(), hex_color)
