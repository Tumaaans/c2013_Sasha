import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції '{func.__name__}': {execution_time} секунд")
        return result
    return wrapper
def test_function_to_measure():
    # Функція, яку ми будемо тестувати
    def some_function():
        result = 0
        for i in range(1000000):
            result += i
        return result

    # Вимірюємо час виконання some_function
    measured_function = measure_execution_time(some_function)
    result = measured_function()

    # Перевіряємо, чи функція виконана успішно і час більше 0
    assert result == 499999500000
    assert measured_function.__name__ == 'wrapper'
    assert measured_function.__doc__ == None

if __name__ == "__main__":
    test_function_to_measure()
    print("Тести пройдено успішно.")
