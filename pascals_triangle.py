def triangle(lines):
    if lines < 2:
        raise ValueError('Number of lines must be greater than or equal to 2')
    print('1')
    print('1 ; 1')
    last_line = [1, 1]
    for i in range(lines - 2):
        print('1', end=' ; ')
        current_line = [1]
        for j in range(len(last_line) - 1):
            print(last_line[j] + last_line[j + 1], end=' ; ')
            current_line.append(last_line[j] + last_line[j + 1])
        print('1')
        current_line.append(1)
        last_line = current_line


if __name__ == '__main__':
    triangle(10)
