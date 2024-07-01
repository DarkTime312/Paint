import customtkinter as ctk
from settings import *

class ToolPanel(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(master=parent)

        # setting light mode
        ctk.set_appearance_mode('light')
        # window setup
        self.geometry('200x300+220+220')
        self.title('')
        self.attributes('-topmost', True)
        self.resizable(False, False)
        # self.configure(padx=50, pady=50)

        self.set_layout()
        ColorSlides(self)
        BrushPreview(self)

    def set_layout(self):
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        self.rowconfigure(3, weight=1, uniform='a')

        self.columnconfigure(0, weight=1, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')

        # debug labels

        ctk.CTkLabel(self, text='', bg_color='yellow').grid(row=1, column=0, sticky='news')
        ctk.CTkLabel(self, text='', bg_color='purple').grid(row=1, column=1, sticky='news')

        ctk.CTkLabel(self, text='', bg_color='green').grid(row=2, column=0, sticky='news')
        ctk.CTkLabel(self, text='', bg_color='black').grid(row=2, column=1, sticky='news')

        ctk.CTkLabel(self, text='', bg_color='brown').grid(row=3, column=0, sticky='news')
        ctk.CTkLabel(self, text='', bg_color='cyan').grid(row=3, column=1, sticky='news')


class ColorSlides(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=0, padx=(5, 30))

        ctk.CTkSlider(self, button_color=SLIDER_RED, hover=False).pack(pady=5)
        ctk.CTkSlider(self, button_color=SLIDER_GREEN, hover=False).pack(pady=5)
        ctk.CTkSlider(self, button_color=SLIDER_BLUE, hover=False).pack(pady=5)


class BrushPreview(ctk.CTkCanvas):
    def __init__(self, parent):
        super().__init__(master=parent,
                         width=90,
                         height=75,
                         bg=BRUSH_PREVIEW_BG,
                         borderwidth=0,
                         highlightthickness=0)
        self.grid(row=0, column=1, sticky='w')

        self.draw_circle(35, 35, 35, width=0, fill="black")

        # delete later
    def draw_circle(self, x, y, r, **kwargs):
        self.create_oval(x - r, y - r, x + r, y + r, **kwargs)
