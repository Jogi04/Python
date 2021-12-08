import threading
import time


class test(threading.Thread):
    def __init__(self, identification):
        super().__init__()
        self.identification = identification

    def run(self):
        print(f'started {self.identification}')
        time.sleep(3)
        print(f'finished {self.identification}')


if __name__ == '__main__':
    print('started main thread')
    t1 = test('1')
    t1.start()
    time.sleep(1)
    t2 = test('2')
    t2.start()
    print('finished main thread')
