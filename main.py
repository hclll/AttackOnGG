import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario
from entities.Mario1 import Mario1


windowSize = 640, 480


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound, windowSize, menu)
    if menu.playerNum == 2:
        mario1 = Mario1(0.01, 0, level, screen, dashboard, sound, windowSize, menu)

    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption("Attack on GG")
        if mario.pause:
            mario.pauseObj.update()
        else:
            if menu.playerNum == 2:
                pos0 = mario.getPosIndexAsFloat().x
                pos1 = mario1.getPosIndexAsFloat().x
                if pos0 > pos1:
                    cam = mario.camera
                else:
                    cam = mario1.camera
            else:
                cam = mario.camera
            level.drawLevel(cam)

            dashboard.update()
            mario.update()
            if menu.playerNum == 2:
                mario1.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    return 'restart'


if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
