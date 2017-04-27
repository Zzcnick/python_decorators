import time

def timer(func):
    start = time.time()
    def print_time(n):
        func(n)
        end = time.time()
        return "Execution Time: %.5f"%(end - start)
    return print_time

def inputs(func):
    def print_inputs(*arg):
        return 0 # PLACEHOLDER
    return print_inputs

@timer
def smart_fib(n):
    a = 0
    b = 1
    while n > 0:
        c = b
        b = a + b
        a = c
        n -= 1
    return a

@timer
def naive_fib(n):
    if n < 2:
        return n
    return naive_fib(n-1) + naive_fib(n-2)

print smart_fib(20)
print naive_fib(20)
