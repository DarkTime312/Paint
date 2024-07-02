import customtkinter as ctk
from settings import *
from PIL import Image


class ToolPanel(ctk.CTkToplevel):
    def __init__(self, parent, brush_size, color_string, is_brush_active):
        super().__init__(master=parent)
        self.parent = parent

        # window setup
        self.geometry('200x300+1020+200')
        self.title('')
        self.attributes('-topmost', True)
        self.resizable(False, False)

        # A binding to close the main app if the ToolPanel is closed
        self.bind("<Destroy>", lambda e: self.quit())

        # setting light mode
        ctk.set_appearance_mode('light')

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
        self.event_generate('<<activate_brush>>')
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
        self.color_string = color_string
        self.brush_size_var = brush_size_var
        self.brush_is_on = brush_is_on

        self.grid(row=0, column=1, sticky='w')

        self.brush_size_var.trace('w', self.draw_circle)
        self.color_string.trace('w', self.draw_circle)

        self.draw_circle()

    def draw_circle(self, *args):
        if self.brush_is_on.get():
            color = self.color_string.get()
            width = 0
        else:
            color = BRUSH_PREVIEW_BG
            width = 1

        self.delete('all')
        r = int(self.brush_size_var.get() * 0.7 // 2)
        # x and y for center of oval
        x, y = 35, 35
        self.create_oval(x - r, y - r, x + r, y + r, width=width, fill=color)


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
                              command=lambda color=button_color: self.change_color(color)).grid(row=row,
                                                                                                column=col,
                                                                                                sticky='news')

    def change_color(self, color):
        self.event_generate('<<activate_brush>>')
        self.color_string.set(color)

        red = COLOR_RANGE.index(color[1])
        green = COLOR_RANGE.index(color[2])
        blue = COLOR_RANGE.index(color[3])

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
        self.last_color = None
        self.parent.bind('<<activate_brush>>', lambda e: self.activate_brush())

        self.grid(row=3, column=0, columnspan=2, sticky='news', padx=5, pady=5)

        # Images
        brush_img = ctk.CTkImage(Image.open('images/brush.png'))
        clear_img = ctk.CTkImage(Image.open('images/clear.png'))
        eraser_img = ctk.CTkImage(Image.open('images/eraser.png'))

        self.brush_btn = ctk.CTkButton(self,
                                       text='',
                                       image=brush_img,
                                       fg_color=BUTTON_ACTIVE_COLOR,
                                       hover_color=BUTTON_HOVER_COLOR,
                                       width=55,
                                       command=self.activate_brush)
        self.brush_btn.pack(side='left', padx=(0, 5))

        self.eraser_button = ctk.CTkButton(self,
                                           text='',
                                           image=eraser_img,
                                           fg_color=BUTTON_COLOR,
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
                      command=self.clear_canvas).pack(side='right', padx=(5, 0))

    def activate_brush(self):
        self.is_brush_active.set(True)
        # If there's already a saved color, activate it
        if self.last_color:
            self.color_string.set(self.last_color)
        # Change the brush button color to active
        self.brush_btn.configure(fg_color=BUTTON_ACTIVE_COLOR)
        # Change the eraser button color to not active
        self.eraser_button.configure(fg_color=BUTTON_COLOR)

    def activate_eraser(self):
        self.is_brush_active.set(False)
        # Change the eraser button color to active color
        self.eraser_button.configure(fg_color=BUTTON_ACTIVE_COLOR)
        # Change the brush button color to not active color
        self.brush_btn.configure(fg_color=BUTTON_COLOR)
        # Save the color
        self.last_color = self.color_string.get()
        # Change the brush color to the background color
        self.color_string.set(CANVAS_BG)

    def clear_canvas(self):
        # Generate an event that will clear the canvas
        self.event_generate('<<ClearCanvas>>')
        # Set the brush as active
        self.activate_brush()
