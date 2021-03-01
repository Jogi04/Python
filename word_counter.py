#!/bin/python

class WordCounter:
    def __init__(self, file):
        self.file = file

    def count(self):
        with open(self.file) as file:
            data = file.read()
            words = data.split(' ')
            print(len(words))


if __name__ == '__main__':
    counter = WordCounter("test.txt")
    counter.count()
