import customtkinter as ctk
from draw_surface import DrawSurface
from tool_panel import ToolPanel


class Paint(ctk.CTk):
    """
    A paint application built with CustomTkinter.

    This class represents the main window of the paint application. It initializes
    the drawing surface and the tool panel, and manages the overall application state.
    """
    def __init__(self):
        super().__init__()

        # Force light theme
        ctk.set_appearance_mode('light')

        # window setup
        self.geometry('800x600+200+200')
        self.title('')
        self.iconbitmap('empty.ico')

        # Variable to store and manage the brush size.
        self.brush_size_var = ctk.IntVar(value=100)
        # Variable to store and manage the current color.
        self.color_string = ctk.StringVar(value='#000')
        # Variable to track whether the brush or eraser is active.
        self.is_brush_active = ctk.BooleanVar(value=True)

        # Bind the mouse wheel to the brush size slider
        self.bind('<MouseWheel>', self.change_brush_size)

        DrawSurface(self,
                    self.brush_size_var,
                    self.color_string)

        ToolPanel(self,
                  self.brush_size_var,
                  self.color_string,
                  self.is_brush_active)

    def change_brush_size(self, event):
        """
        Adjust the brush size based on mouse wheel scrolling.

        This method is called when the mouse wheel is scrolled. It increases or
        decreases the brush size within the range of 20 to 100 pixels.

        Args:
            event: The mouse wheel event containing the scroll direction.

        The brush size is increased by 5 when scrolling up and decreased by 5
        when scrolling down, always staying within the 20-100 pixel range.
        """

        current_size = self.brush_size_var.get()

        if event.delta > 0:
            self.brush_size_var.set(min(100, current_size + 5))
        else:
            self.brush_size_var.set(max(20, current_size - 5))


if __name__ == '__main__':
    app = Paint()
    app.mainloop()
