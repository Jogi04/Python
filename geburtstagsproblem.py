def geburtstag_problem(people, write_to_file=True):
    prob = 1
    for i in range(1, people + 1):
        prob = prob * (366 - i) / 365
        print(i)
        print(f'Wahrscheinlichkeit: {prob}')
        if write_to_file is True:
            with open('geburtstagsproblem.txt', 'a') as file:
                file.write(str(i) + '\n')
                file.write(f'Wahrscheinlichkeit: {prob}\n')
                file.close()


if __name__ == '__main__':
    geburtstag_problem(23)
