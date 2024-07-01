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

        DrawSurface(self).pack(fill='both', expand=True)
        ToolPanel(self)


if __name__ == '__main__':
    app = Paint()
    app.mainloop()
