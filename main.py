import random
import graphics as gra
import pygame


def neighbors(x, y, mmap):
    out = []
    w = len(mmap)
    h = len(mmap[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif w > x + i >= 0 and h > y + j >= 0:
                out.append((x + i, y + j))

    return out


def text_show(mmap, v=1):
    print("##" + "#" * len(mmap))
    for x in mmap:
        print("#", end="")
        for y in x:
            print(y[v], end="")
        print("#")
    print("##" + "#" * len(mmap))


def update_board(x, y, mmap):
    if mmap[x][y][0] is False:
        mmap[x][y][0] = True
        if mmap[x][y][1] == 0:
            for r, c in neighbors(x, y, mmap):
                # Repeat function for each neighbor that doesn't have a flag
                update_board(r, c, mmap)
        elif mmap[x][y][1] == -1:
            gra.end()


def list_remove(a, b):
    print("\nError: Tried to remove " + str(a) + " from " + str(b) + " however " + str(a) +
          " was not found.\n       This is probably fine.\n")


def event(current_events: object):
    for cevent in pygame.event.get():
        if cevent.type == pygame.QUIT:
            gra.end()
        elif cevent.type == pygame.MOUSEBUTTONDOWN:
            if cevent.button == 1:
                current_events.append("LEFT")
        elif cevent.type == pygame.MOUSEBUTTONUP:
            if cevent.button == 1:
                try:
                    current_events.remove("LEFT")
                except ValueError:
                    list_remove("LEFT", "currentEvents")
    return current_events


def generate(clicked, X, Y, mines):
    mmap = []
    for x in range(X):
        mmap.append([])
        for y in range(Y):
            mmap[x].append([False, 0])

    near_clicked = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if X > clicked[0] + i >= 0 and Y > clicked[1] + j >= 0:
                near_clicked.append((clicked[0] + i, clicked[1] + j))

    for mine in range(mines):
        while True:
            x = random.randrange(X)
            y = random.randrange(Y)
            if all((x, y) != z for z in near_clicked):
                mmap[x][y][1] = -1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if X > x + i >= 0 and Y > y + j >= 0:
                            if mmap[x+i][y+j][1] != -1:
                                mmap[x+i][y+j][1] += 1
                break

    update_board(clicked[0], clicked[1], mmap)
    return mmap


def check_victory(mmap, mines):
    total = 0
    while total <= mines:
        for x in mmap:
            for y in x:
                if y[0] is True:
                    total += 1
    if total <= mines:
        return True
    else:
        return False


if __name__ == "__main__":

    num_mines = 0
    board_x = 10
    board_y = 2

    block_size = 9
    gap = 1
    total_size = block_size + gap

    Map = generate((1, 0), board_y, board_x, num_mines)
    window_size = (total_size * board_x + 1, total_size * board_y + 1)
    print(total_size, window_size, sep=", ")
    window, clock, font = gra.start(window_size)
    gra.update(block_size, Map, window, font, gap)

    events = []
    while True:
        events = event(events)
        for x in events:
            if x == "LEFT":
                pos = pygame.mouse.get_pos()
                currentX, currentY = pos[0], pos[1]
                if 0 <= currentX < window_size[0] - 10 and 0 <= currentY < window_size[1] - 10:
                    update_board(currentY // 21, currentX // 21, Map)
                    gra.update(block_size, Map, window, font, gap)
                    if check_victory(Map, num_mines):
                        gra.end()
