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
        self.brush_size_var = ctk.IntVar(value=100)
        self.color_string = ctk.StringVar(value='#000')
        self.is_brush_active = ctk.BooleanVar(value=True)

        self.bind('<MouseWheel>', self.change_brush_size)

        DrawSurface(self,
                    self.brush_size_var,
                    self.color_string)

        ToolPanel(self,
                  self.brush_size_var,
                  self.color_string,
                  self.is_brush_active)

    def change_brush_size(self, event):
        current_size = self.brush_size_var.get()

        if event.delta > 0:
            self.brush_size_var.set(min(100, current_size + 5))
        else:
            self.brush_size_var.set(max(20, current_size - 5))


if __name__ == '__main__':
    app = Paint()
    app.mainloop()
