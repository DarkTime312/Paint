import customtkinter as ctk
from settings import *


class DrawSurface(ctk.CTkCanvas):
    def __init__(self, parent, brush_size_var, color_string):
        # Initialize the Canvas with specific settings
        super().__init__(master=parent,
                         bg=CANVAS_BG,
                         borderwidth=0,
                         highlightthickness=0)

        self.parent = parent
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
        brush_size = self.brush_size_var.get()
        color = self.color_string.get()
        # Create a line between two points
        self.create_line(x1, y1, x2, y2, fill=color, width=brush_size, capstyle='round')

    def start_drawing(self, event):
        # Draw a tiny line to create a dot at the starting point
        self.draw_line(event.x, event.y, event.x + 1, event.y + 1)

    def draw(self, event):
        if self.last_x and self.last_y:
            # Draw a line from the last position to the current position
            self.draw_line(self.last_x, self.last_y, event.x, event.y)
        # Update the last position
        self.last_x = event.x
        self.last_y = event.y

    def stop_drawing(self, event=None):
        # Reset the last position
        self.last_x = None
        self.last_y = None

    def clear_screen(self, event=None):
        self.delete('all')
