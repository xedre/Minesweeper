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


def text(msg, colour, x, y, window, font):
    screen_text = font.render(msg, True, colour)
    window.blit(screen_text, [x, y])


def update(block_size, mine_map, screen, font):
    background(screen)
    for x in range(len(mine_map)):
        for y in range(len(mine_map[x])):
            if mine_map[x][y][0] is False:
                screen.fill((0, 0, 0), rect=[y * (block_size + 1) + 1, x * (block_size + 1) + 1, block_size, block_size])
            else:
                screen.fill((150, 150, 150), rect=[y * (block_size + 1) + 1, x * (block_size + 1) + 1, block_size, block_size])
                if mine_map[x][y][1] == 0:
                    show = ""
                elif mine_map[x][y][1] == -2:
                    show = "F"
                else:
                    show = str(mine_map[x][y][1])
                text(show, black, y * (block_size + 1) + 5, x * (block_size + 1) + 2, screen, font)
    pygame.display.update()
