import time
import os
from functools import wraps

def timer(func):
    def f(*arg, **kwarg):
        before = time.time()
        rv = func(*arg, **kwarg)
        after = time.time()
        print("--- %s seconds ---" %(after - before))
        return rv
    return f

def print_param(name_output, BASE_DIR):
    def print_result(func):
        '''
        print_result(sockMerchant(n,ar),"output_sock.txt", BASE_DIR)
        :param func:
        :param name_output:
        :param BASE_DIR:
        :return:
        '''
        @wraps(func)
        def f(*arg, **kwarg):
            output = os.path.join(BASE_DIR, name_output)
            if os.path.exists(output):
                f = open(output, "r+")
            else:
                f = open(output, "w")
            result = func(*arg, **kwarg)
            f.write(str(result))
            f.close()
            myfile = open(output, 'r+')
            print(myfile.readlines())
            return result
        return f
    return print_result


@timer
def add(a,b):
    result = a + b
    return result

if __name__ == "__main__":
    print(add(2,3))
