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
            if X > clicked[0 + i] >= 0 and Y > clicked[1 + j] >= 0:
                nearclicked.append((clicked[0 + i], clicked[1 + j]))

    for mine in range(mines):
        while True:
            x = random.randrange(X)
            y = random.randrange(Y)


if __name__ == "__main__":
    pass
