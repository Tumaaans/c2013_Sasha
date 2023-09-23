result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або рівне b")
        if b > 100:
            raise IndexError("b не може бути більше 100")
        result = a / b
    except ValueError as ve:
        print(f"Помилка ValueError: {ve}")
        result = None
    except IndexError as ie:
        print(f"Помилка IndexError: {ie}")
        result = None
    except Exception as e:
        print(f"Інша помилка: {e}")
        result = None
    return result

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key, value in data.items():
    res = divider(key, value)
    result.append(res)

print(result)
