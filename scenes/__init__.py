from __future__ import annotations
from typing import TYPE_CHECKING, List
from importlib import util
from abc import ABC, abstractmethod
import os
import traceback

if TYPE_CHECKING:
    from pygame.event import Event
    from pygame.surface import Surface
    from pygame.key import ScancodeWrapper


class BaseScene(ABC):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return self.__class__.__name__

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


class SceneLoader:
    __scenes: List[BaseScene] = []
    __current_scene: BaseScene | None = None

    @classmethod
    def get(cls) -> BaseScene | None:
        return cls.__current_scene

    @classmethod
    def set(cls, name: str) -> None:
        cls.__current_scene = SceneLoader.find(name)

    @classmethod
    def find(cls, name: str) -> BaseScene | None:
        for scene in cls.__scenes:
            if scene.__str__() == name:
                return scene
        return None

    @classmethod
    def switch_to(cls, name: str | None) -> None:
        if cls.__current_scene:
            cls.__current_scene.destroy()
        if not name:
            SceneLoader.__current_scene = None
        next_scene = SceneLoader.find(name)
        if next_scene:
            next_scene.awake()
        SceneLoader.set(name)

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.__scenes.append(cls())


def load_scene(path) -> None:
    name = os.path.split(path)[-1]
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    if not fname.startswith('.') and \
       not fname.startswith('__') and fname.endswith('.py'):
        try:
            load_scene(os.path.join(dirpath, fname))
        except Exception:
            traceback.print_exc()
