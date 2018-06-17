import random
import graphics as gra


def generate(clicked, X, Y, mines):
    mmap = []
    for x in range(X):
        mmap.append([])
        for y in range(Y):
            mmap[x].append([False, 1])

    nearClicked = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if X > clicked[0] + i >= 0 and Y > clicked[1] + j>= 0:
                nearClicked.append((clicked[0] + i, clicked[1] + j))

    for mine in range(mines):
        while True:
            x = random.randrange(X)
            y = random.randrange(Y)
            if all((x, y) != z for z in nearClicked):
                mmap[x][y][1] = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if X > x + i >= 0 and Y > y + j >= 0:
                            if mmap[x+i][y+j][1] != 0:
                                mmap[x+i][y+j][1] += 1
                break

    return mmap


if __name__ == "__main__":
    Map = generate((1, 1), 10, 10, 10)
    window, clock, font = gra.start((200, 200))
    gra.update(20, Map, window)
    while True:
        pass
