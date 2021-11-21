import sys


class MatrixAddition:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.result = matrix1
        self.check_same_type()

    def check_same_type(self):
        if len(self.matrix1) != len(self.matrix2):
            print('Not the same type!!!')
            sys.exit()
        for i in range(len(self.matrix1)):
            if len(self.matrix1[i]) != len(self.matrix2[i]):
                print('Not the same type!!!')
                sys.exit()

    def add(self):
        for line in range(len(self.matrix1)):
            for column in range(len(self.matrix1[0])):
                self.result[line][column] = self.matrix1[line][column] + self.matrix2[line][column]

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

    m2 = [[3, 9, 4],
          [4, 2, 3]]

    res = MatrixAddition(m1, m2)
    res.add()
    print(res)
