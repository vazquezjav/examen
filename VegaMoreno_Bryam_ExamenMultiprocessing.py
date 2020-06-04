import random
import time
import multiprocessing

def how_many_max_values_parallel(val):
    if val == max(ar):
        return 1
    else:
        return 0

if __name__ == '__main__':
    ar_count = 4
    ar = [random.randrange(1,30) for i in range(ar_count)]
    inicioPar = time.time()
    pool                    = multiprocessing.Pool(processes=4)
    resultPar = sum(list(pool.map(how_many_max_values_parallel,ar)))
    finPar = time.time()   
    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))
