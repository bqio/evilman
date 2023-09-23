from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from pygame.key import ScancodeWrapper

from scenes import BaseScene, SceneLoader
from core.menu import Menu, MenuItem


class MainMenuScene(BaseScene, SceneLoader):
    def __init__(self) -> None:
        BaseScene.__init__(self)

    def awake(self) -> None:
        print("[Awake]:", "MainMenu")
        self.menu = Menu()
        self.menu.add_item(MenuItem("New Game", self.on_new_game_selected))
        self.menu.add_item(MenuItem("Load Game", self.on_load_game_selected))
        self.menu.add_item(MenuItem("Settings", self.on_settings_selected))
        self.menu.add_item(MenuItem("Exit", self.on_exit_selected))

    def update(self) -> None:
        return super().update()

    def render(self, screen: Surface) -> None:
        self.menu.on_draw(screen)

    def process(self, events: list[Event], pressed_keys: ScancodeWrapper) -> None:
        for event in events:
            self.menu.on_event(event)

    def destroy(self) -> None:
        print("[Destroy]:", "MainMenu")

    def on_new_game_selected(self) -> None:
        pass

    def on_load_game_selected(self) -> None:
        pass

    def on_settings_selected(self) -> None:
        SceneLoader.switch_to("SettingsMenuScene")

    def on_exit_selected(self) -> None:
        SceneLoader.switch_to(None)
