import random
import graphics as gra


def text_show(mmap, v=1):
    print("#" + "#" * len(mmap))
    for x in mmap:
        print("#", end="")
        for y in x:
            print(y[v], end="")
        print("#")
    print("#" + "#" * len(mmap))


def update_board(x, y, mmap):
    print("apples")
    X = len(mmap)
    Y = len(mmap[0])
    if mmap[x][y][0] is False:
        mmap[x][y][0] = True
        if mmap[x][y][1] == 1:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    print(1)
                    if X > x + i >= 0 and Y > y + j >= 0:
                        print(2)
                        if mmap[x + i][y + j][0] is False:
                            print(3)
                            mmap[x + i][y + j][0] = True
                            if mmap[x + i][y + j][1] == 1:
                                print(x + i, y + j, sep=",")
                                update_board(x + i, y + j, mmap)


def generate(clicked, X, Y, mines):
    mmap = []
    for x in range(X):
        mmap.append([])
        for y in range(Y):
            mmap[x].append([False, 1])

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
                mmap[x][y][1] = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if X > x + i >= 0 and Y > y + j >= 0:
                            if mmap[x+i][y+j][1] != 0:
                                mmap[x+i][y+j][1] += 1
                break

    update_board(clicked[0], clicked[1], mmap)
    return mmap


if __name__ == "__main__":
    Map = generate((1, 1), 10, 10, 5)
    text_show(Map)
    window, clock, font = gra.start((220, 220))
    gra.update(20, Map, window)
    while True:
        pass
