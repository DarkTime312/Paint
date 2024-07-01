import customtkinter as ctk
from draw_surface import DrawSurface
from tool_panel import ToolPanel


class Paint(ctk.CTk):
    def __init__(self):
        super().__init__()

        # setting light mode
        ctk.set_appearance_mode('light')
        # window setup
        self.geometry('800x600+200+200')
        self.title('')
        self.iconbitmap('empty.ico')

        # variables
        self.brush_size_var = ctk.IntVar(value=20)
        self.color_string = ctk.StringVar(value='#000')
        self.brush_is_on = ctk.BooleanVar(value=True)

        self.bind('<MouseWheel>', self.change_brush_size)

        self.draw_surface = DrawSurface(self, self.brush_size_var, self.color_string)
        self.tool_panel = ToolPanel(self, self.draw_surface, self.brush_size_var, self.color_string, self.brush_is_on)

        self.brush_size_var.trace('w', self.tool_panel.brush_preview.draw_circle)
        self.color_string.trace('w', self.tool_panel.brush_preview.draw_circle)

    def change_brush_size(self, event):
        if event.delta > 0:
            self.brush_size_var.set(self.brush_size_var.get() + 5)
        else:
            self.brush_size_var.set(self.brush_size_var.get() - 5)


if __name__ == '__main__':
    app = Paint()
    app.mainloop()
