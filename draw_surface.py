import customtkinter as ctk
import tkinter as tk
from settings import *


class DrawSurface(tk.Canvas):
    def __init__(self, parent):
        # Initialize the Canvas with specific settings
        super().__init__(master=parent,
                         bg=CANVS_BG,
                         borderwidth=0,
                         highlightthickness=0)

        # Initialize drawing parameters
        self.drawing = False
        self.color = "black"
        self.brush_size = 5

        # Variables to store the last mouse position
        self.last_x = None
        self.last_y = None

        # Bind mouse events to corresponding methods
        self.bind('<Button-1>', self.start_drawing)
        self.bind('<B1-Motion>', self.draw)
        self.bind('<ButtonRelease-1>', self.stop_drawing)

    def start_drawing(self, event):
        self.drawing = True
        # Draw a tiny line to create a dot at the starting point
        self.draw_line(event.x, event.y, event.x + 1, event.y + 1)

    def draw(self, event):
        if self.drawing:
            if self.last_x and self.last_y:
                # Draw a line from the last position to the current position
                self.draw_line(self.last_x, self.last_y, event.x, event.y)
            # Update the last position
            self.last_x = event.x
            self.last_y = event.y

    def draw_line(self, x1, y1, x2, y2):
        brush_size = self.brush_size
        color = self.color
        # Create a line between two points
        self.create_line(x1, y1, x2, y2, fill=color, width=brush_size, capstyle='round')

    def stop_drawing(self, event):
        self.drawing = False
        # Reset the last position

        self.last_x = None
        self.last_y = None
