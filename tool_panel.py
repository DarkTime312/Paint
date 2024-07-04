import customtkinter as ctk
from settings import *
from PIL import Image


class ToolPanel(ctk.CTkToplevel):
    def __init__(self, parent, brush_size, color_string, is_brush_active):
        super().__init__(master=parent)
        self.parent = parent

        # Forcing light theme
        ctk.set_appearance_mode('light')

        # window setup
        self.geometry('200x300+1020+200')
        self.title('')
        self.attributes('-topmost', True)
        self.resizable(False, False)

        # Had to change the TopLevel icon with a delay because of a bug
        self.after(200, lambda: self.iconbitmap('empty.ico'))

        # A binding to close the main app if the ToolPanel is closed
        self.bind("<Destroy>", lambda e: self.quit())

        # Creating color variables
        self.red_var = ctk.IntVar()
        self.green_var = ctk.IntVar()
        self.blue_var = ctk.IntVar()

        self.set_layout()

        ColorSlides(self,
                    color_string,
                    self.red_var,
                    self.green_var,
                    self.blue_var)

        BrushPreview(self,
                     brush_size,
                     color_string,
                     is_brush_active)

        ColorButtons(self,
                     color_string,
                     self.red_var,
                     self.green_var,
                     self.blue_var)

        BrushSizeSlider(self,
                        brush_size)

        ActionButtons(self,
                      is_brush_active,
                      color_string)

    def set_layout(self):
        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        self.rowconfigure(3, weight=1, uniform='a')

        self.columnconfigure(0, weight=1, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')


class ColorSlides(ctk.CTkFrame):
    def __init__(self, parent, color_string, red_var, green_var, blue_var):
        super().__init__(master=parent)
        self.parent = parent
        self.color_string = color_string
        self.red_var = red_var
        self.green_var = green_var
        self.blue_var = blue_var

        self.grid(row=0, column=0, padx=(5, 30))

        self.create_widgets()

    def create_widgets(self):
        red_slider = ctk.CTkSlider(self,
                                   button_color=SLIDER_RED,
                                   hover=False,
                                   from_=0,
                                   to=15,
                                   variable=self.red_var,
                                   command=self.update_color)
        red_slider.pack(pady=5)

        green_slider = ctk.CTkSlider(self,
                                     button_color=SLIDER_GREEN,
                                     hover=False,
                                     from_=0,
                                     to=15,
                                     variable=self.green_var,
                                     command=self.update_color)
        green_slider.pack(pady=5)

        blue_slider = ctk.CTkSlider(self,
                                    button_color=SLIDER_BLUE,
                                    hover=False,
                                    from_=0,
                                    to=15,
                                    variable=self.blue_var,
                                    command=self.update_color)
        blue_slider.pack(pady=5)

    def update_color(self, *args):
        # Generate an event that will activate brush
        self.event_generate('<<activate_brush>>')

        red = COLOR_RANGE[int(self.red_var.get())]
        green = COLOR_RANGE[int(self.green_var.get())]
        blue = COLOR_RANGE[int(self.blue_var.get())]

        color = f'#{red}{green}{blue}'
        self.color_string.set(color)


class BrushPreview(ctk.CTkCanvas):
    def __init__(self, parent, brush_size_var, color_string, brush_is_on):
        super().__init__(master=parent,
                         width=90,
                         height=90,
                         bg=BRUSH_PREVIEW_BG,
                         borderwidth=0,
                         highlightthickness=0)

        self.color_string = color_string
        self.brush_size_var = brush_size_var
        self.brush_is_on = brush_is_on

        self.grid(row=0, column=1, sticky='w')

        self.brush_size_var.trace('w', self.draw_preview_circle)
        self.color_string.trace('w', self.draw_preview_circle)

        # Finding the coordinates to center of the canvas
        self.x = 90 // 2
        self.y = 90 // 2
        self.max_length = 45

        self.draw_preview_circle()

    def draw_preview_circle(self, *args) -> None:
        if self.brush_is_on.get():
            color: str = self.color_string.get()
            width: int = 0
        else:
            color: str = BRUSH_PREVIEW_BG
            width: int = 1

        self.delete('all')
        radius = int(self.max_length * self.brush_size_var.get() / 100)
        self.create_oval(self.x - radius, self.y - radius, self.x + radius, self.y + radius, width=width, fill=color)


class ColorButtons(ctk.CTkFrame):
    def __init__(self, parent, color_string, red_var, green_var, blue_var):
        super().__init__(master=parent)
        self.color_string = color_string
        self.red_var = red_var
        self.green_var = green_var
        self.blue_var = blue_var

        self.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Create layout
        self.create_layout()
        self.create_buttons()

    def create_layout(self):
        self.columnconfigure(tuple(range(COLOR_COLS)), weight=1, uniform='a')
        self.rowconfigure(tuple(range(COLOR_ROWS)), weight=1, uniform='b')

    def create_buttons(self):
        for row in range(COLOR_ROWS):
            for col in range(COLOR_COLS):
                button_color: str = f'#{COLORS[row][col]}'
                ctk.CTkButton(self,
                              text='',
                              fg_color=button_color,
                              hover=False,
                              corner_radius=0,
                              command=lambda color=button_color: self.change_color(color)
                              ).grid(row=row,
                                     column=col,
                                     sticky='news',
                                     padx=0.4,
                                     pady=0.4)

    def change_color(self, color: str) -> None:
        """
        Changes the brush color to the selected color.
        It also updates the position of color sliders.

        :param color: a string that represents the color as hexadecimal
        :return: None
        """
        # Activates the brush if not selected
        self.event_generate('<<activate_brush>>')
        self.color_string.set(color)

        # Gets the decimal equivalent of each hexadecimal number
        # And uses it to update the sliders positions.
        red: int = int(color[1], 16)
        green: int = int(color[2], 16)
        blue: int = int(color[3], 16)

        self.red_var.set(red)
        self.green_var.set(green)
        self.blue_var.set(blue)


class BrushSizeSlider(ctk.CTkFrame):
    def __init__(self, parent, brush_size):
        super().__init__(master=parent)

        self.grid(row=2, column=0, columnspan=2, sticky='news', padx=5, pady=5)
        ctk.CTkSlider(self,
                      variable=brush_size,
                      from_=20,
                      to=100
                      ).pack(expand=True)


class ActionButtons(ctk.CTkFrame):
    def __init__(self, parent, is_brush_active, color_string):
        super().__init__(master=parent, fg_color='transparent')
        self.parent = parent
        self.is_brush_active = is_brush_active
        self.color_string = color_string
        self.last_color: None | str = None
        self.parent.bind('<<activate_brush>>', lambda e: self.activate_brush())

        self.grid(row=3, column=0, columnspan=2, sticky='news', padx=5, pady=5)

        self.brush_btn = Button(self, image='images/brush.png',
                                command=self.activate_brush)
        self.brush_btn.pack(side='left', padx=(0, 5))

        self.eraser_button = Button(self, image='images/eraser.png',
                                    command=self.activate_eraser)
        self.eraser_button.pack(side='left', padx=5)

        Button(self, image='images/brush.png', command=self.clear_canvas).pack(side='right', padx=(5, 0))

        # Activate brush on first run
        self.activate_brush()

    def activate_brush(self):
        self.is_brush_active.set(True)
        # If there's already a saved color, activate it
        if self.last_color:
            self.color_string.set(self.last_color)
        # Change the brush button color to active
        self.mark_as_active()

    def activate_eraser(self):
        self.is_brush_active.set(False)
        # Change the eraser button color to active color
        self.mark_as_active()
        # Save the color
        self.last_color = self.color_string.get()
        # Change the brush color to the background color
        self.color_string.set(CANVAS_BG)

    def clear_canvas(self):
        # Generate an event that will clear the canvas
        self.event_generate('<<ClearCanvas>>')
        # Set the brush as active
        self.activate_brush()

    def mark_as_active(self) -> None:
        """
        Changes the background of the active button
        to indicate that it's active.

        :return: None
        """
        # If brush is active
        if self.is_brush_active.get():
            active_btn = self.brush_btn
            deactive_btn = self.eraser_button
        # If eraser is active
        else:
            active_btn = self.eraser_button
            deactive_btn = self.brush_btn

        active_btn.configure(fg_color=BUTTON_ACTIVE_COLOR)
        deactive_btn.configure(fg_color=BUTTON_COLOR)


class Button(ctk.CTkButton):
    def __init__(self, parent, image, **kwargs):
        button_img = ctk.CTkImage(Image.open(image))
        super().__init__(master=parent,
                         text='',
                         image=button_img,
                         fg_color=BUTTON_COLOR,
                         hover_color=BUTTON_HOVER_COLOR,
                         width=55,
                         **kwargs)
