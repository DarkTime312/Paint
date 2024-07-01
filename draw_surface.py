import customtkinter as ctk
import tkinter as tk
from settings import *


class DrawSurface(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent,
                         bg=CANVS_BG,
                         borderwidth=0,
                         highlightthickness=0)
