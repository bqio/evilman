from __future__ import annotations
from typing import TYPE_CHECKING, Callable, List

if TYPE_CHECKING:
    from pygame.surface import Surface

from pygame.math import Vector2
from pygame.font import SysFont
from common.colors import WHITE_COLOR, RED_COLOR


class MenuItem:
    def __init__(self, title: str, action: Callable) -> None:
        self.title = title
        self.action = action


class Menu:
    def __init__(self) -> None:
        self.items: List[MenuItem] = []
        self.current_index = 0
        self.font = SysFont("Arial", 32)

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def up(self) -> None:
        if self.current_index == 0:
            self.current_index = len(self.items) - 1
        else:
            self.current_index -= 1

    def down(self) -> None:
        if self.current_index == len(self.items) - 1:
            self.current_index = 0
        else:
            self.current_index += 1

    def select(self) -> None:
        self.items[self.current_index].action()

    def draw(self, surface: Surface) -> None:
        pos = Vector2(50, 65)
        for menu_index, menu_item in enumerate(self.items):
            color = RED_COLOR if menu_index == self.current_index else WHITE_COLOR
            surf = self.font.render(menu_item.title, True, color)
            surface.blit(surf, pos)
            pos.y += 50
