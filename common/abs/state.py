from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from .game_object import GameObject

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from core.game import Game


class State(ABC, GameObject):
    def __init__(self, parent: Game) -> None:
        super().__init__(parent)

    @abstractmethod
    def on_draw(self, surface: Surface) -> None:
        pass

    @abstractmethod
    def on_update(self) -> None:
        pass

    @abstractmethod
    def on_event(self, event: Event) -> None:
        pass
