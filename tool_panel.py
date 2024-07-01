import customtkinter as ctk
from settings import *
from PIL import Image


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

        self.set_layout()

        ColorSlides(self)
        BrushPreview(self)
        ColorButtons(self)
        BrushSizeSlider(self)
        ActionButtons(self)

    def set_layout(self):
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        self.rowconfigure(3, weight=1, uniform='a')

        self.columnconfigure(0, weight=1, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')


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


class ColorButtons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Create layout
        self.create_layout()
        self.create_buttons()

    def create_layout(self):
        self.columnconfigure(tuple(range(4)), weight=1, uniform='a')
        self.rowconfigure(tuple(range(6)), weight=1, uniform='b')

    def create_buttons(self):
        for row in range(COLOR_ROWS):
            for col in range(COLOR_COLS):
                ctk.CTkButton(self, text='', fg_color=f'#{COLORS[row][col]}', corner_radius=0).grid(row=row,
                                                                                                    column=col,
                                                                                                    sticky='news')


class BrushSizeSlider(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        self.grid(row=2, column=0, columnspan=2, sticky='news', padx=5, pady=5)
        ctk.CTkSlider(self).pack(expand=True)


class ActionButtons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')

        self.grid(row=3, column=0, columnspan=2, sticky='news', padx=5, pady=5)

        # Images
        brush_img = ctk.CTkImage(Image.open('images/brush.png'))
        clear_img = ctk.CTkImage(Image.open('images/clear.png'))
        eraser_img = ctk.CTkImage(Image.open('images/eraser.png'))

        ctk.CTkButton(self, text='', image=brush_img, fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, width=55).pack(side='left', padx=(0, 5))
        ctk.CTkButton(self, text='', image=eraser_img, fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, width=55).pack(side='left', padx=5)
        ctk.CTkButton(self, text='', image=clear_img, fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, width=55).pack(side='right', padx=(5, 0))
