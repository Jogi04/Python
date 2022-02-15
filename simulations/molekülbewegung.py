import random


def molekuel_bewegung():
    position = {'rechts': 0, 'links': 0, 'oben': 0, 'unten': 0}
    for i in range(11):
        bewegung = random.choice(['rechts', 'links', 'oben', 'unten'])
        print(bewegung)
        if bewegung == 'rechts':
            position['rechts'] = position['rechts'] + 1
            position['links'] = position['links'] - 1
        elif bewegung == 'links':
            position['links'] = position['links'] + 1
            position['rechts'] = position['rechts'] - 1
        elif bewegung == 'oben':
            position['oben'] = position['oben'] + 1
            position['unten'] = position['unten'] - 1
        elif bewegung == 'unten':
            position['unten'] = position['unten'] + 1
            position['oben'] = position['oben'] - 1
        print(position)

        for j in position:
            if position[j] == 3:
                print(f'Anzahl an Sekunden bis ausserhalb: {i}')
                break
        else:
            continue
        break


if __name__ == '__main__':
    molekuel_bewegung()
