from typing import NamedTuple

from settings import *


class RgbColor(NamedTuple):
    red: int
    green: int
    blue: int


class PaintModel:
    def __init__(self):
        self.brush_color = None
        self.brush_size = None

    def set_brush_color(self, color: str):
        self.brush_color = color

    def get_brush_color(self) -> str:
        return self.brush_color

    def set_brush_size(self, size: int):
        self.brush_size = size

    def get_brush_size(self) -> int:
        return self.brush_size

    @staticmethod
    def convert_hex_to_rgb(color: str) -> RgbColor:
        if '#' in color:
            # Remove the hash sign at the beginning
            color = color[1:]
        red = COLOR_RANGE.index(color[0])
        green = COLOR_RANGE.index(color[1])
        blue = COLOR_RANGE.index(color[2])
        return RgbColor(red, green, blue)

    @staticmethod
    def convert_rgb_to_hex(red: int, green: int, blue: int) -> str:
        hex_color = f"#{COLOR_RANGE[red]}{COLOR_RANGE[green]}{COLOR_RANGE[blue]}"
        return hex_color
