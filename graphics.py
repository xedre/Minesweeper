import pygame

black = (50, 50, 50)


def start(screen_size):
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Minesweeper")
    pygame.display.update()
    font = pygame.font.SysFont('arial', 25)
    return display, clock, font


def end():
    pygame.quit()
    exit()


def background(display, colour=black):
    display.fill(colour)


def update(block_size, mine_map, screen):
    background(screen)
    for x in range(len(mine_map)):
        for y in range(len(mine_map[x])):
            screen.fill((0, 0 if mine_map[x][y][0] is False else 128, 0), rect=[x * (block_size + 1) + 1, y * (block_size + 1) + 1, block_size, block_size])
    pygame.display.update()
