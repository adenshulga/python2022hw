M = {0: 0, 1: 1}

def fib(n):
    if n in M:
        return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]

def fib_gen(n):
    i = 0
    while i != n:
        yield fib(i)
        i += 1

for i in fib_gen(10):
    print(i)
