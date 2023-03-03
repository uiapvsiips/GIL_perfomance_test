import threading
import multiprocessing
import time
import datetime
from pprint import pprint


def write_to_file(filename):
    str_list = []
    for i in range(10000):
        test_str = (str(datetime.datetime.now()) + '\n')
        with open(filename, 'a') as f:
                f.write(test_str + '\n')

def perfomance(func):
    """
    Функція-декоратор, що заміряє продуктивність
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"час виконання функції {func.__name__}: {end_time - start_time} секунд.\n")
        return result
    return wrapper

@perfomance
def multithreading_func():
    pprint('Inside multithreading_func')
    names = [
        "multithreading_test.txt",
        "multithreading_test1.txt"
    ]
    threads = []
    for i in range(2):
        t = threading.Thread(target=write_to_file(names[i-1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

@perfomance
def multiprocessing_func():
    pprint('Inside multiprocessing_func')
    names = [
        "multiprocessing_test.txt",
        "multiprocessing_test1.txt"
    ]
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(write_to_file, names)

@perfomance
def one_process_func():
    pprint('Inside one_process_func')
    write_to_file('one_process_test.txt')
    write_to_file('one_process_test1.txt')


if __name__ == '__main__':
    multiprocessing_func()
    multithreading_func()
    one_process_func()

