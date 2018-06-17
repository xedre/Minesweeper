import pygame

black = (50, 50, 50)


def start(screenSize):
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Minesweeper")
    pygame.display.update()
    font = pygame.font.SysFont('arial', 25)
    return display, clock, font


def end():
    pygame.quit()
    exit()


def background(display, colour=black):
    display.fill(colour)


def update(blockSize, Map, screen):
    background(screen)
    for x in range(len(Map)):
        for y in range(len(Map[x])):
            screen.fill((0, 0 if Map[x][y][0] is False else 128, 0), rect=[x * (blockSize + 1) + 1, y * (blockSize + 1) + 1, blockSize, blockSize])
    pygame.display.update()
