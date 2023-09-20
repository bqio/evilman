from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game import Game


class GameObject:
    def __init__(self, parent: Game) -> None:
        self.parent = parent
