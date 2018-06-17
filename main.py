import random


def generate(clicked, X, Y, mines):
    mmap = []
    for x in range(X):
        mmap.append([])
        for y in range(Y):
            mmap[x].append(1)

    nearclicked = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if X > clicked[0] + i >= 0 and Y > clicked[1] + j>= 0:
                nearclicked.append((clicked[0] + i, clicked[1] + j))

    for mine in range(mines):
        while True:
            x = random.randrange(X)
            y = random.randrange(Y)
            if any((x, y) != x for x in nearclicked):
                mmap[x][y] = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if X > x + i >= 0 and Y > y + j >= 0:
                            if mmap[x+i][y+j] != 0:
                                mmap[x+i][y+j] += 1
                                break

    for x in mmap:
        for y in x:
            print(y, end="")
        print()


if __name__ == "__main__":
    generate((1, 1), 5, 10, 10)
