import random


def flip(iterations):
    for i in range(iterations):
        print(f'{i}: {random.choice(["Kopf", "Zahl"])}')


if __name__ == '__main__':
    flip(30)
