class Counter:
    def __init__(self, max_namber):
        self.i = 0
        self.max_namber = max_namber

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_namber:
            raise StopIteration
        return self.i


count = Counter(5)
'''for elem in count:
    print(elem)
  '''

print(count. __next__())
print(count. __next__())
print(next(count))
print(iter(count))
print(next(count))

