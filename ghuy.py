def raise_to(num, max_degree):
    i = 0
    while True:
        result = num ** i
        yield result
        if result > 100**20:
            return
        i += 1

res = raise_to(122345, 500)
print(res)
for _ in res:
    print(_)
    print("-"*20)