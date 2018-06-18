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


def events(current_events: object):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                current_events.append("LEFT")
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
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


if __name__ == "__main__":
    Map = generate((1, 0), 10, 10, 10)
    text_show(Map)
    window_size = (220, 220)
    window, clock, font = gra.start(window_size)
    gra.update(20, Map, window, font)

    events = []
    while True:
        events = gra.events(events)
        for x in events:
            if x == "LEFT":
                pos = pygame.mouse.get_pos()
                currentX, currentY = pos[0], pos[1]
                if 0 <= currentX < window_size[0] - 10 and 0 <= currentY < window_size[1] - 10:
                    update_board(currentY // 21, currentX // 21, Map)
                    gra.update(20, Map, window, font)
