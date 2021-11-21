class MatrixAddition:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.result = matrix1

    def add(self):
        for line in range(len(self.matrix1)):
            for column in range(len(self.matrix1[0])):
                self.result[line][column] = self.matrix1[line][column] + self.matrix2[line][column]

        for i in self.result:
            print(i)


if __name__ == '__main__':
    m1 = [[1, 1, 3],
          [4, -2, 6]]

    m2 = [[3, 9, 4],
          [4, 2, 3]]

    addition = MatrixAddition(m1, m2)
    addition.add()
