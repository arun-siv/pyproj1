from urllib.parse import urlparse

class MyBomb:
    def __init__(self, start):
        print(f'Activating the bomb in {start} sec.')
        self.start = start

    def __iter__(self):
        return MyBombIterator(self.start)


class MyBombIterator:
    def __init__(self, count):
        self.count = count

    def __next__(self):
        if self.count <= 0:
            print("BAMMMMM!!!!")
            raise StopIteration
        value = self.count
        self.count -= 1
        return value


for i in MyBomb(6):
    print(i)
