from common.constants import (
    DISPLAY_CAPTION,
    DISPLAY_SIZE,
    DISPLAY_FPS
)
from scenes import SceneLoader
from common.colors import BLACK_COLOR
import pygame


def run() -> None:
    pygame.init()
    pygame.display.set_caption(DISPLAY_CAPTION)
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    clock = pygame.time.Clock()

    SceneLoader.set("MainMenuScene")

    active_scene = SceneLoader.get()
    active_scene.awake()

    while active_scene != None:
        screen.fill(BLACK_COLOR)

        pressed_keys = pygame.key.get_pressed()

        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            if quit_attempt:
                SceneLoader.switch_to(None)
            else:
                filtered_events.append(event)

        active_scene.process(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen)

        pygame.display.flip()
        clock.tick(DISPLAY_FPS)

        active_scene = SceneLoader.get()

    pygame.quit()
