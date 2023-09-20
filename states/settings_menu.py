from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from core.game import Game

from common.abs.state import State
from core.menu import Menu, MenuItem
from pygame import K_UP, K_DOWN, KEYUP, K_RETURN


class SettigsMenuState(State):
    def __init__(self, parent: Game) -> None:
        super().__init__(parent)

        self.menu = Menu()
        self.menu.add_item(MenuItem("Game", self.on_game_selected))
        self.menu.add_item(MenuItem("Video", self.on_video_selected))
        self.menu.add_item(MenuItem("Audio", self.on_audio_selected))
        self.menu.add_item(MenuItem("Back", self.on_back_selected))

    def on_draw(self, surface: Surface) -> None:
        self.menu.draw(surface)

    def on_update(self) -> None:
        pass

    def on_event(self, event: Event) -> None:
        if event.type == KEYUP:
            if event.key == K_UP:
                self.menu.up()
            if event.key == K_DOWN:
                self.menu.down()
            if event.key == K_RETURN:
                self.menu.select()

    def on_game_selected(self) -> None:
        pass

    def on_video_selected(self) -> None:
        pass

    def on_audio_selected(self) -> None:
        pass

    def on_back_selected(self) -> None:
        self.parent.state_manager.set_state(0)
