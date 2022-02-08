def geburtstag_problem(people):
    prob = 1
    for i in range(1, people + 1):
        print(i)
        prob = prob * (366 - i) / 365
        print(f'Wahrscheinlichkeit: {prob}')


if __name__ == '__main__':
    geburtstag_problem(23)
