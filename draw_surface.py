import customtkinter as ctk
from settings import *


class DrawSurface(ctk.CTkCanvas):
    """
    A custom canvas widget for drawing in the paint application.

    This class extends CTkCanvas to create a drawing surface that responds to
    mouse events for drawing. It manages the drawing state and handles the
    creation of lines based on mouse movements.
    """
    def __init__(self, parent, brush_size_var, color_string):
        # Initialize the Canvas with specific settings
        super().__init__(master=parent,
                         bg=CANVAS_BG,
                         borderwidth=0,
                         highlightthickness=0,
                         )

        self.brush_size_var = brush_size_var
        self.color_string = color_string

        self.pack(fill='both', expand=True)

        # Variables to store the last mouse position
        self.last_x = None
        self.last_y = None

        # Bind mouse events to corresponding methods
        self.bind('<Button-1>', self.start_drawing)
        self.bind('<B1-Motion>', self.draw)
        self.bind('<ButtonRelease-1>', self.stop_drawing)

        # Bind custom event to the clear_screen function
        self.bind_all('<<ClearCanvas>>', self.clear_screen)

    def draw_line(self, x1, y1, x2, y2):
        """
        Draw a line between two points.

        Args:
            x1 (int): The x-coordinate of the start point.
            y1 (int): The y-coordinate of the start point.
            x2 (int): The x-coordinate of the end point.
            y2 (int): The y-coordinate of the end point.

        This method creates a line on the canvas between the specified points
        using the current brush size and color.
        """

        brush_size = self.brush_size_var.get()
        color = self.color_string.get()
        # Create a line between two points
        self.create_line(x1, y1, x2, y2, fill=color, width=brush_size, capstyle='round')

    def start_drawing(self, event):
        """
        Handle the start of a drawing action.

        Args:
            event: The mouse event that triggered the start of drawing.

        This method is called when the mouse button is pressed. It starts
        the drawing by creating a small line at the mouse position.
        """

        # Draw a tiny line to create a dot at the starting point
        self.draw_line(event.x, event.y, event.x + 1, event.y + 1)

    def draw(self, event):
        """
        Handle the drawing action as the mouse moves.

        Args:
            event: The mouse event containing the current mouse position.

        This method is called when the mouse moves while the button is pressed.
        It continues the drawing by creating lines between the last known
        position and the current mouse position.
        """

        if self.last_x and self.last_y:
            # Draw a line from the last position to the current position
            self.draw_line(self.last_x, self.last_y, event.x, event.y)
        # Update the last position
        self.last_x = event.x
        self.last_y = event.y

    def stop_drawing(self, event=None):
        """
        Handle the end of a drawing action.

        Args:
            event: The mouse event that triggered the end of drawing (optional).

        This method is called when the mouse button is released. It resets
        the last known position to prepare for the next drawing action.
        """
        # Reset the last position
        self.last_x = None
        self.last_y = None

    def clear_screen(self, event=None):
        """
        Clear all drawings from the canvas.

        Args:
            event: The event that triggered the clear action (optional).

        This method removes all drawn elements from the canvas, effectively
        clearing the drawing surface.
        """

        self.delete('all')
