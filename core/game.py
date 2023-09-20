from pygame import init, quit
from core.display_manager import DisplayManager
from core.event_manager import EventManager
from core.state_manager import StateManager
from states.main_menu import MainMenuState
from states.settings_menu import SettigsMenuState


class Game:
    def __init__(self) -> None:
        init()
        self.state_manager = StateManager(self)
        self.display_manager = DisplayManager(self)
        self.event_manager = EventManager(self)

    def run(self) -> None:
        self.state_manager.add_state(MainMenuState(self))
        self.state_manager.add_state(SettigsMenuState(self))
        self.event_manager.loop()
        quit()
