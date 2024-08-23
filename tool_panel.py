import customtkinter as ctk
from settings import *
from PIL import Image


class ToolPanel(ctk.CTkToplevel):
    """
    A custom top-level window that serves as the tool panel for the paint application.

    This class creates a separate window containing various controls for the paint
    application, including color selection, brush size adjustment, and action buttons.

    This panel provides all the necessary controls for the user to interact with
    the paint application, separate from the main drawing area.
    """
    def __init__(self, parent, brush_size, color_string, is_brush_active):
        super().__init__(master=parent)
        self.parent = parent

        # Force light theme
        ctk.set_appearance_mode('light')

        # window setup
        self.geometry('200x350+1020+200')
        self.title('')
        self.attributes('-topmost', True)  # Make it always on top
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
        """
        Configure the grid layout for the tool panel.
        """

        self.rowconfigure(0, weight=2, uniform='a')
        self.rowconfigure(1, weight=3, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        self.rowconfigure(3, weight=1, uniform='a')

        self.columnconfigure(0, weight=1, uniform='b')
        self.columnconfigure(1, weight=1, uniform='b')


class ColorSlides(ctk.CTkFrame):
    """
    A custom frame containing sliders for adjusting RGB color values.

    This class creates a set of three sliders that allow fine-tuning of the
    red, green, and blue components of the brush color in the paint application.

    The ColorSlides class provides an intuitive interface for users to adjust
    the brush color by manipulating individual RGB components. Each slider
    corresponds to one of the RGB channels and updates the color in real-time
    as the user interacts with it.
    """
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
        """
        Create and configure the color sliders.

        This method creates three CTkSlider widgets, one for each RGB component.
        Each slider is configured with appropriate colors and ranges, and is
        linked to its corresponding color variable. The sliders are then packed
        into the frame.
        """

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

    def update_color(self, *args) -> None:
        """
        Update the color based on the current slider values.

        Args:
            *args: Variable length argument list (not used, but required for Tkinter variable tracing).

        This method is called whenever one of the sliders is adjusted. It reads the
        current values of the red, green, and blue sliders, converts them to a
        hexadecimal color string, and updates the color_string variable.
        It also generates an event to activate the brush if it's not already active.
        """

        # Generate an event that will activate brush
        self.event_generate('<<activate_brush>>')

        # Convert decimal number that is taken from sliders
        # to HexaDecimal equivalent
        red: str = COLOR_RANGE[int(self.red_var.get())]
        green: str = COLOR_RANGE[int(self.green_var.get())]
        blue: str = COLOR_RANGE[int(self.blue_var.get())]

        color: str = f'#{red}{green}{blue}'
        self.color_string.set(color)


class BrushPreview(ctk.CTkCanvas):
    """
    A custom canvas widget that provides a visual preview of the current brush.

    This class creates a small canvas that displays a circle representing the
    current brush size and color. It updates in real-time as the user adjusts
    the brush settings in the paint application.
    """
    def __init__(self, parent, brush_size_var, color_string, brush_is_on):
        # Initialize the canvas with specific dimensions and appearance
        super().__init__(master=parent,
                         width=100,
                         height=100,
                         bg=BRUSH_PREVIEW_BG,
                         borderwidth=0,
                         highlightthickness=0)

        # Store references to the brush properties
        self.color_string = color_string
        self.brush_size_var = brush_size_var
        self.brush_is_on = brush_is_on

        # Position the preview canvas in the parent widget
        self.grid(row=0, column=1, sticky='w')

        # Bind the brush size and color variables to the update method
        # This ensures the preview updates when these values change
        self.brush_size_var.trace('w', self.draw_preview_circle)
        self.color_string.trace('w', self.draw_preview_circle)

        # Calculate the center coordinates of the canvas
        self.x = 100 // 2
        self.y = 100 // 2

        # Initial draw of the preview circle
        self.draw_preview_circle()

    def draw_preview_circle(self, *args) -> None:
        """
        Draw or update the preview circle on the canvas.

        Args:
            *args: Variable length argument list (not used, but required for Tkinter variable tracing).

        This method clears the canvas and draws a new circle representing the
        current brush. The circle's size corresponds to the brush size, and its
        color matches the current brush color. If the eraser is active, the circle
        is drawn as an outline instead of a filled circle.

        The method is called automatically whenever the brush size, color, or
        active tool (brush/eraser) changes.
        """
        # Determine the color and outline based on whether brush or eraser is active
        if self.brush_is_on.get():
            color: str = self.color_string.get()
            width: int = 0  # Filled circle for brush
        else:
            color: str = BRUSH_PREVIEW_BG
            width: int = 1  # Outline for eraser

        # Clear the canvas
        self.delete('all')

        # Calculate the radius based on the current brush size
        radius = int(self.brush_size_var.get() // 2)
        # Draw the circle
        self.create_oval(self.x - radius, self.y - radius, self.x + radius, self.y + radius, width=width, fill=color)


class ColorButtons(ctk.CTkFrame):
    """
    A custom frame containing a set of color selection buttons.

    This class creates a grid of buttons, each representing a predefined color.
    It allows users to quickly select common colors for their brush in the paint application.

    The ColorButtons class provides a user-friendly interface for quick color selection,
    complementing the more precise color adjustment offered by the ColorSlides class.
    When a color button is clicked, it updates both the color_string and the individual
    RGB variables, ensuring consistency across the application.
    """
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
        """
        Create and arrange the color selection buttons.

        This method creates a button for each color in the predefined color list.
        The buttons are arranged in a grid layout within the frame. Each button
        is configured with its respective color and bound to the change_color method.
        """

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
        Set the selected color as the current brush color.

        Args:
            color (str): The selected color in hex format.

        This method updates the color_string variable with the selected color.
        It also updates the individual RGB variables by converting the hex color
        to RGB values. This ensures that all color-related components of the
        application are synchronized when a new color is selected.
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
    """
    A custom frame containing a slider for adjusting the brush size.

    This class creates a slider that allows users to change the size of the brush
    or eraser in the paint application.
    """
    def __init__(self, parent, brush_size):
        super().__init__(master=parent)

        self.grid(row=2, column=0, columnspan=2, sticky='news', padx=5, pady=5)
        ctk.CTkSlider(self,
                      variable=brush_size,
                      from_=20,
                      to=100
                      ).pack(expand=True)


class ActionButtons(ctk.CTkFrame):
    """
    A custom frame containing action buttons for brush, eraser, and canvas clearing.

    This class creates a set of buttons that allow users to switch between brush and eraser modes,
    and to clear the canvas in the paint application.
    """
    def __init__(self, parent, is_brush_active, color_string):
        super().__init__(master=parent, fg_color='transparent')
        self.parent = parent
        self.is_brush_active = is_brush_active
        self.color_string = color_string
        self.last_color: None | str = None  # Last used color
        self.parent.bind('<<activate_brush>>', lambda e: self.activate_brush())

        self.grid(row=3, column=0, columnspan=2, sticky='news', padx=5, pady=5)

        # Create brush button
        self.brush_btn = Button(self, image='images/brush.png',
                                command=self.activate_brush)
        self.brush_btn.pack(side='left', padx=(0, 5))

        # Create eraser button
        self.eraser_button = Button(self, image='images/eraser.png',
                                    command=self.activate_eraser)
        self.eraser_button.pack(side='left', padx=5)

        # Create clear canvas button
        Button(self, image='images/clear.png', command=self.clear_canvas).pack(side='right', padx=(5, 0))

        # Activate brush on first run
        self.activate_brush()

    def activate_brush(self):
        """Activate brush mode and restore last used color."""
        self.is_brush_active.set(True)
        # If there's already a saved color, use that
        if self.last_color:
            self.color_string.set(self.last_color)
        # Change the brush button color to active
        self.mark_as_active()

    def activate_eraser(self):
        """Activate eraser mode and set color to canvas background."""
        self.is_brush_active.set(False)
        # Change the eraser button color to active color
        self.mark_as_active()
        # Save the color
        self.last_color = self.color_string.get()
        # Change the brush color to the background color
        self.color_string.set(CANVAS_BG)

    def clear_canvas(self):
        """Clear the canvas and activate brush mode."""
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
    """
    A custom button class that extends CTkButton with predefined styling and image support.
    """
    def __init__(self, parent, image, **kwargs):
        button_img = ctk.CTkImage(Image.open(image))
        super().__init__(master=parent,
                         text='',
                         image=button_img,
                         fg_color=BUTTON_COLOR,
                         hover_color=BUTTON_HOVER_COLOR,
                         width=55,
                         **kwargs)
