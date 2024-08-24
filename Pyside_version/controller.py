from PySide6.QtCore import QLine, QLineF
from PySide6.QtGui import QPen, QColor, Qt
from PySide6.QtWidgets import QPushButton
from functools import partial

from view import PaintView
from model import PaintModel

STARTING_COLOR = '#000'
STARTING_BRUSH_SIZE = 20


class PaintController:
    def __init__(self):
        self.last_x = None
        self.last_y = None
        self.view = PaintView()
        self.model = PaintModel()
        self.add_functionality()
        self.initialize()

    def initialize(self):
        self.model.set_brush_color(STARTING_COLOR)
        self.model.set_brush_size(STARTING_BRUSH_SIZE)

        # Create pen object with default color and size
        self.pen = QPen(QColor(self.model.get_brush_color()),
                        self.model.get_brush_size())

        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        self.view.draw_brush_preview(self.model.get_brush_size(), self.model.get_brush_color())

    def add_functionality(self):
        for btn in self.view.tool_panel.ui.frm_palette.findChildren(QPushButton):
            btn.clicked.connect(partial(self.change_brush_color, btn.styleSheet().split(' ')[1]))

        self.view.tool_panel.ui.slider_brush_size.valueChanged.connect(self.change_brush_size)
        self.view.tool_panel.ui.slider_red.valueChanged.connect(self.rgb_slider_moved)
        self.view.tool_panel.ui.slider_green.valueChanged.connect(self.rgb_slider_moved)
        self.view.tool_panel.ui.slider_blue.valueChanged.connect(self.rgb_slider_moved)

        self.view.canvas.mouse_pressed.connect(self.handle_mouse_pressed)
        self.view.canvas.mouse_moved.connect(self.handle_mouse_movement)
        self.view.canvas.mouse_released.connect(self.handle_mouse_released)
        self.view.tool_panel.ui.btn_clear.clicked.connect(self.clear_canvas)
        self.view.tool_panel.ui.btn_eraser.toggled.connect(self.activate_eraser)

    def handle_mouse_pressed(self, event):
        # if self.last_x and self.last_y:
        current_position = event.pos()
        self.view.draw_line(
            QLine(current_position.x(),
                  current_position.y(),
                  current_position.x() + 1,
                  current_position.y() + 1
                  ), self.pen
        )

    def handle_mouse_movement(self, event):
        current_position = event.pos()

        if self.last_x and self.last_y:
            # Draw a line from the last position to the current position
            self.view.draw_line(
                QLine(self.last_x,
                      self.last_y,
                      current_position.x(),
                      current_position.y()
                      ), self.pen
            )

        # Update the last position
        self.last_x = current_position.x()
        self.last_y = current_position.y()

    def handle_mouse_released(self, event):
        # Reset the last position
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        self.view.clear_canvas()

    def activate_eraser(self, eraser_is_active):
        """Activate eraser mode and set color to canvas background."""
        if eraser_is_active:
            self.pen.setColor("#f3f3f3")
            self.view.set_eraser_mode(True)
        else:
            self.pen.setColor(self.model.get_brush_color())
            self.view.set_eraser_mode(False)
        self.view.draw_brush_preview(self.model.get_brush_size(),
                                     self.model.get_brush_color())

        # self.is_brush_active.set(False)
        # # Change the eraser button color to active color
        # self.mark_as_active()
        # # Save the color
        # self.last_color = self.color_string.get()
        # # Change the brush color to the background color
        # self.color_string.set(CANVAS_BG)

    def change_brush_color(self, color: str):
        self.pen.setColor(QColor(color))
        self.update_rgb_sliders(color)
        self.model.set_brush_color(color)
        brush_size = self.model.get_brush_size()
        self.view.update_brush(brush_size, color)
        self.view.update_slider_accent_color(color)

    def change_brush_size(self, size: int):
        self.pen.setWidth(size)

        self.model.set_brush_size(size)
        brush_color = self.model.get_brush_color()
        self.view.update_brush(size, brush_color)

    def update_rgb_sliders(self, color: str):
        rgb = self.model.convert_hex_to_rgb(color)
        self.view.update_rgb_sliders(rgb.red, rgb.green, rgb.blue)

    def rgb_slider_moved(self):
        hex_color = self.model.convert_rgb_to_hex(*self.view.get_rgb_sliders_values())
        self.change_brush_color(hex_color)
        # self.view.update_brush(self.model.get_brush_size(), hex_color)
