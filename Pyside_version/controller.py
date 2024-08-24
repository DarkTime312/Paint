from functools import partial

from PySide6.QtCore import QLine
from PySide6.QtGui import QPen, QColor, Qt
from PySide6.QtWidgets import QPushButton

from model import PaintModel
from view import PaintView
from settings import *


class PaintController:
    def __init__(self):
        self.pen = None
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
        self.view.draw_brush_preview(self.model.get_brush_size(),
                                     self.model.get_brush_color())

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
        """
        Handle the start of a drawing action.

        Args:
            event: The mouse event that triggered the start of drawing.

        This method is called when the mouse button is pressed. It starts
        the drawing by creating a small line at the mouse position.
        """
        current_position = event.pos()
        # Draw a tiny line to create a dot at the starting point
        self.view.draw_line(
            QLine(current_position.x(),
                  current_position.y(),
                  current_position.x() + 1,
                  current_position.y() + 1
                  ), self.pen
        )

    def handle_mouse_movement(self, event):
        """
        Handle the drawing action as the mouse moves.

        Args:
            event: The mouse event containing the current mouse position.

        This method is called when the mouse moves while the button is pressed.
        It continues the drawing by creating lines between the last known
        position and the current mouse position.
        """

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
        """
        Handle the end of a drawing action.

        Args:
            event: The mouse event that triggered the end of drawing.

        This method is called when the mouse button is released. It resets
        the last known position to prepare for the next drawing action.
        """

        # Reset the last position
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        """
        Clear all drawings from the canvas.

        This method removes all drawn elements from the canvas, effectively
        clearing the drawing surface.
        """
        self.view.clear_canvas()

    def activate_eraser(self, eraser_is_active: bool):
        """Activate eraser mode and set color to canvas background."""
        self.pen.setColor(QColor(CANVAS_BG) if eraser_is_active else self.model.get_brush_color())
        self.view.set_eraser_mode(True if eraser_is_active else False)
        self.view.draw_brush_preview(self.model.get_brush_size(),
                                     self.model.get_brush_color())

    def change_brush_color(self, color: str):
        self.pen.setColor(QColor(color))
        self.update_rgb_sliders(color)
        self.model.set_brush_color(color)
        brush_size = self.model.get_brush_size()
        # Update the preview
        self.view.draw_brush_preview(brush_size, color)
        # Update the brush size slider's look
        self.view.update_slider_accent_color(color)

    def change_brush_size(self, size: int):
        self.pen.setWidth(size)

        self.model.set_brush_size(size)
        brush_color = self.model.get_brush_color()
        self.view.draw_brush_preview(size, brush_color)

    def update_rgb_sliders(self, hex_color: str):
        self.model.set_brush_color(hex_color)
        rgb = self.model.convert_hex_to_rgb(hex_color)
        self.view.update_rgb_sliders(rgb.red, rgb.green, rgb.blue)

    def rgb_slider_moved(self):
        hex_color = self.model.convert_rgb_to_hex(*self.view.get_rgb_sliders_values())
        self.change_brush_color(hex_color)
