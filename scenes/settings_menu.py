from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from pygame.key import ScancodeWrapper

from common.base.scene import BaseScene
from scenes.main_menu import MainMenuScene
from core.menu import Menu, MenuItem


class SettingsMenuScene(BaseScene):
    def __init__(self) -> None:
        BaseScene.__init__(self)

    def awake(self) -> None:
        print("[Awake]:", "SettingsMenu")
        self.menu = Menu()
        self.menu.add_item(MenuItem("Game", None))
        self.menu.add_item(MenuItem("Video", None))
        self.menu.add_item(MenuItem("Audio", None))
        self.menu.add_item(MenuItem("Back", self.on_back_selected))

    def update(self) -> None:
        return super().update()

    def render(self, screen: Surface) -> None:
        self.menu.on_draw(screen)

    def process(self, events: list[Event], pressed_keys: ScancodeWrapper) -> None:
        for event in events:
            self.menu.on_event(event)

    def destroy(self) -> None:
        print("[Destroy]:", "SettingsMenu")

    def on_back_selected(self) -> None:
        self.switch_to(MainMenuScene())
