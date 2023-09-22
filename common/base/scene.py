from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from pygame.key import ScancodeWrapper


class BaseScene(ABC):
    def __init__(self) -> None:
        self.next = self

    @abstractmethod
    def awake(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def process(self, events: list[Event], pressed_keys: ScancodeWrapper) -> None:
        pass

    @abstractmethod
    def render(self, screen: Surface) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        pass

    def switch_to(self, next_scene: BaseScene) -> None:
        if self.next:
            self.next.destroy()
        if next_scene:
            next_scene.awake()
        self.next = next_scene

    def kill(self) -> None:
        self.switch_to(None)
