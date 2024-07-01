import customtkinter as ctk
from settings import *
from PIL import Image


class ToolPanel(ctk.CTkToplevel):
    def __init__(self, parent, draw_surface, brush_size, color_string, brush_is_on):
        super().__init__(master=parent)
        self.brush_is_on = brush_is_on
        self.draw_surface = draw_surface
        self.brush_size_var = brush_size
        self.color_string = color_string
        # setting light mode
        ctk.set_appearance_mode('light')
        # window setup
        self.geometry('200x300+220+220')
        self.title('')
        self.attributes('-topmost', True)
        self.resizable(False, False)

        self.set_layout()

        self.color_slides = ColorSlides(self, self.color_string, brush_is_on)
        self.brush_preview = BrushPreview(self, self.brush_size_var, self.color_string, self.brush_is_on)
        ColorButtons(self, color_string, self.color_slides)
        BrushSizeSlider(self, self.brush_size_var)
        self.action_buttons = ActionButtons(self, self.draw_surface, self.brush_is_on, color_string)

    def set_layout(self):
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        self.rowconfigure(3, weight=1, uniform='a')

        self.columnconfigure(0, weight=1, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')


class ColorSlides(ctk.CTkFrame):
    def __init__(self, parent, color_string, brush_is_on):
        super().__init__(master=parent)
        self.grid(row=0, column=0, padx=(5, 30))
        self.color_string = color_string
        self.brush_is_on = brush_is_on
        self.parent = parent
        self.red_var = ctk.IntVar()
        self.green_var = ctk.IntVar()
        self.blue_var = ctk.IntVar()

        self.red_slider = ctk.CTkSlider(self,
                                        button_color=SLIDER_RED,
                                        hover=False,
                                        from_=0,
                                        to=15,
                                        variable=self.red_var,
                                        command=self.update_color)
        self.red_slider.pack(pady=5)

        self.green_slider = ctk.CTkSlider(self,
                                          button_color=SLIDER_GREEN,
                                          hover=False,
                                          from_=0,
                                          to=15,
                                          variable=self.green_var,
                                          command=self.update_color)
        self.green_slider.pack(pady=5)

        self.blue_slider = ctk.CTkSlider(self,
                                         button_color=SLIDER_BLUE,
                                         hover=False,
                                         from_=0,
                                         to=15,
                                         variable=self.blue_var,
                                         command=self.update_color)
        self.blue_slider.pack(pady=5)

    def update_color(self, *args):
        self.parent.action_buttons.activate_brush()
        red = COLOR_RANGE[int(self.red_slider.get())]
        green = COLOR_RANGE[int(self.green_slider.get())]
        blue = COLOR_RANGE[int(self.blue_slider.get())]

        color = f'#{red}{green}{blue}'
        self.color_string.set(color)


class BrushPreview(ctk.CTkCanvas):
    def __init__(self, parent, brush_size_var, color_string, brush_is_on):
        super().__init__(master=parent,
                         width=90,
                         height=75,
                         bg=BRUSH_PREVIEW_BG,
                         borderwidth=0,
                         highlightthickness=0)
        self.grid(row=0, column=1, sticky='w')
        self.color_string = color_string
        self.brush_size_var = brush_size_var
        self.brush_is_on = brush_is_on

        self.draw_circle()

    def draw_circle(self, *args):
        if self.brush_is_on.get():
            color = self.color_string.get()
            width=0
        else:
            color = BRUSH_PREVIEW_BG
            width=1

        self.delete('all')
        r = int(self.brush_size_var.get() * 0.7 // 2)
        x = 35
        y = 35
        self.create_oval(x - r, y - r, x + r, y + r, width=width, fill=color)


class ColorButtons(ctk.CTkFrame):
    def __init__(self, parent, color_string, color_slides):
        super().__init__(master=parent)
        self.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.color_string = color_string
        self.color_slides = color_slides
        self.parent = parent
        # Create layout
        self.create_layout()
        self.create_buttons()

    def create_layout(self):
        self.columnconfigure(tuple(range(4)), weight=1, uniform='a')
        self.rowconfigure(tuple(range(6)), weight=1, uniform='b')

    def create_buttons(self):
        for row in range(COLOR_ROWS):
            for col in range(COLOR_COLS):
                button_color = f'#{COLORS[row][col]}'
                ctk.CTkButton(self,
                              text='',
                              fg_color=button_color,
                              hover=False,
                              corner_radius=0,
                              command=lambda e=button_color: self.change_color(e)).grid(row=row,
                                                                                        column=col,
                                                                                        sticky='news')

    def change_color(self, color):
        self.parent.action_buttons.activate_brush()

        self.color_string.set(color)

        red = COLOR_RANGE.index(color[1])
        green = COLOR_RANGE.index(color[2])
        blue = COLOR_RANGE.index(color[3])

        self.color_slides.red_var.set(red)
        self.color_slides.green_var.set(green)
        self.color_slides.blue_var.set(blue)


class BrushSizeSlider(ctk.CTkFrame):
    def __init__(self, parent, brush_size):
        super().__init__(master=parent)
        self.brush_size = brush_size

        self.grid(row=2, column=0, columnspan=2, sticky='news', padx=5, pady=5)
        self.brush_size_slider = ctk.CTkSlider(self,
                                               variable=self.brush_size,
                                               from_=20,
                                               to=100
                                               )
        self.brush_size_slider.pack(expand=True)


class ActionButtons(ctk.CTkFrame):
    def __init__(self, parent, draw_surface, brush_is_on, color_string):
        super().__init__(master=parent, fg_color='transparent')
        self.draw_surface = draw_surface
        self.brush_is_on = brush_is_on
        self.color_string = color_string
        self.last_color = None

        self.grid(row=3, column=0, columnspan=2, sticky='news', padx=5, pady=5)

        # Images
        brush_img = ctk.CTkImage(Image.open('images/brush.png'))
        clear_img = ctk.CTkImage(Image.open('images/clear.png'))
        eraser_img = ctk.CTkImage(Image.open('images/eraser.png'))

        self.brush_btn = ctk.CTkButton(self, text='', image=brush_img, fg_color=BUTTON_ACTIVE_COLOR,
                                       hover_color=BUTTON_HOVER_COLOR,
                                       width=55,
                                       command=self.activate_brush)
        self.brush_btn.pack(side='left', padx=(0, 5))

        self.eraser_button = ctk.CTkButton(self, text='', image=eraser_img, fg_color=BUTTON_COLOR,
                                           hover_color=BUTTON_HOVER_COLOR,
                                           width=55,
                                           command=self.activate_eraser)
        self.eraser_button.pack(side='left', padx=5)

        ctk.CTkButton(self,
                      text='',
                      image=clear_img,
                      fg_color=BUTTON_COLOR,
                      hover_color=BUTTON_HOVER_COLOR,
                      width=55,
                      command=self.clear_canvas).pack(side='right', padx=(5, 0), )

    def activate_brush(self):
        if self.last_color:
            self.brush_is_on.set(True)
            self.color_string.set(self.last_color)
        if not self.brush_is_on.get():
            self.brush_is_on.set(True)
        self.brush_btn.configure(fg_color=BUTTON_ACTIVE_COLOR)
        self.eraser_button.configure(fg_color=BUTTON_COLOR)

    def activate_eraser(self):
        if self.brush_is_on.get():
            self.brush_is_on.set(False)
            self.eraser_button.configure(fg_color=BUTTON_ACTIVE_COLOR)
            self.brush_btn.configure(fg_color=BUTTON_COLOR)
            self.last_color = self.color_string.get()
            self.color_string.set(CANVAS_BG)

    def clear_canvas(self):
        self.draw_surface.clear_screen()
        self.activate_brush()
