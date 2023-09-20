from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game import Game

from pygame import QUIT
from pygame.time import Clock
from pygame.event import get
from common.constants import DISPLAY_FPS
from common.abs.game_object import GameObject


class EventManager(GameObject):
    def __init__(self, parent: Game) -> None:
        super().__init__(parent)

        self.clock = Clock()
        self.is_running = True

    def loop(self) -> None:
        while self.is_running:
            self.clock.tick(DISPLAY_FPS)
            state = self.parent.state_manager.get_state()
            for event in get():
                if event.type == QUIT:
                    self.quit()
                state.on_event(event)
            self.parent.display_manager.clear()
            state.on_draw(self.parent.display_manager.get_surface())
            state.on_update()
            self.parent.display_manager.update()

    def quit(self) -> None:
        self.is_running = False
