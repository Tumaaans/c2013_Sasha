class GeneratorIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration

def generator_example(start, end):
    for number in range(start, end):
        yield number

# Створюємо ітерований об'єкт
iterator = GeneratorIterator(1, 6)

# Використовуємо ітератор
for num in iterator:
    print(num)

# Використовуємо генератор
gen = generator_example(1, 6)
for num in gen:
    print(num)
