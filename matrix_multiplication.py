class MatrixMultiplication:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.check_type()
        self.result = [[0, 0], [0, 0]]

    def check_type(self):
        for i in range(len(self.matrix1)):
            if len(self.matrix1[i]) != len(self.matrix2):
                raise TypeError("Matrices are not the same type")

    def multiply(self):
        for line in range(len(self.matrix2) - 1):
            for column in range(len(self.matrix1[0]) - 1):
                for i in range(len(self.matrix1[line])):
                    self.result[line][column] += self.matrix1[line][i] * self.matrix2[i][column]

        return self.result

    def __str__(self):
        result_formatted = ""
        for i in range(len(self.result)):
            if i == len(self.result) - 1:
                result_formatted += f'{self.result[i]}'
            else:
                result_formatted += f'{self.result[i]}\n'
        return result_formatted


if __name__ == '__main__':
    m1 = [[1, 1, 3],
          [2, 7, 1]]

    m2 = [[3, 9],
          [4, 2],
          [4, 2]]

    res = MatrixMultiplication(m1, m2)
    res.multiply()
    print(res)
