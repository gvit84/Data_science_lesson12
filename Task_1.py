from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time



def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

def thread_pool_executor():
    started_at = time.time()
    with ThreadPoolExecutor() as executor:
        fact1 = executor.submit(factorial, 10)
        fact2 = executor.submit(factorial, 20)
        print(f"factorial fact1 = {fact1.result()}")
        print(f"factorial fact2 = {fact2.result()}")
    t1 = time.time() - started_at
    print(f"Execution time with ThreadPoolExecutor is {t1} seconds")
    return t1

def process_pool_executor():
    started_at = time.time()
    with ProcessPoolExecutor() as executor:
        fact1 = executor.submit(factorial, 10)
        fact2 = executor.submit(factorial, 20)
        print(f"factorial fact1 = {fact1.result()}")
        print(f"factorial fact2 = {fact2.result()}")
    t2 = time.time() - started_at
    print(f"Execution time with ProcessPoolExecutor is {t2}")
    return t2

def faster():
    t1 = thread_pool_executor()
    print("--------------------------------------------------------------------------")
    t2 = process_pool_executor()
    print("--------------------------------------------------------------------------")
    if t1 > t2:
        print("ProcessPoolExecutor is faster")
    else:
        print("ThreadPoolExecutor is faster")

if __name__ == '__main__':
    faster()