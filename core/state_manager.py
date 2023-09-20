from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game import Game

from common.abs.state import State
from common.abs.game_object import GameObject


class StateManager(GameObject):
    def __init__(self, parent: Game) -> None:
        super().__init__(parent)

        self.states = []
        self.state_index = 0

    def add_state(self, state: State) -> None:
        self.states.append(state)

    def set_state(self, state_index: int) -> None:
        if state_index > len(self.states) - 1:
            self.state_index = 0
        else:
            self.state_index = state_index

    def get_state(self) -> State:
        return self.states[self.state_index]

    def next_state(self) -> None:
        self.set_state(self.state_index + 1)
