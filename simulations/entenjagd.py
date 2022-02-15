import random

'''
    Problembeschreibung: 10 absolut treffsichere Jäger schießen gleichzeitig auf 10 Enten, wobei jeder Jäger sich sein
    Ziel zufällig aussucht
'''


def entenjagd(iterations):
    moeglichtkeiten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ueberlebende_enten = 0
    for i in range(iterations):
        enten = []
        for j in range(10):
            ente = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            enten.append(ente)
        enten_unterschied = []
        for k in moeglichtkeiten:
            if k not in enten:
                enten_unterschied.append(k)
        ueberlebende_enten = ueberlebende_enten + len(enten_unterschied)
        print(f'{enten} ; {enten_unterschied} ; {len(enten_unterschied)}')
    print(f'Durchschnitt überlebender Enten: {ueberlebende_enten / iterations}')


if __name__ == '__main__':
    entenjagd(100000)
