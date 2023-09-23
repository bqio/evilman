from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from pygame.key import ScancodeWrapper

from scenes import SceneLoader, BaseScene
from core.menu import Menu, MenuItem


class SettingsMenuScene(BaseScene, SceneLoader):
    def __init__(self) -> None:
        BaseScene.__init__(self)

    def awake(self) -> None:
        print("[Awake]:", "SettingsMenu")
        self.menu = Menu()
        self.menu.add_item(MenuItem("Game", self.on_game_selected))
        self.menu.add_item(MenuItem("Video", self.on_video_selected))
        self.menu.add_item(MenuItem("Audio", self.on_audio_selected))
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

    def on_game_selected(self) -> None:
        pass

    def on_video_selected(self) -> None:
        pass

    def on_audio_selected(self) -> None:
        pass

    def on_back_selected(self) -> None:
        SceneLoader.switch_to("MainMenuScene")
