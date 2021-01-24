from time import time

def timer(func):
    def f(*arg, **kwarg):
        before = time.time()
        rv = func(*arg, **kwarg)
        after = time.time()
        print("--- %s seconds ---" %(after - before))
        return rv
    return f

@timer
def add(a,b):
    result = a + b
    return result

if __name__ == "__main__":
    print(add(2,3))
