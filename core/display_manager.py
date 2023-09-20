from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game import Game
    from pygame.surface import Surface

from pygame.display import set_caption, set_mode, get_surface, update
from common.constants import DISPLAY_CAPTION, DISPLAY_SIZE
from common.colors import BLACK_COLOR
from common.abs.game_object import GameObject


class DisplayManager(GameObject):
    def __init__(self, parent: Game) -> None:
        super().__init__(parent)

        set_caption(DISPLAY_CAPTION)
        set_mode(DISPLAY_SIZE)

    def clear(self) -> None:
        get_surface().fill(BLACK_COLOR)

    def update(self) -> None:
        update()

    def get_surface(self) -> Surface:
        return get_surface()
