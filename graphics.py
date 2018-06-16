import pygame


def start(screenSize):
    pygame.init()
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Minesweeper")
    pygame.display.update()
    font = pygame.font.SysFont('arial', 25)
    return gameDisplay, clock, font


def end():
    pygame.quit()
    exit()