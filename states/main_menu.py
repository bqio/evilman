from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from core.game import Game

from common.abs.state import State
from core.menu import Menu, MenuItem
from pygame import K_UP, K_DOWN, KEYUP, K_RETURN


class MainMenuState(State):
    def __init__(self, parent: Game) -> None:
        super().__init__(parent)

        self.menu = Menu()
        self.menu.add_item(MenuItem("New Game", self.on_new_game_selected))
        self.menu.add_item(MenuItem("Load Game", self.on_load_game_selected))
        self.menu.add_item(MenuItem("Settings", self.on_settings_selected))
        self.menu.add_item(MenuItem("Exit", self.on_exit_selected))

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

    def on_new_game_selected(self) -> None:
        pass

    def on_load_game_selected(self) -> None:
        pass

    def on_settings_selected(self) -> None:
        self.parent.state_manager.set_state(1)

    def on_exit_selected(self) -> None:
        self.parent.event_manager.quit()
